class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #question similar to rotten oranges but returning other one
        original_color = image[sr][sc]

        if original_color == color:
            return image 
        def dfs(image,sr,sc,color):
            rows,cols=len(image),len(image[0])
            if (sr<0 or sc<0 or sr>=rows or sc>=cols or image[sr][sc]!=original_color):
                return
            directions=[[0,1],[1,0],[0,-1],[-1,0]]
            image[sr][sc]=color
            for dr,dc in directions:
                nr,nc=dr+sr,dc+sc
                dfs(image,nr,nc,color)

        dfs(image,sr,sc,color)
        return image


            



        