def convert(min_x_str, min_y_str, max_x_str, max_y_str, left_str, top_str, right_str, bottom_str, pos_y_str, pos_x_str):

    print("\n==========")
    print("\n-- Step 1: Coords (in real life) boundary info --\n")

    min_x = float(min_x_str)
    min_y = float(min_y_str)
    max_x = float(max_x_str)
    max_y = float(max_y_str)

    print("[ Northwesternmost coords (LAT, LONG): " + max_y_str + ", " + min_x_str + " ]")
    print("[ Southeasternmost coords (LAT, LONG): " + min_y_str + ", " + max_x_str + " ]")


    print("\n==========")
    print("\n-- Step 2: Block (in Minecraft map) boundary info --\n")

    left_block = float(left_str)
    top_block = float(top_str)
    right_block = float(right_str)
    bottom_block = float(bottom_str)

    print("[ Top-left block (X, Z): " + left_str + ", " + top_str + " ]")
    print("[ Bottom-right block (X, Z): " + right_str + ", " + bottom_str + ") ]")

    ew_scale = (right_block - left_block) / (max_x - min_x)
    ns_scale = (bottom_block - top_block) / (max_y - min_y)


    print("\n==========")
    print("\n-- Step 3: Target Minecraft block position in real-life coords --\n")

    pos_x = float(pos_x_str)
    pos_y = float(pos_y_str)

    print("[ Target coords (LAT, LONG): " + pos_y_str + ", " + pos_x_str + " ]")


    print("\n==========")
    print("\n-- RESULT --\n")

    block_result_x = ew_scale * (pos_x - min_x) + left_block
    block_result_z = ns_scale * (max_y - pos_y) + top_block

    print("----------------------------------------")
    print("CONVERTED BLOCK POSITION (X, Z):\n")
    print(str(block_result_x) + " , " + str(block_result_z))
    print("\n----------------------------------------")
