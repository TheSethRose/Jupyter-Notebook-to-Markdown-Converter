# Jupyter Notebook to Markdown Converter

This Python script allows you to convert Jupyter Notebook files (.ipynb) to Markdown format (.md) and combine all the converted Markdown files into a single file. It also provides options to delete the original Jupyter Notebook files, individual Markdown files, and subdirectories.

## Features

- Converts Jupyter Notebook files to Markdown format
- Combines all converted Markdown files into a single file
- Deletes original Jupyter Notebook files with confirmation
- Deletes individual Markdown files (except the combined file) with confirmation
- Deletes all subdirectories with confirmation

## Prerequisites

- Python 3.x
- `nbformat` library
- `nbconvert` library

You can install the required libraries using pip:

```bash
pip install nbformat nbconvert
```

## Usage

1. Clone the repository or download the script file.

2. Open the script file and replace the following placeholders with your desired values:
   - `<YOUR_DIRECTORY_PATH>`: Replace with the path to the directory containing your Jupyter Notebook files.
   - `your_combined_filename.md`: Replace with your desired filename for the combined Markdown file.

3. Run the script using the following command:
```
python convert.py
```

4. The script will perform the following actions:
- Convert all Jupyter Notebook files within the specified directory (and its subdirectories) to Markdown format.
- Prompt for confirmation to delete the original Jupyter Notebook files.
- Combine all converted Markdown files into a single file with the specified filename.
- Prompt for confirmation to delete the individual Markdown files (except the combined file).
- Prompt for confirmation to delete all subdirectories within the specified directory.

5. After the script finishes executing, you will find the combined Markdown file in the specified directory.

## Notes

- The script handles errors gracefully and provides informative error messages.
- The script prompts for confirmation before deleting files or directories to prevent accidental deletion.
- The combined Markdown file will have a transformed filename as a header for each section, followed by the content of the corresponding Markdown file.
- The script uses the `os` and `shutil` modules for file and directory operations, and the `nbformat` and `nbconvert` libraries for converting Jupyter Notebooks to Markdown.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements

- The script utilizes the `nbformat` and `nbconvert` libraries for converting Jupyter Notebooks to Markdown.
- Special thanks to the contributors of the libraries used in this project.
