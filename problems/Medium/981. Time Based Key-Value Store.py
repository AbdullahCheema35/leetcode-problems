from typing import Dict, Tuple, List


class TimeMap:
    class TimeValList:
        def __init__(self):
            self.val: List[Tuple[int, str]] = []
        
        def get(self, time: int) -> str:
            res: str = ""
            l, r = 0, len(self.val) - 1
            while l <= r:
                mid = (l + r) >> 1
                if self.val[mid][0] < time:
                    l = mid + 1
                    res = self.val[mid][1]
                elif self.val[mid][0] > time:
                    r = mid - 1
                else:
                    return self.val[mid][1]
            return res
        
        def set(self, time: int, val: str) -> None:
            self.val.append((time, val))

    def __init__(self):
        self.kv_store: Dict[str, TimeMap.TimeValList] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kv_store:
            self.kv_store[key] = TimeMap.TimeValList()
        self.kv_store[key].set(timestamp, value)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.kv_store:
            return self.kv_store[key].get(timestamp)
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)