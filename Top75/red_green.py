def check_cards(input_list):
    R_list = []
    G_list = []
    for i in range(len(input_list)):
        if input_list[i].startswith("R"):
            R_list.append(input_list[i])
        elif input_list[i].startswith("G"):
            G_list.append(input_list[i])
    return sorted(R_list) + sorted(G_list)


print(check_cards(['R1','G2','R5','G1','R4','R2','R3','G4','G3','G5']))