import os
import shutil
from sys import argv

dir = argv[1]


def recursive_explore(root, dir, lista):
    """
    Recorrido preorder a un directorio con carpetas y archivos dentro de este, guarda
    todo en otra carpeta.
    """
    os.chdir(dir)
    files = os.listdir()

    for file in files:
        if os.path.isdir(file):
            recursive_explore(root, file, lista)
            os.chdir("..")
        elif os.path.isfile(file):
            full_path = f"{os.getcwd()}/{file}"
            lista.append(full_path)


if __name__ == "__main__":
    recorrido = []
    recursive_explore(dir, dir, recorrido)

    for archivo in recorrido:
        shutil.move(archivo, dir)
        print(f"{archivo}->{dir}")
