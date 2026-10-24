def vacuum_cleaner():
    rooms = {'A': 'Dirty', 'B': 'Dirty'}
    position = 'A'

    while 'Dirty' in rooms.values():
        print("Vacuum at", position)
        if rooms[position] == 'Dirty':
            rooms[position] = 'Clean'
            print(position, "cleaned")

        position = 'B' if position == 'A' else 'A'

    print("All rooms are clean")
    print(rooms)

vacuum_cleaner()