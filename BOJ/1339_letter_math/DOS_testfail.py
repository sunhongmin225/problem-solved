"""
current:
  - pairwise comparsion: O(n^2)
  1. sort words long -> short
  2. compare left <-> right 
    1. if left is longer or same than right -> assign largest number to first left letter
  3. iterate until sorted words list is full of '' strings.

future:
  - pairwise comparision: O(n^2) 
  - needs additional function that counts the number(or result values) of the current letter
"""

def get_bj_input():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(str(input()))
    return words


def main(words):
    LETTER_VALUES = dict()
    N_WORDS = len(words)
    NUMS_LIST = list(range(0, 10))

    def get_sorted_words(words):
        return sorted(words, key=len, reverse=True)

    def get_words_len(sorted_words):
        return [len(word) for word in sorted_words]

    def word2int(word, letter_values):
        result = ''
        for letter in word:
            result += str(letter_values.get(letter))
        return int(result)

    sorted_words = get_sorted_words(words)
    len_words = get_words_len(sorted_words)

    while sorted_words != [''] * N_WORDS:
        for i, _ in enumerate(sorted_words):
            for j in range(i):
                if len_words[j] >= len_words[i]:
                    if sorted_words[j] != '' and LETTER_VALUES.get(sorted_words[j][0]) is None:
                        LETTER_VALUES[sorted_words[j][0]] = NUMS_LIST.pop()
                    sorted_words[j] = sorted_words[j][1:]
                    len_words[j] -= 1
                else:
                    if sorted_words[i] != '' and LETTER_VALUES.get(sorted_words[i][0]) is None:
                        LETTER_VALUES[sorted_words[i][0]] = NUMS_LIST.pop()
                    sorted_words[i] = sorted_words[i][1:]
                    len_words[i] -= 1

    return sum([word2int(word, LETTER_VALUES) for word in words])


# 제출용 코드
# print(main(get_bj_input()))


if __name__=="__main__":
    words = ["GCF", "ACDEB"] # 683 + 98754 = 99437
    print(main(words))# 
    words = ["AAA", "AAA"] # 999 + 999 = 1998
    print(main(words))# 
    words = ["A", "B"] # 9 + 8 = 17
    print(main(words))# 
    words = ["AB", "BA"] # 98 + 89 = 187
    print(main(words))# 
    words = ["A", "BA"] # 98 + 8 = 106
    print(main(words))# 
    words = ["A", "B", "C"] # 9 + 8 + 7 = 24
    print(main(words))# 
    words = ["A", "B"] # 9 + 8 = 17
    print(main(words))# 
    words = ["A", "B", "C", "D", "E", "F", "G" , "H" , "I"] # 45
    print(main(words))# 
    words = ["ABB", "BB", "BB", "BB", "BB", "BB", "BB", "BB", "BB", "BB"] # A: 8, B: 9 => 1790
    print(main(words))# 