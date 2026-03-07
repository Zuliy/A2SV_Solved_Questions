class Solution:
    def flipAndInvertImage(self, image):
        for row in image:
            # Reverse the row and invert each bit
            for i in range((len(row) + 1) // 2):
                # Swap and invert at the same time
                row[i], row[-i-1] = 1 - row[-i-1], 1 - row[i]
        return image