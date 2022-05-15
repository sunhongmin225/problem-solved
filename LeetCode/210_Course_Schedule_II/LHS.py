class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        num_pre = len(prerequisites)
        pre_dict = {}
		
		# dict initialize	
        for i in range(numCourses):
            if i not in pre_dict:
                pre_dict[i] = []
       
        # key: number, value: list of prerequisites
		for pair in prerequisites:
            pre_dict[pair[0]].append(pair[1])
        res = []
        while(len(pre_dict)):
            canuse = [key for key in pre_dict if len(pre_dict[key])==0]
            if len(canuse) == 0:
                break
            res.extend(canuse)
            # if predict[canuse] is empty, erase it from dict
			for num in canuse:
                pre_dict.pop(num)
            for key in pre_dict:
                pre_dict[key] = list(set(pre_dict[key]) - set(canuse))
                
        if len(res) == numCourses:
            return res
        else:
            return []
