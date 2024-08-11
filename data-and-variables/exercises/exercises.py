shuttle name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 38400
MILES_PER_KM = 0.621
print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(MILES_PER_KM))
miles_to_mars = distances_to_mars * MILES_PER_KM
hours_to_mars = miles_to_mars / shuttle_speed_mph 
days_to_mars = hours_to_mars / 24
print(shuttle_name + " will take " + days_to_moon + " days to reach the Moon. ")


# Code your solution to exercise 5 here
