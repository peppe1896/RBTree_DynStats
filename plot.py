import matplotlib.pyplot as plt


def create_data_array(list_of_read, tipo, algoritmo, object):
    final_list = []
    for k in list_of_read:
        if object:
            nom_file = "Obj_In-" + str(k) + ".txt"
            file = open("./Test/ObjRes/" + str(algoritmo) + "/" + str(tipo) + "/" + nom_file, "r")
        else:
            nom_file = "In=" + str(k) + ".txt"
            file = open("./Test/"+str(algoritmo)+"/"+str(tipo)+"/"+nom_file, "r")
        final_list.append(float(file.readline(7)))
        file.close()
    return final_list


def draw_graphic(list_input, tipo_input, algoritmo, name, object=False):
    list_x = list_input
    list_y = create_data_array(list_x, tipo_input, algoritmo, object)

    if name == "":

        name = str(algoritmo)
        if tipo_input == "Casuale":
            color = "b"
            mark = "^"
            mk_face_color = "m"
            label = "Input " + str(tipo_input)
        elif tipo_input == "Invertito":
            color = "r"
            mark = "d"
            mk_face_color = "c"
            label = "Input " + str(tipo_input)
        elif tipo_input == "Ordinato":
            color = "g"
            mark = "o"
            mk_face_color = "y"
            label = "Input " + str(tipo_input)
        else:
            color = "w"
            mark = "o"
            mk_face_color = "y"
            label = "Input " + str(tipo_input)
    else:

        if algoritmo == "MergeSort":
            color = "r"
            mark = "d"
            mk_face_color = "c"
        elif algoritmo == "InsertionSort":
            color = "b"
            mark = "o"
            mk_face_color = "m"
        elif algoritmo == "QuickSort":
            color = "g"
            mark = "*"
            mk_face_color = "r"
        elif algoritmo == "RadixSort":
            color = "c"
            mark = "."
            mk_face_color = "r"
        label = str(algoritmo)
    if object:
        plt.xlabel("Memoria occupata (KB)")
        plt.ylabel("Input (num elementi)", labelpad=-5)
        for i in range(0, len(list_y)):
            list_y[i] /= 1024
        plt.plot(list_y, list_x, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    else:
        plt.xlabel("Input (num elementi)")
        plt.ylabel("Time (s)")
        plt.plot(list_x, list_y, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    plt.legend()
    plt.title(name)


def print_plot():
    plt.show()


#################################


def plot_mode(tipo_input, algoritmo, full, name=""):
    if tipo_input == 0:
        print("Uso input CASUALE::")
        tipo_input = "Casuale"
    elif tipo_input == 1:
        print("Uso input INVERTITO::")
        tipo_input = "Invertito"
    elif tipo_input == 2:
        print("Uso input ORDINATO::")
        tipo_input = "Ordinato"
    else:
        print("DEFAULT INPUT TYPE: Random")
        tipo_input = "Casuale"

    print("Plotting:", str(tipo_input) + ", generato da " + str(algoritmo))
    lista_input = [1000, 10000, 20000, 35000, 50000, 60000, 80000, 100000, 120000]  # Base list

    if full and algoritmo == "MergeSort":
        lista_input.append(500000)
        lista_input.append(1200000)
        lista_input.append(5000000)
        lista_input.append(25000000)
        lista_input.append(50000000)
    elif algoritmo == "QuickSort":
        if full and tipo_input != "Ordinato":
            lista_input.append(500000)
            lista_input.append(1200000)
            lista_input.append(5000000)
            lista_input.append(25000000)
            lista_input.append(50000000)
        else:
            print("work in progress: INSERISCI QUI LA LISTA DEI VALORI PER QUICKSORT ORDINATO")
    elif algoritmo == "InsertionSort":
        if tipo_input == "Ordinato" and full:
            lista_input.append(500000)
            lista_input.append(1200000)
            lista_input.append(5000000)
            lista_input.append(12000000)
            lista_input.append(25000000)
            lista_input.append(50000000)
    elif full and algoritmo == "RadixSort":
        lista_input.append(500000)
        lista_input.append(1200000)
        lista_input.append(5000000)
        lista_input.append(12500000)
        lista_input.append(25000000)
        lista_input.append(50000000)
    plt.draw_graphic(lista_input, tipo_input, algoritmo, name)