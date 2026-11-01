class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        gride = []
        
        for x in range(m):
            if x == 0 :
                gride.append('.'*n)
            else:
                gride.append('#'*(n-1)+'.')
        
        return gride
            
            
cost = 0
grid = [[1,2],[3,4]]

