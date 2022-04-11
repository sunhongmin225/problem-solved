class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
		# dictionary for grouping
		str_dict={}
        
        for str in strs:
			# convert each str in ascending order
            key = ''.join(sorted(str))
            if key not in str_dict:
                str_dict[key]=[]
                str_dict[key].append(str)
            else:
                str_dict[key].append(str)
        return list(str_dict.values())
