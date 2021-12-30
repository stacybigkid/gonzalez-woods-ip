import numpy as np

class PixelDistance:
    ''' A class to calculate distance between two given 
    pixel position tuples, p and q.'''

    def __init__(self, p, q):

        self.x1, self.y1 = p
        self.x2, self.y2 = q

        # the two px positions must be different:
        assert (self.x1 != self.x2) & (self.y1 != self.y2), "The specified pixels are the same! Their distance is 0"

    def calculate_euclidian_distance(self):
        return np.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)

    def calculate_city_block_distance(self):
        return np.absolute(self.x1 - self.x2) + np.absolute(self.y1 - self.y2)

    def calculate_chessboard_distance(self):
        return np.max([np.absolute(self.x1 - self.x2), np.absolute(self.y1 - self.y2)])


if __name__ == '__main__':
    p = (1, 1)
    q = (4, 4)
    pd = PixelDistance(p, q)

    print(f'The 8 px distance between p and q is {pd.calculate_chessboard_distance()}')



