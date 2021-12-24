# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a_NN import get_permutations


# ### HELPER CODE ### #
def load_words(file_name):
    """
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    """
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


# ### END HELPER CODE ### #

WORDLIST_FILENAME = 'words.txt'
WORDLIST = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


class SubMessage(object):
    def __init__(self, text):
        """
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        """
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        """
        return self.message_text

    def get_valid_words(self):
        """
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        """
        return self.valid_words[:]

    def build_transpose_dict(self, vowels_permutation):
        """
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        """
        # assure the input is a 5 letter string?

        # all lowercase and uppercase values
        vowels_permutation_lower = vowels_permutation.lower()
        vowels_permutation_upper = vowels_permutation.upper()

        transpose_dict = {}

        # access values through index
        for index in range(len(VOWELS_LOWER)):
            transpose_dict[VOWELS_LOWER[index]] = vowels_permutation_lower[index]
            transpose_dict[VOWELS_UPPER[index]] = vowels_permutation_upper[index]

        # access values directly
        for letter in CONSONANTS_LOWER + CONSONANTS_UPPER:
            transpose_dict[letter] = letter

        return transpose_dict

    def apply_transpose(self, transpose_dict):
        """
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        """

        to_transpose = self.get_message_text()
        transposed_text = ''

        for letter in to_transpose:
            if letter in transpose_dict.keys():
                transposed_text += transpose_dict[letter]
            else:
                transposed_text += letter

        return transposed_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        """
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        """
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        """
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use your function from Part 4A
        """

        permutations_list = get_permutations(VOWELS_LOWER)
        vowel_permutation = VOWELS_LOWER
        max_score = 0

        for entry in permutations_list:

            transpose_dict = self.build_transpose_dict(entry)
            transposed_text = self.apply_transpose(transpose_dict)

            # separate words
            split_text = transposed_text.split()

            score = 0
            for word in split_text:
                if is_word(WORDLIST, word):
                    score += 1

            if score > max_score:
                max_score = score
                vowel_permutation = entry

        return self.apply_transpose(self.build_transpose_dict(vowel_permutation))


if __name__ == '__main__':
    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE

    # Test 1

    text1 = "If you can't explain it simply, you don't understand it enough."
    case1 = SubMessage(text1)
    permutation1 = "uiaeo"
    dict1 = case1.build_transpose_dict(permutation1)

    print("Original message:", case1.get_message_text())
    print("Permutation:", permutation1)
    print("Expected encryption:", "Af yeo cun't ixpluan at samply, yeo den't ondirstund at ineogh.")
    print("Actual encryption:", case1.apply_transpose(dict1))

    # Test 2

    text2 = "I have not failed. I’ve just found 10,000 ways that won’t work."
    case2 = SubMessage(text2)
    permutation2 = "iioii"
    dict2 = case2.build_transpose_dict(permutation2)

    print("Original message:", case2.get_message_text())
    print("Permutation:", permutation2)

    print("Expected encryption:", "O hivi nit fiolid. O’vi jist fiind 10,000 wiys thit win’t wirk.")
    print("Actual encryption:", case2.apply_transpose(dict2))