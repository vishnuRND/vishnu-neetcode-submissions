class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        left = 0
        values = self.time_map[key]
        right = len(values) - 1
        result = ""
        while left <= right:
            mid = (left+right) // 2
            mid_timestamp = values[mid][0]
            mid_value = values[mid][1]
            if mid_timestamp == timestamp:
                result = mid_value
                break
            elif mid_timestamp < timestamp:
                result = mid_value
                left = mid+1
            else:
                right = mid-1

        return result

            
        
