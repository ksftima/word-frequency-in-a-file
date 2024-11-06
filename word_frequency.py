import re
from collections import Counter

def count_word_frequency(filename):
    """
    Reads a text file and counts the frequency of each word in the file.

    Args:
        - filename: The path to the text file to be analyzed.

    Prints:
        - A sorted list of words with their frequencies in descending order.

    Handles:
        - FileNotFoundError: If the file is not found.
        - UnicodeDecodeError: If the file cannot be decoded as UTF-8.
        - General exceptions for any unexpected errors.
    """
    try:
        # Open the file and read the content in lowercase
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read().lower()
        
        # Remove the punctuations and split into words
        words = re.findall(r'\b\w+\b', text)  # This regex matches whole words
        
        # Use Counter to count word frequencies
        word_count = Counter(words)
        
        # Display sorted word frequencies
        print("Word frequency (sorted):")
        for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except UnicodeDecodeError:
        print(f"Could not decode the file '{filename}'. Ensure it's a text file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the filename
filename = input('Enter the filename: ')
count_word_frequency(filename)
