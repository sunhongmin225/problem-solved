'''
# python key, value 조회하고 싶을 때, items()를 꼭 붙여야함.
# python string에 대해 sorting 해볼 수 있다는 걸 못 생각해냈음..
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        anagrams hold data like below
        eg. 
            key: "aet"
            value: ["tea", "ate"]
        '''
        anagrams = dict({})

        for word in strs:
            '''
            word: "tea"
            word_sorted: "aet"
            '''
            word_sorted = ''.join(sorted(word))
            if word_sorted not in anagrams:
                anagrams[word_sorted] = [word]
            else:
                anagrams[word_sorted].append(word)

        answer = []
        for key, value in anagrams.items():
            answer.append(value)

        return answer


if __name__ == "__main__":
    # strs = ["eat","tea","tan","ate","nat","bat"]
    strs = [""]
    print(Solution().groupAnagrams(strs))