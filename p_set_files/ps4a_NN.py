# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence, saved_permutations=None):
    """
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """

    # FIRST APPROACH:
    # recursively remove letters from the sequence until len == 1
    # base case --> permutation on a single letter = [itself]
    # insert the first letter of the previous sequence in all the possible positions
    # ex.: "abcd"
    # base case = d --> # insert c in possible positions : [.d.]
    # yields [cd, dc] --> continue with b in : [.c.d.] and in [.d.c.]
    # repeat for all the letters to get the full set of permutations

    # SECOND APPROACH:

    # fix the first letter
    # get the permutations of the remaining letters and add them to the fixed letter
    # recursion allows to reduce the complexity by fixing letters inside the remaining letters set
    # base case --> len <= 1 sequence = [itself]

    # default argument None to have immutable arguments
    if saved_permutations is None:
        saved_permutations = {}

    # create variable
    permutations = []

    # base case
    if len(sequence) <= 1:
        return [sequence], saved_permutations

    # for each letter get the remaining letters
    for index in range(len(sequence)):
        remaining_letters = sequence[0:index] + sequence[index+1:]

        # dictionary save to avoid multiple calls to the same recursion values
        if remaining_letters in saved_permutations:
            recursion_values = saved_permutations[remaining_letters]
        else:
            # recursion applied to the remaining letters --> reduces length at each function call
            recursion_values, saved_permutations = get_permutations(remaining_letters, saved_permutations)
            saved_permutations[remaining_letters] = recursion_values

        # add each permutation to the fixed letter
        for entry in recursion_values:
            word = sequence[index] + entry

            # assure word are not repeated in the output
            if word not in permutations:
                permutations.append(word)

    return permutations, saved_permutations


if __name__ == '__main__':
    # # EXAMPLE
    # example_input = 'abc'
    # print('Input:', example_input)
    # print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input)[0])
    # # Put three example test cases here (for your sanity, limit your inputs
    # # to be three characters or fewer as you will have n! permutations for a
    # # sequence of length n)

    # Tests: (following the examples above)
    # It is assumed that sequence is a non-empty string and the function returns a list.

    test_sets = ['abc', 'xxyy', 'ide', 'ooooo']
    test_results = []
    expected_output = [['abc', 'acb', 'bac', 'bca', 'cab', 'cba'],
                       ['xxyy', 'xyxy', 'xyyx', 'yxxy', 'yxyx', 'yyxx'],
                       ['ide', 'ied', 'die', 'dei', 'eid', 'edi'],
                       ['ooooo']]
    for n in range(len(test_sets)):
        print('Input:', test_sets[n])
        print('Expected Output:', expected_output[n])
        result = get_permutations(test_sets[n])[0]
        print('Actual Output:', result)
        test_results.append(result)

    for i in range(len(test_results)):
        assert expected_output[i] == test_results[i], 'Should be equal'
