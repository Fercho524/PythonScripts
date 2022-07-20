import os
import shutil
from sys import argv
import pandas as pd
from termcolor import cprint

dir = argv[1]


def group_files_by_size(dir):
    """
    Agrupa los archivos de un directorio por su tamaño en Megabytes
    """

    # Getting the files inside
    if os.path.isdir(dir):
        os.chdir(dir)

    files = os.listdir(dir)
    filenames = []
    filesizes = []

    for file in files:
        if os.path.isfile(file):
            filenames.append(file)
            filesizes.append(os.path.getsize(file)/1000000)

    # Creating a Dataset to use Groupby
    dic = {
        "name": filenames,
        "size": filesizes
    }

    df = pd.DataFrame(dic)
    df["class"] = round(df["size"], 1)
    class_names = df["class"].unique()

    # Grouping  files by Size in MB
    for clase in class_names:
        if not os.path.isdir(str(clase)):
            os.mkdir(str(clase))

        cprint(f"Class {str(clase)} Directory created", "green")
        classfiles = df[df["class"] == clase]

        for name in classfiles.loc[:, "name"]:
            shutil.move(name, os.path.join(str(clase), name))
            print(f"Moving : {name} -> {str(clase)}/{name} ")


group_files_by_size(dir)
