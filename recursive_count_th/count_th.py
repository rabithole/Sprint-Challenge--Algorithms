'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # Stop when the string has one or less letters. 
    if len(word) <= 1:
        return 0

    # Counting matches
    count = 0

    # Looking for th in the string
    str = 'th'

    # Grab the first two letters
    char = word[0:2]

    # Check for a match between 
    if str == char:
        # Update if a match is found
        count += 1
    # Remove a character to check the next characters for th
    word = word[1:]

    return count + count_th(word)

print(count_th('thunkadunkthumk'))
