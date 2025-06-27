class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startcolor = image[sr][sc]
        if startcolor == color:
            return image  # No need to change anything

        m = len(image)
        n = len(image[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j):
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == startcolor:
                    image[nr][nc] = color
                    dfs(nr, nc)

        image[sr][sc] = color
        dfs(sr, sc)
        return image
