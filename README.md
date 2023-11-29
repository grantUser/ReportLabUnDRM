# ReportLabUnDRM

## Overview

The ReportLabUnDRM script is designed to remove the ReportLab watermark from a PDF file. It is implemented as a command-line tool, allowing users to specify the PDF file they want to process.

## Usage

1. **Installation:** Ensure you have Python installed on your machine.

2. **Clone the Repository:**
   ```
   git clone https://github.com/grantUser/ReportLabUnDRM.git
   cd ReportLabUnDRM
   ```

3. **Run the Script:**
   ```
   python ReportLabUnDRM.py path/to/your/file.pdf
   ```

## Features

- **Remove Watermark:** The script identifies the ReportLab watermark in the second and tenth lines (from the end) of the PDF file and removes these lines.
  
- **New File Generation:** After removing the watermark, the script creates a new PDF file with an incremented version number in the filename.

## Example

Suppose you have a PDF file named `example.pdf` with a ReportLab watermark. To remove the watermark, run the following command:

```
python script_name.py example.pdf
```

The script will check if the watermark is present, remove it, and generate a new file named `example_undrm.pdf` (or `example_undrm (1).pdf` if a file with the same name already exists).

## Note

- This script relies on Python's argparse module to handle command-line arguments. Ensure you have the necessary permissions to read and write files in the specified directory.

- Always make a backup of your original file before running any script that modifies it.
