# You are given two strings word1 and word2. */
# Merge the strings by adding letters in alternating order, starting with word1.*/ 
# If a string is longer than the other, append the additional letters onto the end of the merged string. */
# Return the merged string. */

class solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            merged += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len(word1):
            merged += word1[i:]
        if j < len(word2):
            merged += word2[j:]
        return merged