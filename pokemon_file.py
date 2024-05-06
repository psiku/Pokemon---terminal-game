def read_from_file(file):
    with open(file, "r", encoding='cp850') as reader:
        line_number = 0
        list_of_pokemons = []
        list_of_names = []
        for row in reader:
            line_number += 1
            if line_number == 1:
                continue
            x = row.partition(']')
            b = x[2].split(",")
            weak = (b[1], b[2], b[3], b[4], b[5], b[6], b[7],
                    b[8], b[9], b[10], b[11], b[12], b[13],
                    b[14], b[15], b[16], b[17], b[18])
            pokemon = (b[30], b[19], b[25], b[28], b[35], b[36], b[37], weak)
            list_of_pokemons.append(pokemon)
            list_of_names.append(b[30])
        return (list_of_pokemons, list_of_names)
