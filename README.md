# File Duplicate Finder

## Author
**Sarah MARTIN-ALONSO**

## License
This project is licensed under the MIT License.

## Description
The **File Duplicate Finder** is a Python script designed to search for duplicate files in a specified directory and its subdirectories. It compares files based on their size, type, and content, allowing users to efficiently manage and organize their files. Unique files are copied to a designated output directory, while any duplicates are logged in a text file for reference.

## Features
- Recursively searches for duplicate files in a specified directory.
- Supports multiple file types, including:
  - PDF (.pdf)
  - PowerPoint (.ppt, .pptx)
  - Word Documents (.doc, .docx)
  - CSV (.csv)
  - Excel (.xls, .xlsx)
- Calculates SHA256 hash values to compare file contents.
- Copies unique files to an output directory, ensuring no duplicates are stored.
- Logs duplicates with their original file paths and the paths of files in the output directory.

## Requirements
- Python 3.x
- Required libraries:
  - `os` (part of the standard library)
  - `hashlib` (part of the standard library)
  - `shutil` (part of the standard library)

## Installation
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/SarahMaAl/data-cleanup-tool]
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd your-repo-name
   ```

3. **Ensure you have Python 3.x installed**. You can check this by running:
   ```bash
   python --version
   ```

## Usage
1. **Update the script**:
   Open `file_duplicate_finder.py` in a text editor and modify the `start_directory` and `output_directory` variables to point to the desired folders:
   ```python
   start_directory = r'C:\path\to\your\start_directory'
   output_directory = r'C:\path\to\your\output_directory'
   ```

2. **Run the script**:
   You can execute the script by running the following command in your terminal or command prompt:
   ```bash
   python file_duplicate_finder.py
   ```

3. **Check the output**:
   - Unique files will be copied to the specified output directory.
   - A log file named `duplicates_log.txt` will be created in the output directory, listing all detected duplicates and their paths.

## Example
For example, if you want to search for duplicates in your Downloads folder and copy unique files to a new folder called "unique_files", you would set:
```python
start_directory = r'C:\Users\YourUsername\Downloads'
output_directory = r'C:\Users\YourUsername\Downloads\unique_files'
```

## Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to fork the repository and submit a pull request.

## Acknowledgments
- This project is inspired by the need for efficient file management and organization in personal and professional environments.

## Contact
For any questions or issues regarding this script, please reach out to me at [sarah.martin.alonso@gmail.com].
