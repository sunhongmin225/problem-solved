'''
Notes:
1. how to sort by a specific column (using lambda)
2. how to split a string in python
3. Get used to how to process input in BOJ style
4. Why should I solve this with Greedy algorithm?
'''

# TYPE: greedy

import sys

def solution(num: int, timelines: list[tuple[int]]) -> int:
    # 1. Sort the timelines first by start time, and then by end time
    timelines = sorted(timelines, key=lambda item: item[0])
    timelines = sorted(timelines, key=lambda item: item[1])

    cnt = 0
    most_recent_ended = 0

    for start, end in timelines:
        if start >= most_recent_ended: 
            cnt += 1
            most_recent_ended = end
    
    return cnt


if __name__ == "__main__":
    num = int(input())
    
    timelines = []
    for i in range(num):
        start, end = map(int, input().split())
        timelines.append((start, end))

    ans = solution(num, timelines)
    print(ans)


