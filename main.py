import itertools

all_observations = []
sender_observations = []
HS = []

def read_data():
    data_file = open("observation_mix.txt", "r")
    for line in data_file:
        removed_colon = line.replace(":", "").replace("  ", " ")
        value1, value2, value3, value4, value5, value6, value7, value8, value9 = removed_colon.split(" ")
        value1 = int(value1)
        value2 = int(value2)
        value3 = int(value3)
        value4 = int(value4)
        value5 = int(value5)
        value6 = int(value6)
        value7 = int(value7)
        value8 = int(value8)
        sender_set = [value1, value2, value3, value4]
        receiver_set = [value5, value6, value7, value8]
        observation = [sender_set, receiver_set]
        all_observations.append(observation)
    data_file.close()


def return_observations_with_specific_sender(sender):
    for observation in all_observations:
        if sender in observation[0]:
            sender_observations.append(observation[1])


def exact_hs(KB, m, C):
    if not KB:
        print("hello")
        C.sort()
        HS.append(C)
    elif m >= 1:
        B = KB[0]
        index_of_observation = 0
        while (len(KB) > 0) & (len(B) >= 1) & (index_of_observation >= 0) & (index_of_observation < 4):
            r = B[index_of_observation]
            exact_hs(get_subset_of_observations_without_r(KB, r), m - 1, C + [r])
            index_of_observation += 1
            print(index_of_observation)


def get_subset_of_observations_without_r(superset, r):
    subset = []
    for observation in superset:
        if r not in observation:
            subset.append(observation)
    return subset


def remove_duplicates_from_mhs(minimal_hitting_sets):
    return list(minimal_hitting_sets for minimal_hitting_sets, _ in itertools.groupby(minimal_hitting_sets))


def start_hs_attack():
    global HS
    KB = sender_observations
    m = 1
    while not HS:
        exact_hs(KB, m, [])
        m = m + 1
    HS = remove_duplicates_from_mhs(HS)
    print(HS)


read_data()
return_observations_with_specific_sender(10)
start_hs_attack()

