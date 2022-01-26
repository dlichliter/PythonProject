import random
import time


# Simulate a queue for a movie theater
# Till show is the time until the show starts and tickets cannot be sold
# max time is how long it takes a person to purchase a ticket
def simulate_line(till_show, max_time):
    # Pq represents the people who want to purchase a ticket
    pq = Queue()
    tx_sold = []

    for i in range(50):
        pq.enqueue("Person" + str(i))
        t_end = time.time() + till_show
        now = time.time()
        # While t_end has not been reached and there are still people in the queue
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            # simulate how long it takes to buy a ticket
            time.sleep(r)
            # After the person buys a ticket, remove them from pq and place them in the tickets sold list
            person = pq.dequeue()
            print(person)
            tx_sold.append(person)

    return tx_sold


# The queue class represents a queue data structure, with items handed in a FIFO order
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    # Add item to front of the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    # Remove last item of queue
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


queue = Queue()
sold = simulate_line(5, 1)
print(sold)
