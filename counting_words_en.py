import os, glob

path= 'data/test_texts_en20.txt'
total = 0
for filename in glob.glob(os.path.join(path, '*.txt')):
#    total = 0
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        x = f.read()
       
        lines = x.split()
        for x in lines:
           total+=1
print(total)

def count_words(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        word_count = len(contents.split())
        return word_count

file_path = 'train_texts_en20.txt'  

try:
    words = count_words(file_path)
    print(f"The file contains {words} words.")
except FileNotFoundError:
    print("File not found.")

def count_words(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        word_count = len(contents.split())
        return word_count

file_path = 'test_texts_en20.txt'  
try:
    words = count_words(file_path)
    print(f"The file contains {words} words.")
except FileNotFoundError:
    print("File not found.")

def count_words(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        word_count = len(contents.split())
        return word_count

file_path = 'valid_texts_en20.txt' 

try:
    words = count_words(file_path)
    print(f"The file contains {words} words.")
except FileNotFoundError:
    print("File not found.")

