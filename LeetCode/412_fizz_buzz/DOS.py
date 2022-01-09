class Solution:
    def fizzBuzz(self, n: int):
        result = []
        if 1 <= n <= 10**4:
            for i in range(1, n+1):
                if (i % 5 == 0) and (i % 3 == 0):
                    result.append('FizzBuzz')
                elif (i % 5 == 0):
                    result.append('Buzz')
                elif (i % 3 == 0):
                    result.append('Fizz')
                else:
                    result.append(str(i))

        return result


if __name__=="__main__":
    print(sol(15))

