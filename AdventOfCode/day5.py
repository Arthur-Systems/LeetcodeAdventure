def map_value(source_value, map_list):
    # calculate the destination value for a given source value
    for (
        destination_start,
        source_start,
        length,
    ) in map_list:  # if the source value is in the range
        if source_start <= source_value < source_start + length:
            # Calculate the offset from the start of the source range
            offset = source_value - source_start
            # Apply the same offset to the destination range
            return destination_start + offset
    # If the value doesn't match any range, it maps to itself
    return source_value


def process_seed(seed, mappings):
    """
    Process a seed through all mappings to find its final location number.
    """
    current_value = seed
    for mapping in mappings:
        current_value = map_value(current_value, mapping)
    return current_value


def main():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day5input.txt"
    )

    total_map = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    with open(filename, "r") as file_object:
        current_map = None
        for line in file_object:
            # Get seeds
            if line.startswith("seeds"):
                seeds = [int(n) for n in line.strip().split(": ")[1].split()]
                print("seeds:", seeds)
            elif "map" in line:
                current_map = line.strip().split()[0]
            elif current_map and line.strip():
                total_map[current_map].append([int(n) for n in line.strip().split()])

    print(total_map)

    processed_mappings = [
        total_map[key]
        for key in [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]
    ]
    location_numbers = [process_seed(seed, processed_mappings) for seed in seeds]

    print("Location numbers:", location_numbers)

    final_location = min(location_numbers)

    print("Final location:", final_location)


def process_range(start, length, mappings):
    location_numbers = []
    for seed in range(start, start + length):
        location_numbers.append(process_seed(seed, mappings))
    return min(location_numbers)


def main2():
    filename = (
        "/Users/arthur/Documents/GitHub/LeetcodeAdventure/AdventOfCode/day5input.txt"
    )

    total_map = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    with open(filename, "r") as file_object:
        current_map = None
        for line in file_object:
            if line.startswith("seeds"):
                seed_ranges = [int(n) for n in line.strip().split(": ")[1].split()]
                # Generate all seed numbers from the ranges
                seeds = []
                for i in range(0, len(seed_ranges) - 1, 2):
                    start, length = seed_ranges[i], seed_ranges[i + 1]
                    seeds.extend(range(start, start + length))
                # If the seed_ranges list is odd, add the last number as a single-value range
                if len(seed_ranges) % 2 != 0:
                    seeds.append(seed_ranges[-1])

            elif "map" in line:
                current_map = line.strip().split()[0]
            elif current_map and line.strip():
                total_map[current_map].append([int(n) for n in line.strip().split()])

    # Process each seed through all mappings
    processed_mappings = [
        total_map[key]
        for key in [
            "seed-to-soil",
            "soil-to-fertilizer",
            "fertilizer-to-water",
            "water-to-light",
            "light-to-temperature",
            "temperature-to-humidity",
            "humidity-to-location",
        ]
    ]
    location_numbers = [process_seed(seed, processed_mappings) for seed in seeds]

    # Find the lowest location number
    final_location = min(location_numbers)

    print("Final location:", final_location)


if __name__ == "__main__":
    main2()
