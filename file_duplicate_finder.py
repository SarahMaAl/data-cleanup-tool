"""
file_duplicate_finder.py

Author: Sarah MARTIN-ALONSO
License: MIT License
Date : 2024-10-15

Description:
This script searches for duplicate files in a specified directory and its subdirectories
based on file size, type, and content. Unique files are copied to an output directory,
while duplicates are logged in a text file.

Usage:
Update the `start_directory` and `output_directory` variables with appropriate paths
before running the script.
"""

import os
import hashlib
import shutil


def calculate_file_hash(file_path):
    """Calculate the SHA256 hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The SHA256 hash of the file's contents.
    """
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def find_duplicates_and_organize_files(start_directory, output_directory):
    """Find duplicate files and organize unique files in the output directory.

    Args:
        start_directory (str): The starting directory to search for files.
        output_directory (str): The directory to store unique files.
    """
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    seen_files = {}  # Dictionary to hold file hashes and paths
    duplicate_log = []  # List to hold information about duplicates

    # Allowed file extensions
    allowed_extensions = {'.pdf', '.ppt', '.pptx', '.doc', '.docx', '.csv', '.xls', '.xlsx'}

    for dirpath, _, filenames in os.walk(start_directory):
        for filename in filenames:
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in allowed_extensions:
                file_path = os.path.join(dirpath, filename)
                file_size = os.path.getsize(file_path)
                file_hash = calculate_file_hash(file_path)

                # Create a unique key based on size and hash
                key = (file_size, file_hash)

                if key not in seen_files:
                    # If the file is unique, copy it to the output directory
                    output_file_path = os.path.join(output_directory, filename)
                    if not os.path.exists(output_file_path):
                        shutil.copy2(file_path, output_file_path)
                        seen_files[key] = output_file_path  # Store the unique file path
                    else:
                        # If a file with the same name already exists, rename it
                        base, ext = os.path.splitext(filename)
                        counter = 1
                        new_filename = f"{base}_{counter}{ext}"
                        while os.path.exists(os.path.join(output_directory, new_filename)):
                            counter += 1
                            new_filename = f"{base}_{counter}{ext}"
                        shutil.copy2(file_path, os.path.join(output_directory, new_filename))
                        seen_files[key] = os.path.join(output_directory, new_filename)
                else:
                    # If a duplicate is found, log the details
                    original_file_path = seen_files[key]
                    duplicate_log.append((file_path, original_file_path))

    # Write duplicates to a log file
    log_file_path = os.path.join(output_directory, 'duplicates_log.txt')
    with open(log_file_path, 'w') as log_file:
        for duplicate in duplicate_log:
            log_file.write(f"Duplicate: {duplicate[0]} -> Found in Output: {duplicate[1]}\n")

# Example usage
if __name__ == "__main__":
    start_directory = r'C:\path\to\your\start_directory'  # Change this to your start directory
    output_directory = r'C:\path\to\your\output_directory'  # Change this to your output directory
    find_duplicates_and_organize_files(start_directory, output_directory)
