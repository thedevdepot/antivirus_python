# tutorial from https://www.youtube.com/watch?v=Q2tIh4rwovY

import os

def scan_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

if __name__ == "__main__":
    specified_folder = r"./"
    scan_files(specified_folder)
