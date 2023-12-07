def calculate_winning_ways(times, record_distances):
    """
    Calculate the number of winning ways for each race and return the product of these numbers.
    """
    # if times or record is not an array make it one
    if type(times) != list:
        times = [times]
    if type(record_distances) != list:
        record_distances = [record_distances]

    def winning_ways_for_race(time, record_distance):
        # Count the number of ways to beat the record for a single race
        count = 0
        for hold_time in range(time + 1):
            travel_time = time - hold_time
            distance = hold_time * travel_time
            if distance > record_distance:
                count += 1
        return count

    # Calculate for each race and multiply the results
    total_ways = 1
    for time, record_distance in zip(times, record_distances):
        total_ways *= winning_ways_for_race(time, record_distance)

    return total_ways


def main():
    filename = "day6input.txt"

    with open(filename, "r") as file_object:
        for line in file_object:
            # Get seeds
            if line.startswith("Time"):
                time = [int(n) for n in line.strip().split(": ")[1].split()]
            if line.startswith("Distance"):
                distance = [int(n) for n in line.strip().split(": ")[1].split()]

                data = {time[i]: distance[i] for i in range(len(time))}
        print(calculate_winning_ways(time, distance))


def main2():
    filename = "day6input.txt"

    with open(filename, "r") as file_object:
        for line in file_object:
            if line.startswith("Time"):
                times = line.split()[1:]
                time = int("".join(times))
            if line.startswith("Distance"):
                distances = line.split()[1:]
                distance = int("".join(distances))

        print(distance)

        print(calculate_winning_ways(time, distance))


if __name__ == "__main__":
    main2()
