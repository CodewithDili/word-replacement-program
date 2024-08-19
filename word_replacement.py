def replace_word(text, old_word, new_word):
    """
    Replaces all occurrences of old_word with new_word in the given text.
    
    Parameters:
    text (str): The input string where the replacement will occur.
    old_word (str): The word to be replaced.
    new_word (str): The word to replace with.

    Returns:
    str: The modified string with replaced words.
    """
    # Replace the old word with the new word in the text
    modified_text = text.replace(old_word, new_word)
    return modified_text

# Example usage
if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    old_word = "fox"
    new_word = "cat"
    
    result = replace_word(text, old_word, new_word)
    print("Original text:", text)
    print("Modified text:", result)
