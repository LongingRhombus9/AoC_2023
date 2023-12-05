def main():
    valid_id = []
    powers = []

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            results = {"red":0, "green":0, "blue":0}
            sep = line.split(": ")
            id = sep[0].split(" ")[1]
            games = sep[1].split(";")

            for game in games:
                game = game.strip().split(", ")
                for cube in game:
                    res = cube.split(" ")
                    quantity = int(res[0])
                    colour = res[1]
                    curVal = results[colour.strip()]
                    if quantity > curVal:
                        results[colour] = quantity
            
            powers.append(results["red"] * results["green"] * results["blue"])
            
            if results["red"] <= 12 and results["green"] <= 13 and results["blue"] <= 14:
                valid_id.append(int(id))
                print(id, results, "PASS")
            else:
                print(id, results, "FAIL")

main()