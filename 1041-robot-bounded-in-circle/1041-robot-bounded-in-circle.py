class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = y = 0
        direction = 0  # 0=N, 1=E, 2=S, 3=W

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = moves[direction]
                x += dx
                y += dy
            elif instruction == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0