class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        intersection_list = []
        first_idx = 0
        second_idx = 0
        
        if len(firstList) == 0 or len(secondList) == 0:
            return []
        
        while(True):
            interval1 = firstList[first_idx]
            interval2 = secondList[second_idx]
            
            if interval1[0] > interval2[1]:
                # if interval 1 starts after interval 2 ends
                second_idx += 1
            elif interval1[1] < interval2[0]:
                # if interval 2 starts after interval 1 ends
                first_idx += 1
            else:
                # else there is an overlap
                if interval2[0] >= interval1[0] and interval2[1] <= interval1[1]:
                    # [...[interval 2]...] <- interval 1
                    intersection_list.append(interval2)
                    second_idx += 1
                elif interval2[0] <= interval1[0] and interval2[1] >= interval1[1]:
                    # [...[interval 1]...] <- interval 2
                    intersection_list.append(interval1)
                    first_idx += 1
                elif interval1[0] <= interval2[0] and interval1[1] <= interval2[1]:
                    # interval 1 -> [...[...]...] <- interval 2
                    intersection_list.append([interval2[0], interval1[1]])
                    first_idx += 1
                elif interval1[0] >= interval2[0] and interval1[1] >= interval2[1]:
                    # interval 2 -> [...[...]...] <- interval 1
                    intersection_list.append([interval1[0], interval2[1]])
                    second_idx += 1
            
            if first_idx == len(firstList) or second_idx == len(secondList):
                break
        
        return intersection_list
