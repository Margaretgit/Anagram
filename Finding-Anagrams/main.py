# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    str1 = "below"
    str2 = "elbow"

# check if length is same
if(len('below') == len('elbow')):

    # sort the strings
    sorted_str1 = sorted('below')
    sorted_str2 = sorted('elbow')

    # if sorted char arrays are same
    if(sorted_str1 == sorted_str2):
        print('below' + " and " + 'elbow' + " are anagram.")
    else:
        print('below' + " and " + 'elbow' + " are not anagram.")

else:
    print('below' + " and " + 'elbow' + " are not anagram.")



