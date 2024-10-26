"""
3D Printing Project Setup Script
Author: Sarah MARTIN-ALONSO
Date: 2024-10-26
License: MIT License

This script creates a new 3D printing project with a specified folder structure
and generates a README.md file with a basic template. The main project folder 
will be placed under the '3D_Printing/Projects' directory.
"""

import os


def create_3d_printing_project(base_dir, project_name):
    """
    Creates a new 3D printing project with the required subfolders.

    Parameters:
        base_dir (str): The base directory where the '3D_Printing' folder is located.
        project_name (str): The name of the new project.

    The function will create a main directory for the project, several
    subdirectories, and a README.md file with a template.
    """
    # Define the main 3D Printing directory path
    main_dir = os.path.join(base_dir, '3D_Printing', 'Projects', project_name)

    # Define subdirectories to be created for the project
    subdirectories = [
        'Designs',     # Folder for CAD files, STL files, etc.
        'Output',      # Folder for G-code files, final 3D print files
        'Results',     # Folder for photos, test results
    ]

    try:
        # Create the main project directory
        os.makedirs(main_dir, exist_ok=True)
        print(f"Project directory '{main_dir}' created successfully.")

        # Create each subdirectory
        for sub_dir in subdirectories:
            sub_dir_path = os.path.join(main_dir, sub_dir)
            os.makedirs(sub_dir_path, exist_ok=True)
            print(f"Subdirectory '{sub_dir}' created at '{sub_dir_path}'.")

        # Create a README.md file in the main project directory
        readme_path = os.path.join(main_dir, 'README.md')
        with open(readme_path, 'w', encoding='utf-8') as readme_file:
            readme_file.write(f"# {project_name}\n\n")
            readme_file.write("## Project Overview\n")
            readme_file.write("Provide a brief description of the project, its purpose, and the main objectives.\n\n")
            readme_file.write("## Folder Structure\n")
            readme_file.write("- **Designs/**: Contains CAD files, STL models, etc.\n")
            readme_file.write("- **Output/**: Includes G-code files and other final files for 3D printing.\n")
            readme_file.write("- **Results/**: Holds photos of the printed object, test results, and documentation.\n\n")
            readme_file.write("## Usage Instructions\n")
            readme_file.write("Provide instructions on how to use the files in this project, such as print settings or post-processing steps.\n\n")
            readme_file.write("## License\n")
            readme_file.write("Include any license information if applicable.\n")
        print(f"README.md created at '{readme_path}'.")

    except OSError as error:
        print(f"An error occurred while creating the project: {error}")


if __name__ == '__main__':
    # Example usage
    BASE_DIRECTORY = '/path/to/Documents'  # Change this to your actual base directory path
    NEW_PROJECT_NAME = 'Sample_Project'    # Replace with your project name

    create_3d_printing_project(BASE_DIRECTORY, NEW_PROJECT_NAME)
