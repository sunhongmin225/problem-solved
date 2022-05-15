# Time limit exceed
class Solution:
    def numSquares(self, n: int) -> int:
        int(sqrt(n))
        # [0] is not used, [1...]
        way = [0 for i in range(n+1)]
        
        # 1 1-1
        # 2 2-1+1
        # 3 3-1+1+1 
        # 4 1-4
        # 5 2-4+1
        # 6 3-4+1+1
        # 7 4-4+1+1+1     
        # 8 2-4+4
        # 9 1-9
        # 10 2-9+1
        # 11 3-9+1+1
        # 12 3-4+4+4
        # 13 2-9+4
        # 14 9+5 =3 4+4+4+1+1
        # 48 16 16 16 
        for i in range(1, n+1):
            root = sqrt(i)
            iroot = int(sqrt(i))
            
            if iroot == 1:
                way[i] = i
            elif root == iroot:
                way[i] = 1
            else:
                val = 10001
                ## i >= 4
                for j in range(iroot, 0, -1):
                    # print(f"i is {i}, iroot is {iroot} j is {j}")
                    quo = int(i/j**2)
                    rem = i - quo*j**2
                    newval = quo + way[rem]
                    # print(f"quo: {quo}, rem: {rem}, newval:{newval}")
                    val = min(val, newval)
                way[i] = val
        
        return way[-1]
