class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return list()
        res = []

        for first in firstList:
            for second in secondList:
                # no overlap between first and second
                if second[1] < first[0] or first[1] < second[0]:
                    continue
                # when first is bigger than second
                elif first[0] <= second[0] and second[1] <= first[1]:
                    res.append(second)
                # when second is bigger than first
                elif second[0] <= first[0] and first[1] <= second[1]:
                    res.append(first)
                # partially overlapped: second -> first
                elif second[0] <= first[0] and first[0] <= second[1] and second[1] <= first[1]:
                    res.append([first[0], second[1]])
                # partially overlapped: first -> second
                elif first[0] <= second[0] and second[0] <= first[1] and first[1] <= second[1]:
                    res.append([second[0], first[1]])
        return(res)
