import os
from sys import argv

dir = argv[1]
extension = argv[2]


def change_extension(dir, extension):
    """
    Cambia la extension de todos los archivos de un directorio
    """
    files = os.listdir(dir)
    os.chdir(dir)

    for file in files:
        new_name = f'{file.split(".")[0]}.{extension}'
        print(f'{file} -> {new_name}')
        os.rename(file, new_name)


if __name__ == "__main__":
    change_extension(dir, extension)
