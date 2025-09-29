import time

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.users = {}  # { user_id: [start_time, request_count] }

    def is_allowed(self, user_id: str) -> bool:
        current_time = time.time()

        if user_id not in self.users:
            # First request for user → create record
            self.users[user_id] = [current_time, 1]
            print(f"✅ Request allowed for {user_id}")
            return True

        start_time, count = self.users[user_id]

        if current_time - start_time < self.window_seconds:
            # Still in the same window
            if count < self.max_requests:
                self.users[user_id][1] += 1
                print(f"✅ Request allowed for {user_id} ({count+1}/{self.max_requests})")
                return True
            else:
                print(f"⛔ Rate limit exceeded for {user_id}, try after {int(self.window_seconds - (current_time - start_time))}s")
                return False
        else:
            # Window expired → reset
            self.users[user_id] = [current_time, 1]
            print(f"✅ Request allowed for {user_id} (new window started)")
            return True