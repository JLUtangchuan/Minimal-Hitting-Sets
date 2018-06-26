import itertools

all_observations = []
HS = []


# Öffnet die Textdatei, liest Zeile für Zeile ein und schließt die Datei
def read_data():
    data_file = open("observation_mix.txt", "r")
    for line in data_file:
        # entfernt den Doppelpunkt und erstellt ein sender_set/receiver_set
        # diese werden als eine Observation in die all_observations Liste gespeichert
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


# speichert die Empfängermengen des übergebenen Senders in sender_observations
def return_observations_with_specific_sender(sender):
    sender_observations = []
    for observation in all_observations:
        if sender in observation[0]:
            sender_observations.append(observation[1])
    return sender_observations


# berechnet alle Minimal Hitting-Sets der Größe <= m in KB
def exact_hs(KB, m, C):
    if not KB:
        HS.append(C)
    elif m >= 1:
        B = KB[0]
        index_of_observation = 0
        while (len(KB) > 0) & (len(B) >= 1) & (index_of_observation >= 0) & (index_of_observation < 4):
            r = B[index_of_observation]
            exact_hs(get_subset_of_observations_without_r(KB, r), m - 1, C + [r])
            index_of_observation += 1


# gibt eine Liste zurück, die alle Beobachtungen aus dem superset enthält, die r nicht enthalten
def get_subset_of_observations_without_r(superset, r):
    subset = []
    for observation in superset:
        if r not in observation:
            subset.append(observation)
    return subset


# entfernt Duplikate
def remove_duplicates_from_mhs(minimal_hitting_sets):
    return list(minimal_hitting_sets for minimal_hitting_sets, _ in itertools.groupby(minimal_hitting_sets))


# sortiert Listen in globaler Variable HS
def sort_mhs():
    for mhs in HS:
        mhs.sort()


# Funktionsaufruf zum Starten des ExactHS Algorithmuses
def start_hs_attack():
    # HS global zum abspeichern definieren
    global HS
    # iteriert über Sender und gibt alle entsprechenden Sendermengen in den exact_hs Algorithmus
    # falls exact_hs terminiert wird m um eins erhöht und so lange wiederholt, bis HS nicht mehr leer ist
    for i in range(1, 11):
        HS = []
        KB = return_observations_with_specific_sender(i)
        m = 1
        while not HS:
            exact_hs(KB, m, [])
            m = m + 1
        sort_mhs()
        HS = remove_duplicates_from_mhs(HS)
        print("Minimal Hitting Set for Sender " + str(i) + " (m = " + str(m-1) + ")" + ": " + str(HS))

# Funktionsaufrufe
read_data()
start_hs_attack()

