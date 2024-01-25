"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'
    '''

    def __init__(self, file_path):
        """Initialize WordFinder with a file path and read the words from the file."""
        self.words = self.read_words(file_path)

    def read_words(self, file_path):
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file]
        print(f"{len(words)} words read")
        return words
    
    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def read_words(self, file_path):
        """Read words from they specified file, excluding blank lines and comments"""
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        print(f"{len(words)} words read")
        return words
    
