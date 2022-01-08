class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz = []
        for num in range(n):
            if (num+1) % 15 == 0:
                fizzbuzz.append("FizzBuzz")
            elif (num+1) % 5 == 0:
                fizzbuzz.append("Buzz")
            elif (num+1) % 3 == 0:
                fizzbuzz.append("Fizz")
            else:
                fizzbuzz.append(str(num+1))
                
        return fizzbuzz
