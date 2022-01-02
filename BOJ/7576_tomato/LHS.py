from os import statvfs_result
import sys
sys.stdin = open("input5.txt", "r")

shape = input().split()
M = int(shape[0])
N = int(shape[1])

status = []
for i in range(N):
  status.extend(list(map(int, input().split())))

zero_num = [x for x in status if x ==0]
# print(zero_num)
if (len(zero_num)==0):
    print(0)
else:        
    for i in range(M-1+N-1+M-1+N-2):
        news = [idx for idx in range(len(status)) if status[idx]==1]
        diff = 0
        for j in news:
            left = j - 1
            right = j + 1
            up = j - M
            down = j + M
            if (left>= 0 and left< M*N and int(left/M) == int(j/M)):
                if(status[left] == 0):
                    status[left] = 1
                    diff = 1
            if (right>= 0 and right< M*N and int(right/M) == int(j/M)):
                if(status[right] == 0):
                    status[right] = 1
                    diff = 1
            if (up>= 0 and up< M*N):
                if(status[up] == 0):
                    status[up] = 1
                    diff =1 
            if (down>= 0 and down< M*N):
                if(status[down] == 0):
                    status[down] = 1   
                    diff =1  
        if(diff==0):
            print(-1)
            break
        zero_num = [x for x in status if x ==0]
        if (len(zero_num)==0):
            if(i==0):
                print(i)
            else:
                print(i+1)
            break


