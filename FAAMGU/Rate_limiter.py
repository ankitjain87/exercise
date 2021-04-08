
from collections import defaultdict
from datetime import datetime, timedelta
import time


# n = 3
# duration = 5
# {
#     1: [1,3,5,7,9]=> [5,7,9]

# }


class RateLimiter:
    def __init__(self, no_of_requests, in_time):
        self.customer_map = defaultdict(list)
        self.allowed_requests = no_of_requests
        self.duration = in_time


    def allow(self, customer_id):
        if customer_id not in self.customer_map:
            self.customer_map[customer_id].append(datetime.now())
            return True

        old_requests = self.customer_map[customer_id]
        # old_requests.reverse()
        count = 0
        now = datetime.now()
        for i in range(len(old_requests)-1, -1, -1):
            if (now - old_requests[i]).total_seconds() <= self.duration:  # 10 - 9 => 1, 3, 5 => 3
                count += 1
            else:
                self.customer_map[customer_id] = old_requests[i+1:]
                break

        if count < self.allowed_requests:
            self.customer_map[customer_id].append(now)
            return True

        return False



rl = RateLimiter(1, 3)
for i in range(10):
    print(1, rl.allow(1))
    time.sleep(1)
    print(2, rl.allow(2))
    print(3, rl.allow(3))



        

            
        



