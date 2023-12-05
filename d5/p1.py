def main():
    raw_mappings = {}
    locations = []

    with open("input.txt") as f:
        lines = f.readlines()
        # Get seeds
        seeds = lines[0].split(" ")[1:]

        # Get mappings
        map_title = ""
        for line in lines[2:]:
            line = line.strip()
            if 'map' in line:
                map_title = line.split(" ")[0]
                raw_mappings[map_title] = []
                continue
            if line == "":
                continue
            raw_mappings[map_title].append(line.split(" "))

        # Create mapping data
        for seed in seeds:
            num = int(seed.strip())
            for v in raw_mappings.values():
                for i in v:
                    start = int(i[1])
                    end = int(i[0])
                    step = int(i[2].strip())
                    diff = num - start
                    check = end + diff
                    if check >= end and check <= end + step:
                        num = check
                        break
            locations.append(num)

        print(min(locations))
main()
