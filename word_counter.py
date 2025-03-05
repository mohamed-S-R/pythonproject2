def count_words(text):
    """
    Function to count the number of words in a given text.
    :param text: str - Input sentence or paragraph
    :return: int - Word count
    """
    if not text.strip():  # Handling empty input
        return 0
    return len(text.split())

# Test cases
if __name__ == "__main__":
    test_sentences = [
        "Hello world!",  # Expected output: 2
        "This is a sample sentence.",  # Expected output: 5
        "  ",  # Expected output: 0 (empty input)
        "Python programming is fun and powerful.",  # Expected output: 6
        "Word Counter Project"  # Expected output: 3
    ]
    
    for i, sentence in enumerate(test_sentences, 1):
        word_count = count_words(sentence)
        print(f"Test {i}: '{sentence}' -> Word count: {word_count}")