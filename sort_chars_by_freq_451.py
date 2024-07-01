from collections import defaultdict


'''
    Sort Characters By Frequency

    Given a string s, sort it in decreasing order based on the frequency of the characters.
    The frequency of a character is the number of times it appears in the string.
    Return the sorted string. If there are multiple answers, return any of them.


    Example 1:
    Input: s = "tree"
    Output: "eert"
    Explanation: 'e' appears twice while 'r' and 't' both appear once.
    So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

'''

def frequencySort(s: str) -> str:
    # Sort the letters with occurence

    counts = defaultdict(int)

    for char in s:
        counts[char] += 1

    # Sort counts in descending order of occurence

    sorted_count = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    # Create a new string with the new sorted_count accordingly

    res = ''

    for k, v in sorted_count.items():
        res += (k * v)

    return res

# Test
# t_1 = "tree"
# t_2 = "cccaaa"
# t_3 = "Aabb"

# print(frequencySort(t_1))  --> eetr
# print(frequencySort(t_2))  --> cccaaa
# print(frequencySort(t_3))  --> bbAa