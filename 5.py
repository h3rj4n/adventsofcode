from enum import Enum
from itertools import chain
import re

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
            if len(seeds) <= 0:
                continue
            for seed_id in chain(range(seeds[0], seeds[0] + seeds[1]), range(seeds[2], seeds[2] + seeds[3])):
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

print(build)

l = [s[ToMap.HUMIDITY_TO_LOCATION] for s in build]
print("Answer 2:", min(l))
            

