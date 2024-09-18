from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        original = image[sr][sc]
        image[sr][sc] = color

        # Using dict as a lookup for dynamic programming
        d: dict[tuple[int, int], int] = {(sr, sc): 1}

        self.fill(image, sr, sc + 1, original, color, d)
        self.fill(image, sr, sc - 1, original, color, d)
        self.fill(image, sr - 1, sc, original, color, d)
        self.fill(image, sr + 1, sc, original, color, d)

        return image

    def fill(
        self,
        image: List[List[int]],
        i: int,
        j: int,
        original: int,
        color: int,
        d: dict[tuple[int, int], int],
    ) -> None:
        # if index out of bounds
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
            return
        # if not the same color as original
        if image[i][j] != original:
            return

        # Check of dynamic Programming
        if d.get((i, j)) is not None:
            return

        # update lookup value
        d[(i, j)] = 1
        # change color
        image[i][j] = color
        # check in other 4 directions
        self.fill(image, i, j + 1, original, color, d)
        self.fill(image, i, j - 1, original, color, d)
        self.fill(image, i - 1, j, original, color, d)
        self.fill(image, i + 1, j, original, color, d)
