# thank you python ^^

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_string = ''.join(sorted(word)) # sort letters in string in alphabetical order
            if sorted_string in anagrams:
                anagrams[sorted_string].append(word)
            else:
                anagrams[sorted_string] = [word]
        
        output = []
        for k in anagrams:
            output.append(anagrams[k])
          
        return output
