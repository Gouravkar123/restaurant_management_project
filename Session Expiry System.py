import time
import uuid

class SessionManager:
    def __init__(self, session_timeout: int = 60):
        """
        session_timeout: lifetime of session in seconds
        """
        self.session_timeout = session_timeout
        self.sessions = {}  # { session_id: [user_id, creation_time] }

    # Create a new session
    def create_session(self, user_id: str) -> str:
        session_id = str(uuid.uuid4())  # unique session ID
        self.sessions[session_id] = [user_id, time.time()]
        print(f"Session created: {session_id} for user {user_id}")
        return session_id

    # Validate if session is active
    def is_session_active(self, session_id: str) -> bool:
        if session_id not in self.sessions:
            print(f"Session {session_id} not found.")
            return False

        user_id, creation_time = self.sessions[session_id]
        current_time = time.time()

        if current_time - creation_time < self.session_timeout:
            print(f"Session {session_id} is active for user {user_id}")
            return True
        else:
            # Session expired → remove it
            del self.sessions[session_id]
            print(f"Session {session_id} expired for user {user_id}")
            return False

    # Optional: clean up all expired sessions
    def cleanup_expired_sessions(self):
        expired = []
        current_time = time.time()
        for session_id, (user_id, creation_time) in list(self.sessions.items()):
            if current_time - creation_time >= self.session_timeout:
                expired.append(session_id)
                del self.sessions[session_id]
        print(f"Cleaned up expired sessions: {expired}")

    # List active sessions
    def list_active_sessions(self):
        print("Active Sessions:", self.sessions)
        return self.sessions
