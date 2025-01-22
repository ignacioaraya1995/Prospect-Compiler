# Prospect File Compiler

**Prospect File Compiler** is a Python-based tool designed to efficiently merge and deduplicate two Excel prospect files. By focusing on the `ADDRESS`, `ZIP`, and `COUNTY` columns, this script ensures that your compiled prospect list is accurate and free from duplicates. The final output is a consolidated Excel file named `compile_prospect_file.xlsx`.

## Table of Contents

- [Prospect File Compiler](#prospect-file-compiler)
	- [Table of Contents](#table-of-contents)
	- [Features](#features)
	- [Requirements](#requirements)
		- [Python Version](#python-version)
		- [Dependencies](#dependencies)
	- [Installation](#installation)
	- [Usage](#usage)
		- [Input Files](#input-files)
		- [Running the Script](#running-the-script)
			- [On macOS](#on-macos)
			- [On Windows](#on-windows)
	- [Example Run](#example-run)
		- [Script Output](#script-output)
		- [Output File](#output-file)
	- [Troubleshooting](#troubleshooting)
		- [Common Errors and Solutions](#common-errors-and-solutions)
			- [1. File Not Found](#1-file-not-found)
			- [2. Missing Required Columns](#2-missing-required-columns)
			- [3. FutureWarning: Downcasting Object Dtype Arrays](#3-futurewarning-downcasting-object-dtype-arrays)
	- [License](#license)

## Features

- **Merge Two Prospect Files**: Combines data from both Excel files based on the `ADDRESS`, `ZIP`, and `COUNTY` columns.
- **Remove Duplicates**: Ensures that each row in the compiled file is unique based on the specified columns.
- **Track Sources**: Adds a `prospect_file_source` column to indicate the origin of each record:
  - `8020REI only`
  - `Other data provider only`
  - `Both`
- **Unified Columns**: Merges duplicate columns with different suffixes (e.g., `_8020` and `_other`) into single, unified columns.
- **Progress Tracking**: Provides real-time progress updates during the merging and deduplication process.

## Requirements

### Python Version

- **Python 3.7** or later

### Dependencies

Install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

**Required Libraries:**

- [`pandas`](https://pandas.pydata.org/) - Data manipulation and analysis.
- [`openpyxl`](https://openpyxl.readthedocs.io/) - Excel file handling.
- [`prettytable`](https://prettytable.readthedocs.io/) - Displaying tabular data in the terminal.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/prospect-file-compiler.git
   ```

2. **Navigate to the Directory:**

   ```bash
   cd prospect-file-compiler
   ```

3. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Input Files

Ensure that both input Excel files meet the following criteria:

1. **Required Columns (All in Uppercase):**
   - `ADDRESS`
   - `ZIP`
   - `COUNTY`

2. **File Format:**
   - Must be Excel files with a `.xlsx` extension.

### Running the Script

#### On macOS

1. **Open Terminal.**

2. **Navigate to the Script Directory:**

   ```bash
   cd /path/to/Prospect-Compiler
   ```

3. **Activate the Virtual Environment (If Applicable):**

   ```bash
   source venv/bin/activate
   ```

4. **Run the Script:**

   ```bash
   python3 main.py
   ```

5. **Follow the Prompts:**
   - Provide the full paths to the two Excel prospect files when prompted.

#### On Windows

1. **Open Command Prompt or PowerShell.**

2. **Navigate to the Script Directory:**

   ```bash
   cd C:\path\to\Prospect-Compiler
   ```

3. **Activate the Virtual Environment (If Applicable):**

   ```bash
   venv\Scripts\activate
   ```

4. **Run the Script:**

   ```bash
   python main.py
   ```

5. **Follow the Prompts:**
   - Provide the full paths to the two Excel prospect files when prompted.

## Example Run

### Script Output

```plaintext
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
```

### Output File

- **`compile_prospect_file.xlsx`**: The resulting compiled Excel file will be saved in the same directory as the script.

## Troubleshooting

### Common Errors and Solutions

#### 1. File Not Found

**Error Message:**
```plaintext
ERROR: The file '<path>' does not exist.
```

**Solution:**
- Verify that the file path you provided is correct.
- Ensure the file exists at the specified location.
- You can drag and drop the file into the terminal or command prompt to automatically obtain the full path.

#### 2. Missing Required Columns

**Error Message:**
```plaintext
ValueError: File does not contain required column: ...
```

**Solution:**
- Ensure that both Excel files contain the columns `ADDRESS`, `ZIP`, and `COUNTY` in uppercase.
- Check for any typos or case mismatches in the column headers.
- Open the Excel files and confirm the presence and correct naming of the required columns.

#### 3. FutureWarning: Downcasting Object Dtype Arrays

**Warning Message:**
```plaintext
FutureWarning: Downcasting object dtype arrays on .fillna is deprecated...
```

**Solution:**
- Update the script and the `pandas` library to the latest version:

  ```bash
  pip install --upgrade pandas
  ```

## License

This project is licensed under the [MIT License](LICENSE).
