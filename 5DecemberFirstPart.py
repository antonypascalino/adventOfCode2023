
def get_map(puzzle_map):
    while True:
        puzzle_input = input()
        if puzzle_input == "":
            break

        curr_line = []
        curr_number = ""
        for character in puzzle_input:
            if character == " ":
                curr_line.append(int(curr_number))
                curr_number = ""
            elif character.isdigit():
                curr_number += character
        curr_line.append(int(curr_number))
        puzzle_map.append(curr_line)


def find_mapped_value(number, current_map):
    value = 0
    for line in current_map:
        if line[1] <= number < line[1] + line[2]:
            value = number + (line[0] - line[1])
            return value
        value = number
    return value


user_input = input()
user_input = user_input.split(":")[1]
seeds = []

curr_seed = ""

# Read all the seed integers
for char in user_input:
    if char == " " and curr_seed != "":
        seeds.append(int(curr_seed))
        curr_seed = ""
    elif char.isdigit():
        curr_seed += char
seeds.append(int(curr_seed))

input()
input()
seed_to_soil_map = []
get_map(seed_to_soil_map)

input()
soil_to_fertilizer_map = []
get_map(soil_to_fertilizer_map)

input()
fertilizer_to_water_map = []
get_map(fertilizer_to_water_map)

input()
water_to_light_map = []
get_map(water_to_light_map)

input()
light_to_temperature_map = []
get_map(light_to_temperature_map)

input()
temperature_to_humidity_map = []
get_map(temperature_to_humidity_map)

input()
humidity_to_location_map = []
get_map(humidity_to_location_map)

locations = []
for seed in seeds:
    soil = find_mapped_value(seed, seed_to_soil_map)
    fertilizer = find_mapped_value(soil, soil_to_fertilizer_map)
    water = find_mapped_value(fertilizer, fertilizer_to_water_map)
    light = find_mapped_value(water, water_to_light_map)
    temperature = find_mapped_value(light, light_to_temperature_map)
    humidity = find_mapped_value(temperature, temperature_to_humidity_map)
    location = find_mapped_value(humidity, humidity_to_location_map)

    locations.append(location)

print(min(locations))
