import numpy as np
import re

a = sorted([x for x in open('input.txt')])
numdays = sum([1 for x in a if "Guard" in x])
print("rows: "+str(len(a))+" days: " + str(numdays))

days_index = {} # don't need this yet....
guards_day = np.zeros([numdays,1])
sleep_logs = np.zeros([numdays,60])
i = -1
current_guard = 0
asleep = 0
# iterate a, get relevant data
for line in a:
    if "Guard" in line:
        i+=1
        current_guard = re.match(".*#(\d+) begins.*",line).group(1)
        # for a first pass, assume that guards start awake at midnight, sleep at least once
        guards_day[i] = current_guard
    elif "asleep" in line:
        minute = int(re.match('.*:(\d+)\].*',line).group(1))
        sleep_logs[i,minute:] = np.ones([1,60-minute])
    elif "wakes" in line:
        minute = int(re.match('.*:(\d+)\].*',line).group(1))
        sleep_logs[i,minute:] = np.zeros([1,60-minute])
    else:
        print("invalid row encountered\n")

# now just get sum of guards's sleep time
sleepiest_guard = 0
most_sleep = 0
for guard in np.unique(guards_day):
    #this_sleep = sum(sum(sleep_logs[guards_day==guard,:]))
    this_sleep = sum([sum(sleep_logs[i,:]) for i,g in enumerate(guards_day) if g == guard])
    if this_sleep > most_sleep:
        most_sleep = this_sleep
        sleepiest_guard = guard
print("sleepiest guard: " + str(sleepiest_guard))

# what was his sleepiest minute?
#sleepiest_minute = sum(sleep_logs[guards_day==sleepiest_guard])
# i am having the sleepiest_minute here. this code is bad and I am bad.
hour = np.zeros([1,60])
for i,guard in enumerate(guards_day):
    if guard == sleepiest_guard:
        hour += sleep_logs[i,:]
print("sleepiest minute: " + str(np.argmax(hour)))
print("answer part 1: " + str(sleepiest_guard*np.argmax(hour)))

# part 2 wants the guard with the single sleepiest minute.

sleepiest_minute_idx = 0
sleepiest_minute_amount = 0
sleepiest_minute_guard = 0
for current_guard in np.unique(guards_day):
    hour = np.zeros([1,60])
    for i, guard in enumerate(guards_day):
        if guard == current_guard:
            hour += sleep_logs[i,:]
    current_guard_max = np.amax(hour)
    if current_guard_max > sleepiest_minute_amount:
        sleepiest_minute_amount = current_guard_max
        sleepiest_minute_guard = current_guard
        sleepiest_minute_idx = np.argmax(hour)

print("answer part 2: " + str(sleepiest_minute_guard*sleepiest_minute_idx))


