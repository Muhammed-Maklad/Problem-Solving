class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            last = out[-1]
            current = intervals[i]

            if last[1] >= current[0]:
                last[1] = max(last[1], current[1])
            else:
                out.append(current)
        return out