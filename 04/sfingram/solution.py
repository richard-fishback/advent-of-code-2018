from datetime import datetime
from re import match
from dataclasses import dataclass
from collections import defaultdict
from itertools import groupby

DATE_FORMAT = '%Y-%m-%d %H:%M'


@dataclass
class GuardShift:
    id: int
    date: datetime
    new_shift: bool = False
    sleep: bool = False
    wake: bool = False


def line_key(line):
    return datetime.strptime(match(r'\[(.+)\] .+', line).groups()[0], DATE_FORMAT)


def get_shift(entry, id=None):
    if match(r'.+ falls asleep', entry):
        return GuardShift(id=id, date=line_key(entry), sleep=True)
    elif match(r'.+ wakes up', entry):
        return GuardShift(id=id, date=line_key(entry), wake=True)
    new_id = int(match(r'.+ Guard #(\d+) begins shift', entry).groups()[0])
    return GuardShift(id=new_id, date=line_key(entry), new_shift=True)


def get_shifts(lines):
    last_id = None
    for entry in sorted((line for line in lines), key=line_key):
        shift = get_shift(entry, last_id)
        last_id = shift.id
        yield shift


def get_max_minute(sleep_counts, id):
    if not sleep_counts[id].items():
        return (0, 0)
    return sorted(sleep_counts[id].items(), key=lambda x: x[-1])[-1]


with open('input.txt') as fin:
    SHIFTS = list(get_shifts(fin))
sleep_counts = {id: defaultdict(int)
                for id in set(shift.id for shift in SHIFTS)}
for g, sleeps in groupby((shift for shift in SHIFTS if not shift.new_shift),
                         key=lambda x: (x.id, x.date.month, x.date.day)):
    for sleep in sleeps:
        wake = next(sleeps)
        for minute in range(sleep.date.minute, wake.date.minute):
            sleep_counts[g[0]][minute] += 1

most_sleep = sorted(((k, sum(v.values())) for k, v in sleep_counts.items()),
                    key=lambda x: x[1])[-1][0]
most_hour = get_max_minute(sleep_counts, most_sleep)[0]
print(f'Part One: {most_sleep*most_hour}')

most_freq = sorted([(k, get_max_minute(sleep_counts, k))
                    for k in sleep_counts], key=lambda x: -x[-1][-1])[0]
print(f'Part Two: {most_freq[0] * most_freq[-1][0]}')
