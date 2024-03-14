

from data_readers.file_reader import FileReader
from data_writers.file_writer import FileWriter


if __name__ == "__main__":
    FileWriter("file").write("Hello world")
    print(FileReader("file").read())