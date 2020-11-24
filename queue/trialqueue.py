import random

class PrintQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items[-1]


class Job:

    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_pages(self):
        if self.pages > 0:
            self.pages -= 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self):
        self.current_job = None

    def get_job(self, print_queue):
        try:
            self.current_job = print_queue.dequeue()
        except IndexError:
            return "No more jobs to print"

    def print_job(self, job):
        while job.pages > 0:
            job.print_pages()

        if job.check_complete():
            return "Printing Completed"

        else:
            return "Incomplete"

