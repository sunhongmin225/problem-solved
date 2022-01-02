op = ["plus", "minus", "mult", "div", "space"]

def ntest(N, number, tlist, count):
    temp = []
    if(count==2):
        for num2 in op:
            if(num2=="plus"):
                res = N+N
                temp.append(res)
                if(res == number):
                    return 1
            elif(num2=="minus"):
                res = N-N
                temp.append(res)
                if(res == number):
                    return 1
            elif(num2=="mult"):
                res = N*N
                temp.append(res)
                if(res == number):
                    return 1
            elif(num2=="div"):
                res = int(N/N)
                temp.append(res)
                if(res == number):
                    return 1
            elif(num2=="space"):
                res = 10*N + N
                temp.append(res)
                if(res == number):
                    return 1        
    else:
        for num in op:
            if(num=="plus"):
                for i in range(len(tlist[count-1])):
                    res = tlist[count-1][i] + N
                    temp.append(res)
                    if(res == number):
                        return 1
            elif(num=="minus"):
                for i in range(len(tlist[count-1])):
                    res = tlist[count-1][i] - N
                    temp.append(res)
                    if(res == number):
                        return 1
            elif(num=="mult"):
                for i in range(len(tlist[count-1])):
                    res = tlist[count-1][i] * N
                    temp.append(res)
                    if(res == number):
                        return 1
            elif(num=="div"):
                for i in range(len(tlist[count-1])):
                    res = int(tlist[count-1][i] / N)
                    temp.append(res)
                    if(res == number):
                        return 1
            elif(num=="space"):
                res = 0
                for i in range(count):
                    res += N * 10**i
                temp.append(res)
                if(res == number):
                    return 1 
          
    tlist.append(temp)
    return 0

def solution(N, number):
    answer = 0
    tlist = []
    tlist.append([])
    tlist.append([])

    if(N == number):
        answer = 1
        return answer
    else:
        # for count in range(2,9):
        for count in range(2,9):
            flag = ntest(N,number,tlist,count)
            if(flag == 1):
                return count
        
    return -1


## answer ##
# def solution(NUM, number):
#     arr = [[]] + [[int(str(NUM) * i)] for i in range(1,9)]

#     if [number] in arr:
#         return arr.index([number])

#     for i in range(2, 9):
#         for j in range(1, i):
#             for a in arr[j]:
#                 for b in arr[i-j]:
#                     arr[i].append(a + b)
#                     arr[i].append(a * b)
#                     arr[i].append(a - b)
#                     if 0 != b:
#                         arr[i].append(a // b)
#         if number in arr[i]:
#             return i
#         arr[i] = list(set(arr[i]))

#     return -1