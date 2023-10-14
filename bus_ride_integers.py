def number():

    bus_stops = [[10, 0], [3, 5], [5, 8]]
    print("HELLO")
    print(bus_stops[0][1])
    print(len(bus_stops))

    embarkers = []
    departures = []

    for each in range(0, len(bus_stops)):
        embarkers.append(bus_stops[each][0])
        departures.append(bus_stops[each][1])

    print(sum(embarkers))

    return sum(embarkers) - sum(departures)

# You can enter your array like this: array[i][j]


number()
