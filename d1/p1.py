def main():
    # count = 0 #DEBUG
    all_values = []

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            # if count >= 5: break #DEBUG
            # print(line.rstrip()) #DEBUG

            # Parse only integers and add together in a string
            line_output = ""
            for char in line:
                if char in str([0,1,2,3,4,5,6,7,8,9]):
                    line_output += char
                    
            # Append first and last of parsed integers
            all_values.append(int(line_output[0] + line_output[-1]))

            # count += 1 #DEBUG
            # print(line_output) #DEBUG
        # print(all_values) #DEBUG
        print(sum(all_values))

main()