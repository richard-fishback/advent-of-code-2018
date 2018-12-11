from datetime import datetime
from re import match
from collections import defaultdict, Counter
from operator import itemgetter

def process_input(input):
    for item in input:
        parts = match(r"\[(.+)\] (.+)", item).groups()
        yield {
            'timestamp': datetime.fromisoformat(parts[0]),
            'action': parts[1],
        }

def fall_asleep(start):
    def wake_up(end):
        return range(start,end)
    return wake_up

if __name__ == '__main__':
    input = [line for line in open('input.txt').readlines()]
    records = sorted([record for record in process_input(input)], key=lambda record: record['timestamp'])

    guards = {}
    guard = None
    nap = None
    for record in records:
        if "Guard" in record['action']:
            number = match(r"[A-z]+ #(\d+).+", record['action']).groups()[0]
            try:
                guard = guards[number]
            except KeyError:
                guards[number] = defaultdict(int)
                guard = guards[number]
        elif "asleep" in record['action']:
            nap = fall_asleep(record['timestamp'].minute)
        else:
            for minute in nap(record['timestamp'].minute):
                guards[number][minute] += 1

    sleepiest_guard = max([guard for guard in guards], key=lambda x:sum(guards[x]))
    print('solution 1:', int(sleepiest_guard) * Counter(guards[sleepiest_guard]).most_common(1)[0][0])
    frequent_guard = max([(guard, max(guards[guard].items(), key=itemgetter(1), default=(1,0))) for guard in guards], key=lambda x:x[1][1])
    print('solution 2:', int(frequent_guard[0]) * frequent_guard[1][0])
