def main():
    td_arr = []
    nums = [0,1,2,3,4,5,6,7,8,9]
    all_nums = []

    with open("input.txt") as f:
        lines = f.readlines()

        # Create 2D array
        for line in lines:
            line_arr = []
            for line_char in line.rstrip():
                line_arr.append(line_char)
            td_arr.append(line_arr)

        line_idx = 0
        for line in td_arr:
            char_idx = 0
            for char in line:
                # Symbol detected
                if char == "*":
                    # Mark adjacencies
                    lc = []
                    lc.append([line_idx - 1, char_idx - 1]) #TL
                    lc.append([line_idx - 1, char_idx]) #T
                    lc.append([line_idx - 1, char_idx + 1]) #TR
                    lc.append([line_idx, char_idx - 1]) #L
                    lc.append([line_idx, char_idx + 1]) #R
                    lc.append([line_idx + 1, char_idx - 1]) #BL
                    lc.append([line_idx + 1, char_idx]) #B
                    lc.append([line_idx + 1, char_idx + 1]) #BR

                    # print(lc)

                    # Check adjacencies
                    found_idx = []
                    lc_nums = []
                    for l,c in lc:
                        val = td_arr[l][c]

                        # If adjacent char is a number
                        if val in str(nums):
                            valid = True
                            number = ""
                            # Move to start of number
                            while td_arr[l][c] in str(nums):
                                # print("VAL", td_arr[l][c], "IDX", c)
                                c -= 1
                            # Read whole number from start
                            c += 1
                            try:
                                while td_arr[l][c] in str(nums):
                                    # Ignore number already validated
                                    if [l, c] in found_idx:
                                        valid = False
                                        break
                                    number += td_arr[l][c]
                                    found_idx.append([l, c])
                                    c += 1
                            except:
                                # Boundary error
                                pass
                            
                            if valid:
                                lc_nums.append(int(number))
                    if len(lc_nums) == 2:
                        all_nums.append(lc_nums[0] * lc_nums[1])

                char_idx += 1
            line_idx += 1
        
        # print(td_arr)
        # print(all_nums)
        print(sum((all_nums)))

main()
