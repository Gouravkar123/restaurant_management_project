class TaskQueue:
    def __init__(self):
        self.queue = []

    # Add task to the queue (Enqueue)
    def enqueue(self, task):
        self.queue.append(task)
        print(f"Task added: {task}")

    # Remove task from the queue (Dequeue)
    def dequeue(self):
        if not self.is_empty():
            task = self.queue.pop(0)
            print(f"Task processed & removed: {task}")
            return task
        else:
            print("Queue is empty. No task to process.")
            return None

    # Peek at the first task without removing it
    def peek(self):
        if not self.is_empty():
            print(f"Next task to process: {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty.")
            return None

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Show current tasks
    def display(self):
        print("Current Queue:", self.queue)


# --- Simulation Example ---
if __name__ == "__main__":
    task_queue = TaskQueue()

    # Add tasks
    task_queue.enqueue("Send Welcome Email")
    task_queue.enqueue("Generate Report")
    task_queue.enqueue("Resize Uploaded Image")

    task_queue.display()

    # Peek next task
    task_queue.peek()

    # Process tasks (like workers do in Celery/Redis)
    task_queue.dequeue()
    task_queue.dequeue()
    task_queue.dequeue()
    task_queue.dequeue()  # extra call to show empty queue handling
