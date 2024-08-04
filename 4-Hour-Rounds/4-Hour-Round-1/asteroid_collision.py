"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def asteroid_collision(self, asteroids: list[int]) -> list[int]:
        """
        With a collection of noted asteroids in a line with their sizes and
        their direction, return a list of the asteroids after their collisions.

        Args:
            `asteroids`: A list of asteroids.
        Returns:
            `resulting_asteroids`: The list of asteroids after collisions.
        """

        # Build and remove from stack based on the interactions of the last
        # item in the stack and its relation to the newest considered item.
        resulting_asteroids = []
        resulting_asteroids.append(asteroids[0])
        for _, current in enumerate(asteroids[1:], 1):
            if len(resulting_asteroids) == 0:
                resulting_asteroids.append(current)
                continue
            # If the new asteroid is going left
            if current < 0:
                if len(resulting_asteroids) > 0 and resulting_asteroids[-1] < 0:
                    resulting_asteroids.append(current)
                else:
                    exploded = False
                    while len(resulting_asteroids) > 0 and resulting_asteroids[-1] > 0:
                        if resulting_asteroids[-1] + current < 0:
                            resulting_asteroids.pop()
                            continue
                        elif resulting_asteroids[-1] + current > 0:
                            exploded = True
                            break
                        else:
                            resulting_asteroids.pop()
                            exploded = True
                            break
                    if not exploded:
                        if len(resulting_asteroids) == 0:
                            resulting_asteroids.append(current)
                        elif resulting_asteroids[-1] < 0:
                            resulting_asteroids.append(current)
            # If the new asteroid is going right
            elif current > 0:
                resulting_asteroids.append(current)

        # Return the result
        return resulting_asteroids
