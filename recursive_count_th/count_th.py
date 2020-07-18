'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
counter = 0
def count_th(word):
    # Base case?
    # we reached the last index of word
    global counter
    start = 0
    if len(word) <= 1:
        return counter
    # How to get to base case?
    # similar to sliding window problem, iterate across word, if two indices match 'th', increment counter
    if word[start] == 't':
        if word[start + 1] == 'h':
            counter += 1
            return count_th(word[start+2:])
    else:
        return count_th(word[start+1:])
    # Where to recurse?
    # after compare two indices to 'th' and increment counter if necessary

print(count_th('thTHTHTHTHththththttt'))