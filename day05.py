import sys

_STARTING_NUMBER = 1
_EXAMPLE_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

_REAL_INPUT = """---snip---"""


def parse_numbers_from_line(s: str) -> list[list[int]]:
    o = []
    lines = s.splitlines()[1:]
    for line in lines:
        p = [int(s) for s in line.split(' ') if len(s) > 0]
        o.append(p)

    return o


def array_of_arrays_to_dict(arr: list) -> dict:
    o = {}
    for a in arr:
        destination_start = a[0]
        source_start = a[1]
        count = a[2]

        for i in range(0, count):
            dest_value = destination_start + i
            source_value = source_start + i
            o[source_value] = dest_value
    return o


def array_of_arrays_to_list_of_dicts(arr: list):
    o = []
    for a in arr:
        destination_start = a[0]
        source_start = a[1]
        count = a[2]
        o.append({
            'source_range': range(source_start, source_start+count),
            'source_start': source_start,
            'destination_start': destination_start
        })
    return o
def parse_input(input_str: str) -> dict:
    chunks = [l for l in input_str.split("\n\n") if len(l) > 0]

    seeds = []
    for chunk in chunks:
        if "seeds:" in chunk:
            l = chunk.split('seeds: ')[1]
            seeds = [int(s) for s in l.split(' ') if len(s) > 0]
            continue
        if "seed-to-soil map:" in chunk:
            seed_to_soil = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue
        if "soil-to-fertilizer map:" in chunk:
            soil_to_fertilizer = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue
        if "fertilizer-to-water map:" in chunk:
            fertilizer_to_water = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue
        if "water-to-light map:" in chunk:
            water_to_light = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue
        if "light-to-temperature map:" in chunk:
            light_to_temperature = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue
        if "temperature-to-humidity map:" in chunk:
            temperature_to_humidity = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue
        if "humidity-to-location map:" in chunk:
            humidity_to_location = array_of_arrays_to_list_of_dicts(parse_numbers_from_line(chunk))
            continue

    return {
        "seeds": seeds,
        "seed_to_soil": seed_to_soil,
        "soil_to_fertilizer": soil_to_fertilizer,
        "fertilizer_to_water": fertilizer_to_water,
        "water_to_light": water_to_light,
        "light_to_temperature": light_to_temperature,
        "temperature_to_humidity": temperature_to_humidity,
        "humidity_to_location": humidity_to_location
    }

def input_to_output(input_value: int, mappings: dict, key: str) -> int:
    target_mapping = mappings[key]

    for potential_range_dict in target_mapping:
        if input_value in potential_range_dict['source_range']:
            diff = input_value - potential_range_dict['source_start']
            return potential_range_dict['destination_start'] + diff

    return input_value

def take_seed_to_location(seed: int, mappings: dict) -> int:
    list = [
        #'seed_range',
        'seed_to_soil',
        'soil_to_fertilizer',
        'fertilizer_to_water',
        'water_to_light',
        'light_to_temperature',
        'temperature_to_humidity',
        'humidity_to_location'
    ]

    v = seed
    for key in list:
        #print('start v: ' + str(v))
        #print('key: ' + str(key))
        v = input_to_output(v, mappings, key)
        #print('ending v: ' + str(v))

    return v

def part1(input_str: str):
    d = parse_input(input_str)
    print(d)
    location_list = []
    for seed in d['seeds']:
        location = take_seed_to_location(seed, d)
        location_list.append(location)
        print('seed: ' + str(seed) + ' location: ' + str(location))

    print(min(location_list))

def part2(input_str: str) -> None:
    d = parse_input(input_str)
    location_list = []
    split_arrays = [d['seeds'][i:i+2] for i in range(0, len(d['seeds']), 2)]

    minimum_location = sys.maxsize
    idx = -1
    for pair in split_arrays:
        idx += 1
        if idx < _STARTING_NUMBER:
            continue
        starting_value = pair[0]
        ending_value = pair[1] + starting_value

        for seed in range(starting_value, ending_value):
            location = take_seed_to_location(seed, d)
            #print('location: ' + str(location))
            if (location < minimum_location):
                minimum_location = location
                print("New minimum location: " + str(minimum_location))
            #location_list.append(location)
            #print('seed: ' + str(seed) + ' location: ' + str(location))

        print("finished pair")

    print(minimum_location)
    #print(min(location_list))

if __name__ == '__main__':
    # didn't want to start with the actually parallelizing the code, so I just spun up terminals for each pair and changed the starting number for the seed index
    # I think it would've made sense to take each range and create a set of those values, that way we were never processing the same values
    # Not sure if there's a better approach that brute force... but eventually we got the right answer.
    _STARTING_NUMBER=9
    part2(_REAL_INPUT)


"""
Minimums:
- 316960383
- 120582180 <-- smaller than this
- 51399228
- 1241009111
- 972973391
- 972973391
- 642320287
- 535088217
- 2865447566
"""
