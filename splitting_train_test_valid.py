import random

def filter_and_split_data(greek_file, english_file, greek_train, greek_valid, greek_test, english_train, english_valid, english_test, token_max=27, train_ratio=0.8, valid_ratio=0.1, test_ratio=0.1):
    
    filtered_sentences = []
    with open(greek_file, 'r', encoding='utf-8') as g_file, open(english_file, 'r', encoding='utf-8') as e_file:
        for greek_sentence, english_sentence in zip(g_file, e_file):
            greek_tokens = greek_sentence.strip().split()
            greek_token_count = len(greek_tokens)
            if greek_token_count <= token_max:
                filtered_sentences.append((greek_sentence.strip(), english_sentence.strip()))

    random.shuffle(filtered_sentences)
    total_sentences = len(filtered_sentences)
    train_size = int(total_sentences * train_ratio)
    valid_size = int(total_sentences * valid_ratio)

    # Split the data
    train_sentences = filtered_sentences[:train_size]
    valid_sentences = filtered_sentences[train_size:train_size + valid_size]
    test_sentences = filtered_sentences[train_size + valid_size:]

    def write_to_files(sentences, greek_output_file, english_output_file):
        with open(greek_output_file, 'w', encoding='utf-8') as greek_out, open(english_output_file, 'w', encoding='utf-8') as english_out:
            for greek_sentence, english_sentence in sentences:
                greek_out.write(greek_sentence + '\n')
                english_out.write(english_sentence + '\n')

    write_to_files(train_sentences, greek_train, english_train)
    write_to_files(valid_sentences, greek_valid, english_valid)
    write_to_files(test_sentences, greek_test, english_test)


greek_file = 'texts_grc.txt'
english_file = 'texts_en.txt'

# Output file paths for train, valid, and test sets
greek_train = 'train_texts_grc.txt'
greek_valid = 'valid_texts_grc.txt'
greek_test = 'test_texts_grc.txt'

english_train = 'train_texts_en.txt'
english_valid = 'valid_texts_en.txt'
english_test = 'test_texts_eng.txt'

filter_and_split_data(
    greek_file, 
    english_file, 
    greek_train, 
    greek_valid, 
    greek_test, 
    english_train, 
    english_valid, 
    english_test
)