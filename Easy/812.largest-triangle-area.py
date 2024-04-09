class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in points:
            for j in points:
                for k in points:
                    res = max(
                        res,
                        0.5
                        * (
                            abs(
                                i[0] * j[1]
                                + j[0] * k[1]
                                + k[0] * i[1]
                                - j[0] * i[1]
                                - k[0] * j[1]
                                - i[0] * k[1]
                            )
                        ),
                    )

        return res
