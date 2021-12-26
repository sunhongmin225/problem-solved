import sys
sys.stdin = open("input.txt", "r")


cand = int(input())

mtime = []
for i in range(cand):
  mtime.append(list(map(int, input().split())))

# print(mtime)
mtime = sorted(mtime, key=lambda x:x[0])
# print(mtime)
mtime = sorted(mtime, key=lambda x:x[1])
# print(mtime)

last = -1
num = 0
for st, end in mtime:
  if st >= last:
    last = end
    num += 1
    
print(num)

# print(mtime)
# num = 0
# # for-loop for all combinations
# for i in range(1, 10):
#   onehot = bin(i)[2:].zfill(cand)
#   tnum = 1
#   start = -1
#   end = -1 
#   print(onehot)
#   for index, flag in enumerate(onehot):
#     if (flag == "1"):
#       print(index)
#       if(start == -1):
#         start = mtime[index][0]
#         end = mtime[index][1]
#       else:

#     else: 
#       continue

  
# # tstart = []
# # tend = []
# num = 0
# mtime=[]
# for i in range(meetings):
#   mtime.append(list(map(int, input().split())))
# print(mtime)
#   # tstart.append(int(temp[0]))
#   # tend.append(int(temp[1]))


# num = 0

# for i in range(meetings):
#   tnum = 1
#   start = mtime[i][0]
#   end = mtime[i][1]

#   for iter in range(i+1, meetings):
#     if (mtime[iter][0] >= end):
#       end = mtime[iter][1]
#       tnum = tnum + 1
#   num = max(num, tnum)

# print(num)
