# in-flight entertainment with video on demand

def are_flight_time_movies_present(flight_length, movie_lengths):
    u_set = set()
    for length in movie_lengths:
        if length in u_set:
            return True
        else:
            u_set.add(flight_length - length)
    return False

test_1 = 60, [10, 20, 30, 40, 50, 60]
test_2 = 120, [10, 20, 30, 40, 50, 60]
test_3 = 20, [10, 20, 30, 40, 50, 60]

print are_flight_time_movies_present(test_1[0], test_1[1])
print are_flight_time_movies_present(test_2[0], test_2[1])
print are_flight_time_movies_present(test_3[0], test_3[1])
