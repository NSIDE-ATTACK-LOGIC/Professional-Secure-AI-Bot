import os

from langchain.agents import tool
from werkzeug.utils import safe_join


@tool
def get_filenames_in_directory() -> list:
    """
    Retrieves a list of filenames in the files directory.
    :return: A list of filenames found in the directory.
    """
    file_path = "./textfiles"
    try:
        entries = os.listdir(file_path)
        return entries
    except Exception as e:
        return f"An error occurred: {str(e)}"


@tool
def get_file_content(filename: str) -> str:
    """
    Retrieves the content of a text file given its filename.

    :param filename: The name of the file to read.
    :return: The content of the file as a string, or None if the file cannot be read.
    """
    FILE_DIR = "./textfiles"

    filepath = safe_join(FILE_DIR, filename)

    if not os.path.exists(filepath):
        return "File does not exist."

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except (
        Exception
    ) as e:  # Catch any exception, e.g., permission issues, and handle it
        return f"An error occurred while reading the file: {str(e)}"
