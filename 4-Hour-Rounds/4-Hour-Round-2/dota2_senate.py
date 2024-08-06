"""Problem from LeetCode.com"""


class Solution:
    """Problem from LeetCode.com"""

    def predict_party_victory(self, senate: str) -> str:
        """
        Simulate a group of senators that vote in rounds and have the ability
        to take away the other's ability to vote.

        Args:
            `senate`: A list of senators denoted by their party.
        Returns:
            `"Radiant"` or `"Dire"`: The ultimate winner of the voting rounds.
        """

        # While there are more than a single senator, run another round.
        while len(senate) > 1:

            # Handle taking away rights mid-round.
            midround_senate = ""
            d_skips = 0
            r_skips = 0
            d_count = 0
            r_count = 0
            for senator in senate:
                if senator == "R":
                    r_count += 1
                    if r_skips > 0:
                        r_skips -= 1
                    else:
                        d_skips += 1
                        midround_senate += senator
                elif senator == "D":
                    d_count += 1
                    if d_skips > 0:
                        d_skips -= 1
                    else:
                        r_skips += 1
                        midround_senate += senator

            # If down to one senator, we can stop.
            if len(midround_senate) == 1:
                senate = midround_senate
                break
            # If all from one party, we can stop.
            if d_count == 0:
                senate = "R"
                break
            if r_count == 0:
                senate = "D"
                break

            # Any left over banning should be done to left-most senators.
            new_senate = ""
            if d_skips > 0:
                i = 0
                while d_skips > 0 and i < len(midround_senate):
                    if midround_senate[i] == "R":
                        new_senate += "R"
                    else:
                        d_skips -= 1
                    i += 1
                new_senate += midround_senate[i:]
            if r_skips > 0:
                i = 0
                while r_skips > 0 and i < len(midround_senate):
                    if midround_senate[i] == "D":
                        new_senate += "D"
                    else:
                        r_skips -= 1
                    i += 1
                new_senate += midround_senate[i:]

            # Setup to start a new round.
            if new_senate == "":
                senate = midround_senate
            else:
                senate = new_senate

        # With one senator left, return output.
        if senate == "R":
            return "Radiant"
        return "Dire"
