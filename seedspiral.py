import numpy as np


class SeedPacker:
    max_num = 200

    def __init__(self, x, seed_size=3):
        self.rot_angle = np.pi * 2 * x
        self.seeds = []
        self.seed_size = seed_size
        self.radius = 0
        self.r1 = 4.2

    def min_dist(self, x0, y0):
        min_distance = 0
        for x, y, _, _ in self.seeds:
            dx = x - x0
            dy = y - y0
            d = np.sqrt(dx * dx + dy * dy)
            if not min_distance or min_distance > d:
                min_distance = d
        return min_distance

    def pack_seeds(self):
        theta = 0
        self.radius = 0
        seed_size = self.seed_size
        while True:
            self.radius += seed_size
            self.seeds.append(self.next_position(theta, seed_size))
            if len(self.seeds) >= self.max_num:
                break
            theta += self.rot_angle
            seed_size += 0.05

    def next_position(self, theta, size):
        while True:
            x = self.radius * np.cos(theta)
            y = self.radius * np.sin(theta)
            gap = self.min_dist(x, y) - size * 2
            # print(x, y, gap)
            if gap <= 0:
                break
            self.radius -= gap / 2 if gap > 2 else 1
        return x, y, theta, size
