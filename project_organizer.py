import os

def create_file_system(root_dir, project_type):
    """
    Function to create a file management system with nested folders and generic files.
    """

    # Check if the root directory already exists
    if os.path.exists(root_dir):
        print("Error: Directory already exists. Please choose a different location.")
        return

    # Create the root directory
    os.makedirs(root_dir)

    # Create subfolders based on project type
    if project_type == "Finance":
        subfolders = ['Documents', 'Admin', 'Finance']
    elif project_type == "Coding":
        subfolders = ['Testing', 'Code Reviews', 'Scripts']
    else:
        # print("Error: Invalid project type.")
        return

    for folder in subfolders:
        folder_path = os.path.join(root_dir, folder)
        os.makedirs(folder_path)

        # Create generic files within each subfolder
        create_files(folder_path)

    # Create a user manual file
    create_user_manual(root_dir, project_type)

def create_files(folder_path):
    """
    Function to create generic files within a folder.
    """
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, 'w') as f:
            f.write("This is a generic file created for the file management system.")

def create_user_manual(root_dir, project_type):
    """
    Function to create a user manual explaining the file management system.
    """
    user_manual = f"""
    File Management System User Manual for {project_type.capitalize()} Projects:

    This file management system is organized into the following structure:

    {', '.join([folder for folder in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, folder))])}

    Each folder may contain generic files named file1.txt, file2.txt, and file3.txt.

    """
    manual_path = os.path.join(root_dir, f'{project_type.capitalize()}_User_Manual.txt')
    with open(manual_path, 'w') as f:
        f.write(user_manual)

if __name__ == "__main__":
    root_directory = input("Enter the root directory for the file management system: ")
    project_type = input("Enter the type of project (finance or coding): ").lower()

    create_file_system(root_directory, project_type)
    print("File management system created successfully!")
