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


#
#
#
#
##########



def get_rectangle(left_x, bottom_y, width, height):
    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height
    }

def get_recatangle_with_smaller_dimension(rec_1, rec_2, key):
    if rec_1[key] <= rec_2[key]:
        return rec_1, rec_2
    else:
        return rec_2, rec_1

def get_dimension_start_height_or_width(a1,a2,b1,b2):
    if a2 <= b1:
        raise Exception("No Intersection!")
    elif a2 <= b2:
        return b1, a2 - b1
    else:
        return b1, b2 - b1

def get_coordinates(dim_key1, dim_key2, small_rec, big_rec):
    a1 = small_rec[dim_key1]
    a2 = a1 + small_rec[dim_key2]
    b1 = big_rec[dim_key1]
    b2 = b1 + big_rec[dim_key2]
    return a1, a2, b1, b2

def get_intersect(rectangle_1, rectangle_2):
    (smaller_x_rectangle,
     bigger_x_rectangle) = get_recatangle_with_smaller_dimension(rectangle_1, rectangle_2, 'left_x')
    (smaller_y_rectangle,
     bigger_y_rectangle) = get_recatangle_with_smaller_dimension(rectangle_1, rectangle_2, 'bottom_y')

    a1, a2, b1, b2 = get_coordinates('left_x',
                                      'width',
                                      smaller_x_rectangle,
                                      bigger_x_rectangle)
    left_x, width = get_dimension_start_height_or_width(a1, a2, b1, b2)

    a1, a2, b1, b2 = get_coordinates('bottom_y',
                                     'height',
                                     smaller_y_rectangle,
                                     bigger_y_rectangle)
    bottom_y, height = get_dimension_start_height_or_width(a1, a2, b1, b2)
    return get_rectangle(left_x, bottom_y, width, height)


rec_1 = get_rectangle(0,0, 100, 100)
rec_2 = get_rectangle(15, 20, 7, 10)
print "%s" % get_intersect(rec_1, rec_2)
