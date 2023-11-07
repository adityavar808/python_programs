move  = [" "," "," "," "," "," "," "," "," "] 

print(f'''

      {move[0]} | {move[1]} | {move[2]}
    ----------
      {move[3]} | {move[4]} | {move[5]}
    ----------
      {move[6]} | {move[7]} | {move[8]}
    ''')

turn = 'x'

while 1:
    loc_index = int(input(f"{turn} Turn Enter the location 0-8 : "))
    
    if  move[loc_index] != " " :
        print(f"Location is already in used by {move[loc_index]}. Please try another one !!")
        continue
    elif loc_index > 9 :
        print("location does not exist !!")
    else:
        move[loc_index] = turn

    print(f'''

      {move[0]} | {move[1]} | {move[2]}
    ----------
      {move[3]} | {move[4]} | {move[5]}
    ----------
      {move[6]} | {move[7]} | {move[8]}
    ''')

    if ' ' not in move:
        print("TIE")

    if move[0] == move[1] == move[2] != " ":
        print(move[0], 'Win')
        break
    
    if move[0] == move[4] == move[8] != " ":
        print(move[0], 'Win')
        break
    
    if move[0] == move[3] == move[6] != " ":
        print(move[0], 'Win')
        break
    
    if move[1] == move[4] == move[7] != " ":
        print(move[1], 'Win')
        break
    
    if move[2] == move[5] == move[8] != " ":
        print(move[2], 'Win')
        break

    if move[3] == move[4] == move[5] != " ":
        print(move[3], 'Win')
        break

    if move[6] == move[7] == move[8] != " ":
        print(move[6], 'Win')
        break

    if move[2] == move[4] == move[6] != " ":
        print(move[6], 'Win')
        break
    
    if turn == "o":
        turn = "x"
    else:
        turn = "o"
