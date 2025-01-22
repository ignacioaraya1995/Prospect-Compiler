import os
import pandas as pd
from prettytable import PrettyTable

def unify_duplicate_columns(df, suffix_1='_8020', suffix_2='_other'):
    """
    For columns that appear in the DataFrame with suffixes `_8020` and `_other`,
    combine them into a single column without the suffix, preferring `_8020`
    non-null values over `_other` where they overlap.
    """
    col_set = set(df.columns)
    base_names = set()

    for col in col_set:
        if col.endswith(suffix_1):
            base_names.add(col.replace(suffix_1, ''))
        elif col.endswith(suffix_2):
            base_names.add(col.replace(suffix_2, ''))

    for base in base_names:
        col_8020 = base + suffix_1
        col_other = base + suffix_2
        if col_8020 in df.columns and col_other in df.columns:
            df[base] = df[col_8020].combine_first(df[col_other])
            df.drop(columns=[col_8020, col_other], inplace=True)
        elif col_8020 in df.columns:
            df.rename(columns={col_8020: base}, inplace=True)
        elif col_other in df.columns:
            df.rename(columns={col_other: base}, inplace=True)

    return df

def main():
    print("Welcome! This script will compile two Excel prospect files into one, removing duplicates.")
    print("--------------------------------------------------------------------------------------\n")
    print("NOTE: This code only works if both files contain columns named ADDRESS, ZIP, COUNTY.\n")

    # STEP 1: Read 8020REI file
    path_8020 = input("Please enter the full path for the 8020REI prospect list Excel file (You can drag & drop the file):\n> ")
    while not os.path.isfile(path_8020):
        print(f"ERROR: The file '{path_8020}' does not exist. Please try again.")
        path_8020 = input("Please enter a valid path for the 8020REI Excel file:\n> ")

    print("\nReading 8020REI file. Please wait...")
    df_8020 = pd.read_excel(path_8020)
    print(f"Successfully read {len(df_8020):,} rows from 8020REI file.\n")

    # STEP 2: Read other data provider file
    path_other = input("Please enter the full path for the other data provider prospect Excel file (You can drag & drop the file):\n> ")
    while not os.path.isfile(path_other):
        print(f"ERROR: The file '{path_other}' does not exist. Please try again.")
        path_other = input("Please enter a valid path for the other data provider Excel file:\n> ")

    print("\nReading other data provider file. Please wait...")
    df_other = pd.read_excel(path_other)
    print(f"Successfully read {len(df_other):,} rows from the other data provider file.\n")

    # STEP 3: Check required columns
    required_columns = ['ADDRESS', 'ZIP', 'COUNTY']
    for col in required_columns:
        if col not in df_8020.columns:
            raise ValueError(f"ERROR: 8020REI file does not contain required column: {col}")
        if col not in df_other.columns:
            raise ValueError(f"ERROR: Other data provider file does not contain required column: {col}")

    print("Merging both data sets on ADDRESS, ZIP, and COUNTY...")
    df_8020['__8020_rei__'] = True
    df_other['__other_provider__'] = True

    merged_df = pd.merge(
        df_8020,
        df_other,
        on=['ADDRESS', 'ZIP', 'COUNTY'],
        how='outer',
        suffixes=('_8020', '_other')
    )
    print(f"Number of rows after merge (before dropping duplicates): {len(merged_df):,}\n")

    # STEP 4: Remove duplicates & Create prospect_file_source
    merged_df['__8020_rei__'] = merged_df['__8020_rei__'].notna()
    merged_df['__other_provider__'] = merged_df['__other_provider__'].notna()

    merged_df.drop_duplicates(subset=['ADDRESS', 'ZIP', 'COUNTY'], inplace=True)
    print(f"Number of rows after ensuring unique [ADDRESS, ZIP, COUNTY]: {len(merged_df):,}\n")

    def get_source(row):
        if row['__8020_rei__'] and row['__other_provider__']:
            return 'both'
        elif row['__8020_rei__']:
            return '8020REI only'
        else:
            return 'other data provider only'

    merged_df['prospect_file_source'] = merged_df.apply(get_source, axis=1)

    # STEP 5: Unify duplicate columns & Print Summary
    merged_df = unify_duplicate_columns(merged_df, '_8020', '_other')
    merged_df.drop(columns=['__8020_rei__', '__other_provider__'], inplace=True)

    total_8020_only = (merged_df['prospect_file_source'] == '8020REI only').sum()
    total_other_only = (merged_df['prospect_file_source'] == 'other data provider only').sum()
    total_both = (merged_df['prospect_file_source'] == 'both').sum()
    total_overall = len(merged_df)

    print("\nSummary of Sources:")
    table = PrettyTable()
    table.field_names = ["Category", "Count", "Percentage"]

    def pct(part, whole):
        return f"{(part / whole) * 100:.2f}%" if whole != 0 else "0%"

    table.add_row(["8020REI only", f"{total_8020_only:,}", pct(total_8020_only, total_overall)])
    table.add_row(["Other data provider only", f"{total_other_only:,}", pct(total_other_only, total_overall)])
    table.add_row(["Both", f"{total_both:,}", pct(total_both, total_overall)])
    table.add_row(["Total", f"{total_overall:,}", "100%" if total_overall != 0 else "0%"])

    print(table, "\n")

    print("Compiling the file, this may take a couple of seconds...")
    output_file = "compile_prospect_file.xlsx"
    merged_df.to_excel(output_file, index=False)
    print(f"Final compiled Excel file is saved as '{output_file}' in the current directory.")

    print("\nDone. Thank you for using this script!")

if __name__ == "__main__":
    main()