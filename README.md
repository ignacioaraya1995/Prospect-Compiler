Here’s the documentation in README.md format:

Prospect File Compiler

This script compiles two Excel prospect files into one by merging and deduplicating based on ADDRESS, ZIP, and COUNTY. It is specifically designed to work with files exported from a system that uses these exact column headers. The resulting file is saved as compile_prospect_file.xlsx.

Features
	•	Merge two prospect files: Combines data from both files based on ADDRESS, ZIP, and COUNTY.
	•	Remove duplicates: Ensures unique rows based on the combination of these three columns.
	•	Track sources: Adds a prospect_file_source column to indicate whether a record is from:
	•	8020REI only
	•	Other data provider only
	•	Both
	•	Unified columns: Merges duplicate columns with different suffixes (e.g., _8020 and _other) into a single column.

Requirements

Python Version
	•	Python 3.7 or later

Dependencies

Install the required libraries using requirements.txt:

pip install -r requirements.txt

The required libraries are:
	•	pandas
	•	openpyxl
	•	prettytable

Usage Instructions

Input Files
	1.	Both input files must contain the following columns in uppercase:
	•	ADDRESS
	•	ZIP
	•	COUNTY
	2.	Ensure the files are Excel files (.xlsx).

Steps to Run

On macOS
	1.	Open Terminal.
	2.	Navigate to the script directory:

cd /path/to/Prospect-Compiler


	3.	Activate your virtual environment (if applicable):

source venv/bin/activate


	4.	Run the script:

python3 main.py


	5.	Follow the prompts to provide the full paths to the two Excel files.

On Windows
	1.	Open Command Prompt (or PowerShell).
	2.	Navigate to the script directory:

cd C:\path\to\Prospect-Compiler


	3.	Activate your virtual environment (if applicable):

venv\Scripts\activate


	4.	Run the script:

python main.py


	5.	Follow the prompts to provide the full paths to the two Excel files.

Example Run
	1.	Script Output:

Welcome! This script will compile two Excel prospect files into one, removing duplicates.
--------------------------------------------------------------------------------------

NOTE: This code only works if both files contain columns named ADDRESS, ZIP, COUNTY.

Please enter the full path for the 8020REI prospect list Excel file:
> /path/to/8020REI_Prospects.xlsx

Reading 8020REI file. Please wait...
Successfully read 149,598 rows from 8020REI file.

Please enter the full path for the other data provider prospect Excel file:
> /path/to/OtherDataProvider_Prospects.xlsx

Reading other data provider file. Please wait...
Successfully read 62,297 rows from the other data provider file.

Merging both data sets on ADDRESS, ZIP, and COUNTY...
Number of rows after merge (before dropping duplicates): 199,089
Number of rows after ensuring unique [ADDRESS, ZIP, COUNTY]: 197,779

Summary of Sources:
+--------------------------+---------+------------+
|         Category         |  Count  | Percentage |
+--------------------------+---------+------------+
|       8020REI only       | 135,484 |   68.50%   |
| Other data provider only |  49,489 |   25.02%   |
|           Both           |  12,806 |   6.47%    |
|          Total           | 197,779 |    100%    |
+--------------------------+---------+------------+ 

Compiling the file, this may take a couple of seconds...
Final compiled Excel file is saved as 'compile_prospect_file.xlsx' in the current directory.

Done. Thank you for using this script!


	2.	Output File:
	•	The resulting file compile_prospect_file.xlsx will be saved in the same directory as the script.

Troubleshooting

Error: ERROR: The file '<path>' does not exist.
	•	Ensure the file path is correct. You can drag and drop the file into the terminal/command prompt to get the full path.

Error: ValueError: File does not contain required column: ...
	•	Ensure the files have the columns ADDRESS, ZIP, and COUNTY in uppercase.

Warning: FutureWarning: Downcasting object dtype arrays on .fillna is deprecated
	•	This issue has been addressed in the script. If you still encounter this warning, ensure you are running the latest version of the script.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to update this README with any additional details specific to your project or environment.