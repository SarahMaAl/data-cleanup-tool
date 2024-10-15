"""
file_counter.py

Author: Sarah MARTIN-ALONSO
License: MIT License
Date: 2024-10-15

Description:
This script counts the total number of files (including duplicates) 
with specific extensions in a given directory and its subdirectories.

Supported file extensions:
- .pdf, .ppt, .pptx, .doc, .docx, .csv, .xls, .xlsx

Usage:
Update the `start_directory` variable with the appropriate path before running the script.
"""

import os

def count_files_with_extensions(start_directory):
    """Count the total number of files with specific extensions in the directory.

    Args:
        start_directory (str): The starting directory to search for files.

    Returns:
        int: The total number of files with the specified extensions.
    """
    # Allowed file extensions
    allowed_extensions = {'.pdf', '.ppt', '.pptx', '.doc', '.docx', '.csv', '.xls', '.xlsx'}
    file_count = 0

    # Walk through all files and subdirectories
    for dirpath, _, filenames in os.walk(start_directory):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in allowed_extensions:
                file_count += 1

    return file_count

# Example usage
if __name__ == "__main__":
    start_directory = r'C:\path\to\your\start_directory'  # Change this to your start directory
    total_files = count_files_with_extensions(start_directory)
    print(f"Total number of files with the specified extensions: {total_files}")
