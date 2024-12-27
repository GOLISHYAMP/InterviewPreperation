from multiprocessing import Pool
from nltk.tokenize import word_tokenize

def tokenize_file(file_path):
    with open(file_path, 'r') as f:
        return word_tokenize(f.read())

if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "file3.txt"]
    with Pool(processes=3) as pool:
        tokenized = pool.map(tokenize_file, files)
    print(tokenized)
