def get_bj_input():
    n = int(input())
    times = []
    for _ in range(n):
        start, end = map(int, input().split())
        times.append({'start':start, 'end':end})
    return times

def sol(times=None):
    if times is None:
        times = get_bj_input()
        sol(times)
    else:
        times.sort(key = lambda x: x.get('start'))
        times.sort(key = lambda x: x.get('end'))
        result = 0
        previous_end = None

        for _, time in enumerate(times):
            if previous_end is None or time.get('start') >= previous_end:
                result += 1
                previous_end = time.get('end')

        print(result)
        return result


if __name__=="__main__":
    sol()
    # debug
    n = 11
    times = [
        {'start':1,'end':4},
        {'start':3,'end':5},
        {'start':0,'end':6},
        {'start':5,'end':7},
        {'start':3,'end':8},
        {'start':5,'end':9},
        {'start':6,'end':10},
        {'start':8,'end':11},
        {'start':8,'end':12},
        {'start':2,'end':13},
        {'start':12,'end':14}
        ]
    sol(times)