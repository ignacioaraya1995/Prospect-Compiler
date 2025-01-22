# Prospect File Compiler

**Prospect File Compiler** is a Python script designed to merge and deduplicate two Excel prospect files based on specific columns. This tool ensures that your compiled prospect list is clean, accurate, and free of duplicates, making it easier to manage and analyze your data.

## Table of Contents

- [Prospect File Compiler](#prospect-file-compiler)
	- [Table of Contents](#table-of-contents)
	- [Features](#features)
	- [Requirements](#requirements)
		- [Python Version](#python-version)
		- [Dependencies](#dependencies)
	- [Welcome! This script will compile two Excel prospect files into one, removing duplicates.](#welcome-this-script-will-compile-two-excel-prospect-files-into-one-removing-duplicates)

## Features

- **Merge Two Prospect Files**: Combines data from both files based on `ADDRESS`, `ZIP`, and `COUNTY`.
- **Remove Duplicates**: Ensures unique rows by eliminating duplicates based on the specified columns.
- **Track Sources**: Adds a `prospect_file_source` column to indicate the origin of each record:
  - `8020REI only`
  - `Other data provider only`
  - `Both`
- **Unified Columns**: Merges duplicate columns with different suffixes (e.g., `_8020` and `_other`) into a single column.

## Requirements

### Python Version

- Python **3.7** or later

### Dependencies

Install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt

Required Libraries:
	•	pandas
	•	openpyxl
	•	prettytable

Installation
	1.	Clone the Repository:

git clone https://github.com/yourusername/prospect-file-compiler.git


	2.	Navigate to the Directory:

cd prospect-file-compiler


	3.	Create a Virtual Environment (Optional but Recommended):

python3 -m venv venv


	4.	Activate the Virtual Environment:
	•	macOS/Linux:

source venv/bin/activate


	•	Windows:

venv\Scripts\activate


	5.	Install Dependencies:

pip install -r requirements.txt



Usage

Input Files

Ensure that both input Excel files meet the following criteria:
	1.	Required Columns (All in Uppercase):
	•	ADDRESS
	•	ZIP
	•	COUNTY
	2.	File Format:
	•	Must be Excel files with a .xlsx extension.

Running the Script

On macOS
	1.	Open Terminal.
	2.	Navigate to the Script Directory:

cd /path/to/Prospect-Compiler


	3.	Activate the Virtual Environment (If Applicable):

source venv/bin/activate


	4.	Run the Script:

python3 main.py


	5.	Follow the Prompts:
	•	Provide the full paths to the two Excel prospect files when prompted.

On Windows
	1.	Open Command Prompt or PowerShell.
	2.	Navigate to the Script Directory:

cd C:\path\to\Prospect-Compiler


	3.	Activate the Virtual Environment (If Applicable):

venv\Scripts\activate


	4.	Run the Script:

python main.py


	5.	Follow the Prompts:
	•	Provide the full paths to the two Excel prospect files when prompted.

Example Run

Script Output

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

Output File
	•	compile_prospect_file.xlsx: The resulting compiled Excel file will be saved in the same directory as the script.

Troubleshooting

Common Errors and Solutions

1. File Not Found

Error Message:

ERROR: The file '<path>' does not exist.

Solution:
	•	Verify that the file path you provided is correct.
	•	You can drag and drop the file into the terminal or command prompt to automatically get the full path.

2. Missing Required Columns

Error Message:

ValueError: File does not contain required column: ...

Solution:
	•	Ensure that both Excel files contain the columns ADDRESS, ZIP, and COUNTY in uppercase.
	•	Check for any typos or case mismatches in the column headers.

3. FutureWarning: Downcasting Object Dtype Arrays

Warning Message:

FutureWarning: Downcasting object dtype arrays on .fillna is deprecated

Solution:
	•	The script has been updated to address this warning. Make sure you are using the latest version of the script.
	•	If the warning persists, consider updating the pandas library or modifying the script as suggested in the warning message.

License

This project is licensed under the MIT License.

Feel free to contribute, report issues, or suggest enhancements!

This README was generated and improved to provide clear and comprehensive documentation for the Prospect File Compiler project.

