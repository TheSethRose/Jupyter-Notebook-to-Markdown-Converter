import os
import shutil
import nbformat
from nbconvert import MarkdownExporter

def convert_notebook_to_markdown(notebook_path):
    """
    Converts a Jupyter Notebook to Markdown format.
    
    Parameters:
    - notebook_path (str): The path to the Jupyter Notebook file.
    """
    try:
        # Read the Jupyter Notebook file
        with open(notebook_path, 'r', encoding='utf-8') as file:
            notebook = nbformat.read(file, as_version=4)

        # Create a Markdown exporter
        exporter = MarkdownExporter()

        # Convert the notebook to Markdown
        (body, resources) = exporter.from_notebook_node(notebook)

        # Save the Markdown file with the same name in the same directory
        markdown_path = os.path.splitext(notebook_path)[0] + '.md'
        with open(markdown_path, 'w', encoding='utf-8') as file:
            file.write(body)

        print(f"Converted {notebook_path} to {markdown_path}")
    except Exception as e:
        print(f"Error converting {notebook_path}: {str(e)}")

def process_directory(directory):
    """
    Converts all Jupyter Notebooks within a directory (and its subdirectories) to Markdown.
    
    Parameters:
    - directory (str): The root directory to search for Jupyter Notebooks.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory not found: {directory}")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.ipynb'):
                notebook_path = os.path.join(root, file)
                convert_notebook_to_markdown(notebook_path)

def prompt_confirmation(item_type):
    """
    Prompts the user for confirmation before proceeding to delete files or directories.
    
    Parameters:
    - item_type (str): The type of items to be deleted (e.g., "files", "directories").
    
    Returns:
    - (bool): True if the user confirms, False otherwise.
    """
    confirmation = input(f"Are you sure you wish to delete all {item_type}? (Y/N) ").strip().lower()
    return confirmation == 'y'

def delete_items(directory, item_type, file_extension=None, exclude_file=None):
    """
    Deletes files or directories within a specified directory based on the provided criteria.
    
    Parameters:
    - directory (str): The directory to search for items to delete.
    - item_type (str): The type of items to delete ("files" or "directories").
    - file_extension (str, optional): The file extension of files to be deleted. Required when deleting files.
    - exclude_file (str, optional): The filename to exclude from deletion. Only applicable when deleting files.
    """
    if prompt_confirmation(item_type):
        for root, dirs, files in os.walk(directory, topdown=False):
            if item_type == "files":
                for file in files:
                    if file.endswith(file_extension) and (exclude_file is None or file != exclude_file):
                        path = os.path.join(root, file)
                        try:
                            os.remove(path)
                            print(f"Deleted {path}")
                        except Exception as e:
                            print(f"Error deleting {path}: {str(e)}")
            elif item_type == "directories":
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    try:
                        shutil.rmtree(dir_path)
                        print(f"Deleted directory: {dir_path}")
                    except Exception as e:
                        print(f"Error deleting directory {dir_path}: {str(e)}")

def combine_markdown_files(directory, combined_filename):
    """
    Combines all Markdown files within a directory into a single file.
    
    Parameters:
    - directory (str): The directory to search for Markdown files.
    - combined_filename (str): The filename for the combined Markdown content.
    """
    combined_file_path = os.path.join(directory, combined_filename)
    try:
        with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if file.endswith('.md') and file != combined_filename:
                        file_path = os.path.join(root, file)
                        
                        with open(file_path, 'r', encoding='utf-8') as md_file:
                            content = md_file.read()
                        
                        # Write the transformed filename as a header
                        combined_file.write(f"# {file[:-3].replace('_', ' ').title()}\n\n")
                        combined_file.write(content)
                        combined_file.write("\n\n---\n\n")

        print(f"Combined Markdown file created: {combined_file_path}")
    except Exception as e:
        print(f"Error creating combined Markdown file: {str(e)}")

# Placeholder for starting directory
starting_directory = '<YOUR_DIRECTORY_PATH>'

# Placeholder for the combined Markdown filename
combined_filename = 'your_combined_filename.md'

try:
    # Convert Jupyter notebooks to Markdown
    process_directory(starting_directory)

    # Delete Jupyter notebook files with confirmation
    delete_items(starting_directory, "files", '.ipynb', combined_filename)

    # Combine Markdown files into a single file
    combine_markdown_files(starting_directory, combined_filename)

    # Delete Markdown files (except the combined file) with confirmation
    delete_items(starting_directory, "files", '.md', combined_filename)

    # Delete all directories and subdirectories with confirmation
    delete_items(starting_directory, "directories")
except FileNotFoundError as e:
    print(str(e))
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")