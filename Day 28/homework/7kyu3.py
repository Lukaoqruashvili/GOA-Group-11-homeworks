def number(bus_stops):
    people = 0
    
    for entered, off in bus_stops:
        people += entered
        people -= off

    return people