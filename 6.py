# Write a function to find the rectangular intersection of two given love rectangles.

# They are defined as dictionaries like this:
#
#   my_rectangle = {
#
#     # coordinates of bottom-left corner
#     'left_x': 1,
#     'bottom_y': 5,
#
#     # width and height
#     'width': 10,
#     'height': 4,
#
# }
#
# Your output rectangle should use this format as well.

def get_rectangle(left_x, bottom_y, width, height):
    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height
    }

def get_start_range(a1,l1,b1,l2):
    highest_begin = max(a1, b1)
    lowest_end = min(a1+l1, b1+l2)
    if highest_begin >= lowest_end:
        return None, None
    else:
        return highest_begin, lowest_end - highest_begin

def get_intersect(rec_1, rec_2):
    left_x, width = get_start_range(rec_1['left_x'], rec_1['width'],
                                    rec_2['left_x'], rec_2['width'])
    bottom_y, height = get_start_range(rec_1['bottom_y'], rec_1['height'],
                                       rec_2['bottom_y'], rec_2['height'])
    return get_rectangle(left_x, bottom_y, width, height)


rec_1 = get_rectangle(0,0, 100, 100)
rec_2 = get_rectangle(15, 20, 7, 10)
print "%s" % get_intersect(rec_1, rec_2)
