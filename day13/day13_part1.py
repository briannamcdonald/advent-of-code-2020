def main():
    data = open("day13/input.txt", "r")
    data = [line.strip() for line in data]
    estimate = int(data[0])
    bus_list = set(data[1].split(","))
    bus_list.remove("x")

    time_list = []
    for bus in bus_list:
        bus = int(bus)
        time = 0
        while time <= estimate:
            time += bus
        if time < estimate:
            time += bus
        time_list.append({"time": time - estimate, "bus_id": bus})

    lowest_time = 1000000
    for dictionary in time_list:
        if dictionary.get("time") < lowest_time:
            lowest_time = dictionary.get("time")
            best_bus = dictionary.get("bus_id")
    print(best_bus * lowest_time)


if __name__ == "__main__":
    main()