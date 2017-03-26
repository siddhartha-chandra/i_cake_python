# Your company built an in-house calendar tool called HiCal.
# You want to add a feature to see the times in a day when everyone is available

# To do this, you’ll need to know when any team is having a meeting.
# In HiCal, a meeting is stored as tuples ↴ of integers (start_time, end_time)
# These integers represent the number of 30-minute blocks past 9:00am.
#
# For example:
# (2, 3) # meeting from 10:00 – 10:30 am
# (6, 9) # meeting from 12:00 – 1:30 pm

# Write a function merge_ranges() that takes a list of meeting time ranges and
# returns a list of condensed ranges.
# For example, given:
#   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# your function would return:
#   [(0, 1), (3, 8), (9, 12)]

def merge(x, y):
    if type(x) == type(y):
        if x[1] >= y[0]:
            res = [(x[0], max(x[1], y[1]))]
        else:
            res = [x, y]
    else:
        if x[-1][1] >= y[0]:
            x[-1] = (x[-1][0], max(x[-1][1], y[1]))
            res = x
        else:
            res = x + [y]
    return res

def merge_ranges(ls):
    sorted_tups = sorted(ls) # [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
    res = reduce(merge, ls)
    return res

def merge_ranges_original(meetings):
# sort by start times
sorted_meetings = sorted(meetings)
# initialize merged_meetings with the earliest meeting
merged_meetings = [sorted_meetings[0]]
for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
    last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
    # if the current and last meetings overlap, use the latest end time
    if (current_meeting_start <= last_merged_meeting_end):
        merged_meetings[-1] = (
            last_merged_meeting_start,
            max(last_merged_meeting_end, current_meeting_end))
    # add the current meeting since it doesn't overlap
    else:
        merged_meetings.append((current_meeting_start, current_meeting_end))
return merged_meetings


meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
print merge_ranges(meetings)
