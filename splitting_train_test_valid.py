import random

def filter_and_split_data(greek_file, english_file, greek_train, greek_valid, greek_test, english_train, english_valid, english_test, token_max=27, train_ratio=0.8, valid_ratio=0.1, test_ratio=0.1):
    # Store filtered sentence pairs in memory before splitting
    filtered_sentences = []

    # Read both files
    with open(greek_file, 'r', encoding='utf-8') as g_file, open(english_file, 'r', encoding='utf-8') as e_file:
        for greek_sentence, english_sentence in zip(g_file, e_file):
            # Tokenize the Greek sentence
            greek_tokens = greek_sentence.strip().split()
            greek_token_count = len(greek_tokens)

            # If Greek sentence has <= 27 tokens, store the sentence pair
            if greek_token_count <= token_max:
                filtered_sentences.append((greek_sentence.strip(), english_sentence.strip()))

    # Shuffle the filtered sentences for randomness
    random.shuffle(filtered_sentences)

    # Calculate the split sizes
    total_sentences = len(filtered_sentences)
    train_size = int(total_sentences * train_ratio)
    valid_size = int(total_sentences * valid_ratio)

    # Split the data
    train_sentences = filtered_sentences[:train_size]
    valid_sentences = filtered_sentences[train_size:train_size + valid_size]
    test_sentences = filtered_sentences[train_size + valid_size:]

    # Helper function to write the sentences into files
    def write_to_files(sentences, greek_output_file, english_output_file):
        with open(greek_output_file, 'w', encoding='utf-8') as greek_out, open(english_output_file, 'w', encoding='utf-8') as english_out:
            for greek_sentence, english_sentence in sentences:
                greek_out.write(greek_sentence + '\n')
                english_out.write(english_sentence + '\n')

    # Write train, valid, and test sets to their respective files
    write_to_files(train_sentences, greek_train, english_train)
    write_to_files(valid_sentences, greek_valid, english_valid)
    write_to_files(test_sentences, greek_test, english_test)


# Define your file paths
greek_file = 'texts_grc.txt'
english_file = 'texts_en.txt'

# Output file paths for train, valid, and test sets
greek_train = 'train_texts_grc.txt'
greek_valid = 'valid_texts_grc.txt'
greek_test = 'test_texts_grc.txt'

english_train = 'train_texts_en.txt'
english_valid = 'valid_texts_en.txt'
english_test = 'test_texts_eng.txt'

# Call the function to filter, split, and write the data
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

# Output: Train, valid, and test sets will be written to respective files for Greek and English