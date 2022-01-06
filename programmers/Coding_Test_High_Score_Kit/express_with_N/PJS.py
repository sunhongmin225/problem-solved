def solution(N, number):
    """
    possible_answers: a list of tuples (some number A, # of minimum N's to make A)
    num_min_calculations: a dictionary where keys are some number (reulst of some calculation)
                          and the values are tuples where 
                          (# of minimum N's to make A, index of that number in possible_answers)
    """
    possible_answers = []
    num_min_calculations = {}

    for i in range(8):
        tmp = ""
        for j in range(i+1):
            tmp += str(N)
        possible_answers.append((int(tmp), i+1))
        num_min_calculations[int(tmp)] = (i+1, i)

    for i in range(7):
        # can use at most 8 N's.
        possible_answers_tmp = possible_answers.copy()  # a copy to update within the for loop

        for num1 in possible_answers:            
            for num2 in possible_answers:
                # num_[0] is the actual calculated value, and num_[1] is # of minimum N's needed for that value
                cnt = num1[1] + num2[1] 
                if cnt >= 9:
                    continue
                
                calculations = [num1[0]+num2[0], num1[0]*num2[0], num1[0]-num2[0], num2[0]-num1[0]]
                if num2[0] != 0:
                    calculations.append(num1[0] // num2[0])
                if num1[0] != 0:
                    calculations.append(num2[0] // num1[0]) 
                
                # calculations hold all possible calculated results given the two numbers
                for calculation in calculations:
                    if calculation not in num_min_calculations.keys():
                        # if this is a value newly seen, add that to the num_min_calculations dictionary,
                        # and append it to the possible_answers_tmp list
                        num_min_calculations[calculation] = (cnt, len(possible_answers_tmp))
                        possible_answers_tmp.append((calculation, cnt))
                    else:
                        if num_min_calculations[calculation][0] > cnt:
                            # if the previously known minimum # of N's needed for the calculation is larger than
                            # what is seen currently, then update the num_min_calculations, and the
                            # corresponding tuple in the proper index of the possible_answers_tmp list.
                            index_in_list = num_min_calculations[calculation][1]
                            num_min_calculations[calculation] = (cnt, index_in_list)
                            possible_answers_tmp[index_in_list] = (possible_answers_tmp[index_in_list][0], cnt)

        possible_answers = possible_answers_tmp
    
    for num in possible_answers:
        if num[0] == number:
            return num[1]
    
    return -1


if __name__ == '__main__':
    print(solution(5, 12))
