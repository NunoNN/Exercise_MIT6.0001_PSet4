# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
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
    '''

    assert len(sequence) != 0
    if type(sequence) is str:
        sequence = list(sequence)

    # base case -> string of length 1 --> returns itself
    if len(sequence) == 1:
        # permutations = sequence
        return sequence
    else:
        first_letter = sequence[0]
        sequence = get_permutations(sequence[1:])
        # recursion removes letters from the beginning of the string until sequence is length 1
        # operations after recursion
        temp = sequence[:]
        for n in range(len(temp)):
            for j in range(len(temp[n]) + 1):
                string = temp[n][0:j] + first_letter + temp[n][j:]
                sequence.append(string)
        for i in temp:
            sequence.remove(i)
        return sequence

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

