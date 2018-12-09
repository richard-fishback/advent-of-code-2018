from collections import defaultdict
from dataclasses import dataclass, field
from re import match
import heapq


@dataclass(order=True)
class Order:
    priority: (int, str) = field(default=(0, ''))
    remaining: int = field(default=0, compare=False)
    needs: list = field(default_factory=list, compare=False)
    needed_by: list = field(default_factory=list, compare=False)


def get_orders():
    orders = defaultdict(Order)
    with open('input.txt') as lines:
        for line in lines:
            src, dest = match(r'Step (.+) must be finished before step (.+) can begin.', line).groups()
            orders[dest].needs.append(src)
            orders[dest].priority = (orders[dest].priority[0] + 1, dest)
            orders[dest].remaining = ord(dest) - ord('A') + 61
            orders[src].priority = (orders[src].priority[0], src)
            orders[src].needed_by.append(dest)
            orders[src].remaining = ord(src) - ord('A') + 61
    return orders


def get_queue(orders):
    priority_queue = [order for order in orders.values()]
    heapq.heapify(priority_queue)
    queue_lookup = {order.priority[-1]: order for order in orders.values()}
    return priority_queue, queue_lookup


def zero_work_order(orders):
    priority_queue, queue_lookup = get_queue(orders)
    while priority_queue:
        q_item = heapq.heappop(priority_queue)
        yield q_item.priority[-1]
        for c in q_item.needed_by:
            queue_lookup[c].needs.remove(q_item.priority[-1])
            queue_lookup[c].priority = (queue_lookup[c].priority[0] - 1, c)
        heapq.heapify(priority_queue)


print(f'''Part One: {''.join(zero_work_order(get_orders()))}''')


def timed_work_order(orders, num_workers=5):
    priority_queue, queue_lookup = get_queue(orders)
    workers = []
    time = 0
    while priority_queue or workers:
        while priority_queue and len(workers) < num_workers and priority_queue[0].priority[0] == 0:
            workers.append(heapq.heappop(priority_queue))
        for worker in workers:
            worker.remaining -= 1
            if worker.remaining == 0:
                for c in worker.needed_by:
                    queue_lookup[c].needs.remove(worker.priority[-1])
                    queue_lookup[c].priority = (queue_lookup[c].priority[0] - 1, c)
        workers = [worker for worker in workers if worker.remaining > 0]
        heapq.heapify(priority_queue)
        time += 1
    return time


print(f'''Part Two: {timed_work_order(get_orders())}''')
