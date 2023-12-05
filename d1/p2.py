def main():
    nums = [0,1,2,3,4,5,6,7,8,9]
    num_to_word = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    all_values = []

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:

            idx_to_val = {}

            # Thx @poke on SO
            for num in num_to_word:
                # Get all indicies of num in line
                index = 0
                while index < len(line):
                    index = line.find(num, index)
                    if index == -1:
                        break
                    idx_to_val[index] = str(num_to_word[num])
                    index += len(num)
            
            # Get all indicies of an int in line
            char_count = 0
            for char in line:
                if char in str(nums):
                    idx_to_val[char_count] = char
                char_count += 1

            # Sort list of int and string indicies in line
            output = list(dict(sorted(idx_to_val.items())).values())
            all_values.append((int(output[0] + output[-1])))

        print(sum(all_values))

main()