
if __name__ == '__main__':
    num = int(input())
    letter_numbers = []

    for _ in range(num):
        letter_numbers.append(input())
    
    weights = {}
    # get the weights for each alphabet
    for letter_num in letter_numbers:
        for ind, alphabet in enumerate(letter_num):
            if alphabet in weights:
                weights[alphabet] += 10 ** (len(letter_num) - ind - 1)
            else:
                weights[alphabet] = 10 ** (len(letter_num) - ind - 1)

    numbers = []
    for weight in weights.values():
        numbers.append(weight)
    
    numbers.sort(reverse=True)

    result = 0
    digit = 9
    for number in numbers:
        result += digit * number
        digit -= 1

    print(result)