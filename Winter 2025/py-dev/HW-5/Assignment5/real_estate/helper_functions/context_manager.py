# context_manager.py
import os
from contextlib import contextmanager

@contextmanager
def custom_open(file_name, mode, destination):
    """
    Changes the directory to 'destination', opens 'file_name' with the specified 'mode',
    then returns to the original directory after completion.

    Args:
        file_name (str): Name of the file to open.
        mode (str): File open mode.
        destination (str): Path to the directory where file is located.

    Yields:
        file: A file object opened in given mode. When context exits,
              the file closes and the original working directory is restored.

    """
    original_dir = os.getcwd()
    os.chdir(destination)
    print("Loading data")
    try:
        f = open(file_name, mode)
        yield f
    finally:
        f.close()
        os.chdir(original_dir)
        print("Data loaded")

if __name__ == "__main__":
    test_destination = "."
    with custom_open("test.txt", "w", test_destination) as f:
        f.write("Testing context manager.")
