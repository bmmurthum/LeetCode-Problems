"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def can_visit_all_rooms(self, rooms: list[list[int]]) -> bool:
        """
        With a list of "rooms" where each room contains keys to the other
        locked rooms, can we visit all the rooms?

        Args:
            `rooms`: A list of rooms containing keys.
        Returns:
            `True/False`: Whether we can visit all rooms.
        """

        # Initialize variables
        key_ring = set()
        visited_rooms = set()
        for key in rooms[0]:
            key_ring.add(key)
        visited_rooms.add(0)

        # While we're still finding new keys, keep searching.
        while len(key_ring) != 0:
            temp = set()
            for key in key_ring:
                if key not in visited_rooms:
                    visited_rooms.add(key)
                    for new_key in rooms[key]:
                        temp.add(new_key)
            key_ring = temp

        # Return True/False
        if len(visited_rooms) < len(rooms):
            return False
        return True
