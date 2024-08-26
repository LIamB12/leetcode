class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key, value, timestamp):
        if key in self.data:
            self.data[key]['times'].append(timestamp)
            self.data[key]['values'].append(value)
        else:
            self.data[key] = {}
            self.data[key]['times'] = [timestamp]
            self.data[key]['values'] = [value]

    def get(self, key, timestamp):
        if key not in self.data:
            return ""

        times = self.data[key]['times']
        values = self.data[key]['values']

        l = 0
        r = len(times) - 1

        max_index_under_ts = -1

        while l <= r:
            m = (l + r) // 2
            num = times[m]

            if num == timestamp:
                return values[m]
            
            if num > timestamp:
                r = m - 1
                
            if num < timestamp:
                l = m + 1
                max_index_under_ts = max(max_index_under_ts, m)

        if max_index_under_ts == -1:
            return ""
        else:
            return values[max_index_under_ts]

