import os
import re

def retrieve_files(ext):
    """
    Retrieve files in the current directory subtree with a particular extension.

    Args:
        ext (str): The file extension (e.g., '.txt').

    Returns:
        list of str: A list of full file paths for files ending with the specified extension.
    """

    matching_files = []
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith(ext):
                matching_files.append(os.path.join(root, f))
    return matching_files

def record_loader_gen(file_list):
    """
    Generator that reads records from files matching the pattern.

    Args:
        file_list (list of str): List of file paths to process.

    Yields:
        tuple: A tuple (name, gender, births, year) for each valid record encountered.
    """

    pattern = re.compile(r'yob(\d{4})\.txt')
    for file_path in file_list:
        match = pattern.search(file_path)
        if not match:
            continue
        year = int(match.group(1))

        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, gender, births_str = line.split(",")
                births = int(births_str)
                yield (name, gender, births, year)