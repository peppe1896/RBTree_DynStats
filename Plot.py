import matplotlib.pyplot as plt


def create_data_array(ds_dim, list_statistiche, struttura_dati):
    final_list = []
    for k in list_statistiche:
        file = open("./Risultati/Dim-"+str(ds_dim)+"_OS-"+str(k)+"-"+str(struttura_dati)+".txt", "r")
        final_list.append(float(file.readline()))
        file.close()
    return final_list


def create_array_ds(list_dims, struttura_dati, withOS=True):
    final_list = []
    if struttura_dati == "Albero":
        if withOS == True: # tempo di creazione albero con parametro size
            linetotake = 0
        else:
            linetotake = 1
        for k in list_dims:
            file = open("./Risultati/CreationTimes/" + str(struttura_dati) + "-" + str(k) + ".txt", "r")
            lines = file.readlines()
            final_list.append(float(lines[linetotake]))
            file.close()
    else:
        if withOS: # prendo il tempo della funzione calcolo size
            linetotake = 0
        else:  # prendo il tempo di inserimento
            linetotake = 1
        for k in list_dims:
            file = open("./Risultati/CreationTimes/" + str(struttura_dati) + "-" + str(k) + ".txt", "r")
            line = file.readlines()
            final_list.append(float(line[linetotake]))
            file.close()
    return final_list


def draw_graphic(ds_dim, list_ascissa, struttura_dati, structur_times=False, withOS=True):
    if not structur_times: # voglio stampare i tempi di accesso alle statistiche d'ordine
        list_x = list_ascissa
        list_y = create_data_array(ds_dim, list_ascissa, struttura_dati)
        plt.xlabel("Statistica d'ordine")
        plt.ylabel("Tempo (s)")
        plt.title(str(struttura_dati) + "-" + str(ds_dim))
    else: # voglio stampare i tempi di creazione delle strutture dati
        list_x = list_ascissa
        list_y = create_array_ds(list_ascissa, struttura_dati, withOS)
        plt.xlabel("Dimensione")
        plt.ylabel("Tempo (s)")
        string = " senza campo size."
        if withOS == True:
            string = " con campo size."
        plt.title("Tempi creazione " + str(struttura_dati) + string)
    color = "b"
    mark = "o"
    mk_face_color = "r"
    label = str(struttura_dati) + "-" + str(ds_dim)
    plt.plot(list_x, list_y, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    plt.legend()


def print_plot():
    plt.show()
