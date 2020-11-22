# oh soldier prettify my folder
# define a function which takes path, file and file with extension like jpg
# Capitalize the folder names at given directory, whose names is not present in the file
# Don't change file and format file, just rename format file from 1 to n files.

import os


def soldier(path, file, format):
    # change directories
    os.chdir(path)
    i = 1
    # make a list of files in that directory
    files = os.listdir(path)
    with open(file) as f:
        file_list = f.read().split("\n")

    for file1 in files:
        if file1 not in file_list:
            os.renames(file1, file1.capitalize())

        # os.path.splitext - split the file name and extension and make tuple.
        if os.path.splitext(file1)[1] == format:
            os.renames(file1, f"{i}{format}")
            i += 1


soldier(r"D:\documnets", r"C:\Users\kasar\PycharmProjects\python\Harry.txt", ".jpg")
