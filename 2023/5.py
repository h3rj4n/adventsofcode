from enum import Enum
import re
import pprint

class ToMap(Enum):
    SEED = 'seeds'
    SEED_TO_SOIL = 'seed-to-soil'
    SOIL_TO_FERTILIZER = 'soil-to-fertilizer'
    FERTILIZER_TO_WATER = 'fertilizer-to-water'
    WATER_TO_LIGHT = 'water-to-light'
    LIGHT_TO_TEMPERATURE = 'light-to-temperature'
    TEMPERATURE_TO_HUMIDITY = 'temperature-to-humidity'
    HUMIDITY_TO_LOCATION = 'humidity-to-location'

current_step = ToMap.SEED

build = []

map_values = {
    ToMap.SEED_TO_SOIL: ToMap.SEED,
    ToMap.SOIL_TO_FERTILIZER: ToMap.SEED_TO_SOIL,
    ToMap.FERTILIZER_TO_WATER: ToMap.SOIL_TO_FERTILIZER,
    ToMap.WATER_TO_LIGHT: ToMap.FERTILIZER_TO_WATER,
    ToMap.LIGHT_TO_TEMPERATURE: ToMap.WATER_TO_LIGHT,
    ToMap.TEMPERATURE_TO_HUMIDITY: ToMap.LIGHT_TO_TEMPERATURE,
    ToMap.HUMIDITY_TO_LOCATION: ToMap.TEMPERATURE_TO_HUMIDITY,
}

with open("5_data.txt") as f:
    for line in f:
        if 'map:' in line:
            for search in ToMap:
                if search.value in line:
                    current_step = search

        if (current_step == ToMap.SEED):
            # Extract all the seeds
            m = re.findall(r"([0-9]+)", line)
            seeds = [int(n) for n in m]
            for seed_id in seeds:
                s = {}
                # @todo Default to own ID on the entire list?
                for search in ToMap:
                    s[search] = seed_id
                build.append(s)
            continue

        if current_step not in map_values:
            continue

        data = [int(n) for n in re.findall(r"([0-9]+)", line)]
        if data:
            l = [s[map_values[current_step]] for s in build]
            for index, number in enumerate(l):
                if int(data[1]) <= number <= int(data[1]) + int(data[2]):
                    # print(data[0] + (int(data[1]) - number))
                    build[index][current_step] = data[0] + (number - int(data[1]))
                    found = False
                    for search in ToMap:
                        if found:
                            build[index][search] = data[0] + (number - int(data[1]))
                        else:
                            found = search == current_step

l = [s[ToMap.HUMIDITY_TO_LOCATION] for s in build]
print("Answer 1:", min(l))

# Reset build.
build = []

current_step = ToMap.SEED
with open("5_data.txt") as f:
    for line in f:
        if 'map:' in line:
            for search in ToMap:
                if search.value in line:
                    current_step = search

        if (current_step == ToMap.SEED):
            # Extract all the seeds
            m = re.findall(r"([0-9]+)", line)
            seeds = [int(n) for n in m]
            for i in range(0, int(len(seeds) / 2)):
                s = {}
                for search in ToMap:
                    s[search.value] = [seeds[i * 2], seeds[i * 2] + seeds[(i * 2) + 1]]
                build.append(s)
            #     print(seeds[i * 2], seeds[(i * 2) + 1])
            #     print(i)
            # print(seeds)
#             if len(seeds) <= 0:
#                 continue
#             for seed_id in chain(range(seeds[0], seeds[0] + seeds[1]), range(seeds[2], seeds[2] + seeds[3])):
#                 s = {}
#                 # @todo Default to own ID on the entire list?
#                 for search in ToMap:
#                     s[search] = seed_id
#                 build.append(s)
#             continue

        if current_step not in map_values:
            continue

        data = [int(n) for n in re.findall(r"([0-9]+)", line)]
        if data:
            print(data)
            dest_range = [data[0], data[0] + data[2]]
            source_range = [data[1], data[1] + data[2]]
            print('line: ', source_range, dest_range, current_step.value)

            l = [s[map_values[current_step].value] for s in build]
            for index, number in enumerate(l):
                print(map_values[current_step].value, number, source_range)
                c = build[index].copy()
                # Left: Original source range is bigger, we need to split up.
                if number[0] < source_range[0] and number[1] > source_range[0]:
                    count = (source_range[0] - 1) - number[0]
                    print("count left", count)
                    value = [number[0], source_range[0] - 1] # Create new object.
                    c[map_values[current_step].value] = value
                    found = False
                    for search in ToMap:
                        if found:
                            c[search.value] = value
                        else:
                            found = search == current_step
                            if found is False:
                                c[search.value][1] = c[search.value][0] + count
                    print('append', current_step.value, value)
                    # print(c)
                    build.append(c)
                    build[index][current_step.value] = [source_range[0], number[1]]
                    build[index][map_values[current_step].value] = [source_range[0], number[1]]
                    number[0] = source_range[0]
                    # [source_range[0], number[1]] # Overwrite current object.

                # Right: Original source range is bigger, we need to split up.
                if number[1] > source_range[1] and number[0] < source_range[1]:
                    count = number[1] - (source_range[1] + 1)
                    print("count right", count)
                    value = [source_range[1] + 1, number[1]] # Create new object.
                    c[map_values[current_step].value] = value
                    found = False
                    for search in ToMap:
                        if found:
                            c[search.value] = value
                        else:
                            found = search == current_step
                            if found is False:
                                c[search.value][0] = c[search.value][1] - count
                    # print('t', map_values[current_step].value)
                    print('append', current_step.value, value)
                    # print(c)
                    build.append(c)
                    build[index][current_step.value] = [number[0], source_range[1]]
                    build[index][map_values[current_step].value] = [number[0], source_range[1]]
                    number[1] = source_range[1]

                    # [source_range[1] + 1, number[1]] # Create new object
                    # [number[0], source_range[1]] # Overwrite current object.

                # Now we have an object that fits the dest_range?
                if number[0] >= source_range[0] and number[1] <= source_range[1]:
                    value =  [dest_range[0] + number[0] - source_range[0], dest_range[1] + number[1] - source_range[1]]
                    build[index][current_step.value] = value
                # print(number)
#                 if int(data[1]) <= number <= int(data[1]) + int(data[2]):
#                     # print(data[0] + (int(data[1]) - number))
#                     build[index][current_step] = data[0] + (number - int(data[1]))
                    found = False
                    for search in ToMap:
                        if found:
                            build[index][search.value] = value
                        else:
                            found = search == current_step

                    print("match", value)
            print("\n")

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(build)

l = [s[ToMap.HUMIDITY_TO_LOCATION.value] for s in build]
pp.pprint(l)

# l = [s[ToMap.HUMIDITY_TO_LOCATION] for s in build]
# print("Answer 2:", min(l))


