"""
Script: outofbounds_2.0.py
Description: Tool for outofbounds 2.0
Category: Computer_Vision_Datasets
"""
import json
import os

dir_path = r"C:\Users\henry\Desktop\Dataset\yolo labels"


def read_yolo_file(path):
    with open(path, "r") as f:
        return f.readlines()


def write_new_output(data, filename):
    if not os.path.exists(f"{dir_path}/trimmed"):
        os.mkdir(f"{dir_path}/trimmed")

    with open(f"{dir_path}/trimmed/{filename}", "w") as f:
        f.writelines(data)


def trim(data):
    new = []
    for labels in data:
        sep = labels.split(" ")

        for index,items in enumerate(sep):
            if index != 0:
                if float(items) > 1:
                    sep[index] = '1'
                elif float(items) < 0:
                    sep[index] = '0'

        print(sep)
        mod = " ".join(sep)

        new.append(mod)
    return new


def main():
    for files in os.listdir(dir_path):
        content = read_yolo_file(f"{dir_path}\{files}")
        print(content)

        output = trim(content)

        print(output)

        write_new_output(output, files)


main()