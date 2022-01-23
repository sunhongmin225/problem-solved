
num = int(input())
words = []
for i in range(num):
  words.append(input())

# In this case KeyError(Runtime error) appears
# nums = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0}

## nums can be any alphabets
nums = {}
for word in words:
  for i in range(len(word)):
    alphabet = word[len(word)-i-1]
    # if the alphabet is not visited, add it to the dictionary
    if alphabet not in nums:
      nums[word[len(word)-i-1]] = 10**i
    # if the alphabet is visited, add it to prev. sum of the value
    else:
      nums[word[len(word)-i-1]] += 10**i

## sort nums w.r.t value
sorted_dict = sorted(nums.items(), key = lambda item: item[1], reverse=True)

result = 0
for i in range(len(sorted_dict)):
  if sorted_dict[i][1] != 0:
    result += (9-i)*sorted_dict[i][1]
print(result)
