def solution(N, number):
    tbl = [[]]
    for i in range(1,9):
        operation_results = []
        for j in range(0,i):
            for x in tbl[j]:
                for y in tbl[i-j]:
                    operation_results.append(x+y)
                    operation_results.append(x*y)
                    operation_results.append(x-y)
                    if y != 0:
                        operation_results.append(x//y)

        operation_results.append(int(str(N)*i))

        if number in operation_results:
            return i
        tbl.append(list(set(operation_results)))

    return -1

   
if __name__=="__main__":
    print(solution(5, 12)) # 4
    print(solution(2, 11)) # 3