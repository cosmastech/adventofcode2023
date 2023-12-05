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

_REAL_INPUT = """seeds: 3121711159 166491471 3942191905 154855415 3423756552 210503354 2714499581 312077252 1371898531 165242002 752983293 93023991 3321707304 21275084 949929163 233055973 3626585 170407229 395618482 226312891

seed-to-soil map:
522866878 679694818 556344137
1206934522 1236038955 57448427
2572695651 3529213882 270580892
1082547209 29063229 124387313
2080101996 2392534586 180161065
1079211015 153450542 3336194
2466695431 2286534366 106000220
1887791814 2094224184 192310182
2843276543 2572695651 956518231
2341707296 1887791814 124988135
1264382949 156786736 473875833
67220304 1331644457 455646574
3903217571 3799794774 267521683
2260263061 2012779949 81444235
1738258782 630662569 49032249
29063229 1293487382 38157075
3799794774 4067316457 103422797

soil-to-fertilizer map:
69994133 1665188283 300635345
0 1965823628 36826481
2222587532 2553838094 476943506
2929387922 3030781600 856348250
4182440411 2441311209 112526885
36826481 2002650109 33167652
2044606970 4116986734 177980562
1815516279 549395220 220301482
1186435707 0 549395220
916609638 1315676862 269826069
3785736172 2044606970 396704239
2699531038 3887129850 229856884
1735830927 1585502931 79685352
370629478 769696702 545980160

fertilizer-to-water map:
2485494684 3430237839 78539769
2045426403 2253341567 99573285
290571869 0 280695139
3540352207 2045426403 63912525
2879366909 3356847577 67075608
868611408 858081124 224160766
2304858397 2525185867 55003581
189640733 280695139 100931136
2144999688 3983682880 159858709
3374818325 3858616265 14108175
3604264732 2580189448 427645906
1730244179 535856806 2894582
4242091162 3634410314 52876134
4031910638 3872724440 110958440
1092772174 1116784935 90115688
1182887862 381626275 154230531
4149183732 3263940147 92907430
4142869078 3423923185 6314654
571267008 728392121 129689003
3315918322 2352914852 58900003
2359861978 3508777608 125632706
2735364270 2109338928 144002639
2946442517 2411814855 113371012
1733138761 1082241890 34543045
700956011 1600026409 167655397
3059813529 3041876971 222063176
2564034453 3687286448 171329817
3281876705 3007835354 34041617
0 538751388 189640733
3388926500 4143541589 151425707
1337118393 1206900623 393125786

water-to-light map:
66525849 932008802 34502691
1231709999 161981088 108836128
4050378444 3046032039 195065028
1188304980 324179540 43405019
0 95455239 66525849
1134942656 270817216 53362324
4015087939 2401779423 35290505
3174436586 2144628864 257150559
3688283374 3968162731 326804565
101028540 367584559 564424243
665452783 23428765 72026474
2144628864 2437069928 302742058
1340546127 0 23428765
737479257 1714174561 397463399
3431587145 2789335810 256696229
4245443472 2739811986 49523824
1363974892 966511493 747663068
2447370922 3241097067 727065664

light-to-temperature map:
3188351957 4202865263 58820659
583430260 717912118 192120954
1044551258 2246397764 71032709
3109547837 4261685922 33281374
1678878772 1586709546 87694921
1115583967 3604496785 152969541
3142829211 2200875018 45522746
2103724421 1412959073 173750473
3094755823 2836912864 14792014
4233716778 2851704878 61250518
1809783323 3254776949 293941098
570222212 2097755032 13208048
34744215 693464 72237295
1773265141 2502078476 36518182
775551214 4072807084 98261716
2718819720 511651563 117721319
873812930 4171068800 31796463
905609393 3933865219 138941865
373474927 3892288779 41576440
3040218555 3117948789 54537268
2397118702 2538596658 1887839
0 72930759 34744215
2277474894 1316613368 93303271
370955311 1409916639 2519616
1359408316 3757466326 134822453
2370778165 306806837 1167210
220512052 1412436255 522818
3335711852 1674404467 423350565
335173455 2743397480 35781856
3900016435 982913025 333700343
2399006541 2540484497 202912983
3816795945 2110963080 83220490
415051367 910033072 72879953
2663040982 3548718047 55778738
3759062417 2779179336 57733528
3247172616 629372882 88539236
1494230769 2317430473 184648003
1766573693 2194183570 6691448
2601919524 245685379 61121458
2371945375 220512052 25173327
221034870 3003810204 114138585
2836541039 307974047 203677516
487931320 3172486057 82290892
106981510 0 693464
1268553508 2912955396 90854808

temperature-to-humidity map:
1844491325 2716144828 118858329
1004942401 2971501799 229549152
696973964 238546929 19842755
716816719 119302258 119244671
444146335 2339344684 80152617
3752420807 853580623 112964826
3736479208 2933101125 15941599
1822411864 805752927 11014046
3183816206 2835003157 98097968
3538508914 2576089466 88076349
1833425910 816766973 11065415
3865385633 2664165815 51979013
1706894195 1592117663 89769434
2892814110 3354360228 291002096
2450334080 3645362324 65003481
3934652728 3721018678 66888233
3285923313 2419497301 85776839
3917364646 2257358228 17288082
3371700152 2090549466 166808762
524298952 633077915 172675012
1600852292 966545449 106041903
2283983708 620036820 13041095
2176983704 2274646310 64698374
2515337561 1072587352 32448957
846714263 1105036309 42935019
3719859664 603417276 16619544
2547786518 258389684 345027592
0 1147971328 444146335
1963349654 3787906911 213634050
836061390 3710365805 10652873
889649282 0 115293119
2241682078 1681887097 42301630
3281914174 115293119 4009139
2297024803 3201050951 153309277
1796663629 827832388 25748235
3626585263 2505274140 70815326
1234491553 1724188727 366360739
3697400589 2949042724 22459075

humidity-to-location map:
3693038281 1946208152 169064741
3025397429 1673895501 272312651
2522027478 1111558812 503369951
3862103022 3729735566 432864274
1111558812 2115272893 1374715990
3356676818 3489988883 239746683
3297710080 1614928763 58966738
2486274802 4162599840 35752676
3596423501 4198352516 96614780"""


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