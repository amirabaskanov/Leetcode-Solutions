class TimeMap:
    # Read fine print for this problem: All timestamps are in increasing order
    def __init__(self):
        self.store = {} # key=string, value=list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" #bcz they want us to return an empty string if edgecase
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res