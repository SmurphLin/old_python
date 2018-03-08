j = 0
added_roads =[]
while j < 3:
    roads = [[0, 1], [1, 2], [2, 0]]
    cities = [i for i in range(4)]
    the_city = cities[j]                                                     # v[0] initial
    cities.remove(the_city)                                                  # cities = [1,2,3]
    connected_cities = []
    r = 0
    while r != len(roads):
        if the_city in roads[r] and r != len(roads) - 1:                      # if 0 is [0,1]
            hold = roads[r]                                                   # hold = [0,1]
            hold.remove(the_city)                                             # hold = [1]
            connected_cities.append(hold[0])                                  # ERROR aFIXED
            cities.remove(hold[0])                                            # cities = [2,3]
            r += 1                                                            # roads[r] = [1,2]
        elif the_city not in roads[r] and r != len(roads) - 1:
            r += 1
        elif r == len(roads)-1 and the_city in roads[r]:
            hold = roads[r]
            hold.remove(the_city)
            connected_cities.append(hold[0])
            cities.remove(hold[0])
        else:
            for i in range(len(cities)):
                missing_road = cities[i]
                input_list =[the_city,missing_road]
                added_roads.append(input_list)
            r += 1
            j += 1



print added_roads


def roadsBuilding(cities, roads):
    j = 0
    added_roads = []
    flatten = [i
               for i in range(len(roads))
               for j in range(len(roads[i]))
              ]
    set_flatten = set(flatten)
    list_set_flatten = list(set_flatten)

    while j < len(list_set_flatten):
        roads_list = roads
        cities_list = [i for i in range(cities)]
        current_city = cities_list[j]
        cities_list.remove(current_city)
        connected_cities = []
        r = 0
        while r != len(roads_list):
            if current_city in roads_list[r] and r != len(roads_list)-1:
                hold = roads_list[r]
                hold.remove(current_city)
                connected_cities.append(hold[0])
                cities_list.remove(hold[0])
                r += 1
            elif current_city not in roads_list[r] and r != len(roads_list)-1:
                r += 1
            elif r == len(roads_list)-1 and current_city in roads_list[r]:
                hold = roads_list[r]
                hold.remove(current_city)
                connected_cities.append(hold[0])
                cities_list.remove(hold[0])
            else:
                for i in range(len(cities_list)):
                    missing_road = cities_list[i]
                    input_list = [current_city,missing_road]
                    added_roads.append(input_list)
                    r += 1
                    j += 1

    return added_roads


print roadsBuilding(4,[[0, 1], [1, 2], [2, 0]])
