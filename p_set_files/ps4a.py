# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence, save={}):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # >>> get_permutations('abc')
    # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    # FIRST APPROACH:

    # recursively remove letters from the sequence until len == 1
    # base case --> permutation on a single letter = [itself]
    # insert the first letter of the previous sequence in all the possible positions
    # ex.: 'abcd'
    # base case = d --> # insert c in possible positions : [.d.]
    # yields [cd, dc] --> continue with b in : [.c.d.] and in [.d.c.]
    # repeat for all the letters to get the full set of permutations

    # code:
    # assert len(sequence) != 0
    # if type(sequence) is str:
    #     sequence = list(sequence)
    # if len(sequence) == 1:
    #     return sequence
    # first_letter = sequence[0]
    # sequence = get_permutations(sequence[1:])
    # temp = sequence[:]
    # for n in range(len(temp)):
    #     for j in range(len(temp[n]) + 1):
    #         string = temp[n][0:j] + first_letter + temp[n][j:]
    #         sequence.append(string)
    # for i in temp:
    #     sequence.remove(i)
    # return sequence

    # SECOND APPROACH:

    # fix the first letter
    # get the permutations of the remaining letters and add them to the fixed letter
    # recursion allows to reduce the complexity by fixing letters inside the remaining letters set
    # base case --> len <= 1 sequence = [itself]

    # initiate variables
    permutations = []

    # base case
    if len(sequence) <= 1:
        return [sequence], save

    # for each letter get the remaining letters
    for index in range(len(sequence)):
        remaining_letters = sequence[0:index] + sequence[index+1:]

        # dictionary save to avoid multiple calls to the same recursion values
        if remaining_letters in save:
            z = save[remaining_letters]
        else:
            # recursion applied to the remaining letters --> reduces length at each function call
            # add each permutation to the fixed letter
            z = get_permutations(remaining_letters, save)
            save[remaining_letters] = z[0]

        for n in z[0]:
            word = sequence[index] + n
            if word not in permutations:
                permutations.append(word)
    return permutations, save

    # !!! reduce number of recursions?
    # assure there are no duplicate entries in the final list


if __name__ == '__main__':
    #    #EXAMPLE
    #    example_input = 'abc'
    #    print('Input:', example_input)
    #    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    #    print('Actual Output:', get_permutations(example_input))

    #    # Put three example test cases here (for your sanity, limit your inputs
    #    to be three characters or fewer as you will have n! permutations for a
    #    sequence of length n)

    pass  # delete this line and replace with your code here
