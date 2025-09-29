class InMemoryFileStorage:
    def __init__(self):
        # Dictionary to store files { "filename": "content" }
        self.storage = {}

    # Create or update a file
    def upload(self, filename: str, content: str) -> None:
        self.storage[filename] = content
        print(f"Uploaded file: {filename}")

    # Retrieve file content
    def read(self, filename: str) -> str:
        if filename in self.storage:
            print(f"Reading file: {filename}")
            return self.storage[filename]
        else:
            print(f"File not found: {filename}")
            return None

    # Delete a file
    def delete(self, filename: str) -> None:
        if filename in self.storage:
            del self.storage[filename]
            print(f"Deleted file: {filename}")
        else:
            print(f"Cannot delete, file not found: {filename}")

    # List all stored files
    def list_files(self):
        print("Files in storage:", list(self.storage.keys()))
        return list(self.storage.keys())