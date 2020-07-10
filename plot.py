import matplotlib.pyplot as plt


def create_data_array(ds_dim, list_statistiche, struttura_dati):
    final_list = []
    for k in list_statistiche:
        file = open("./"+str(ds_dim)+"/Dim-"+str(ds_dim)+"_OS-"+str(k)+"-"+str(struttura_dati)+".txt", "r")
        final_list.append(float(file.readline(14)))
        file.close()
    return final_list


def draw_graphic(ds_dim, list_statistiche, struttura_dati):
    list_x = list_statistiche
    list_y = create_data_array(ds_dim, list_statistiche, struttura_dati)
    plt.title(str(struttura_dati) + "-" + str(ds_dim))
    plt.xlabel("Statistica d'ordine")
    plt.ylabel("Time (s)")
    color = "w"
    mark = "o"
    mk_face_color = "y"
    label = str(struttura_dati) + "-" + str(ds_dim)
    plt.plot(list_x, list_y, label=label, color=color, marker=mark, markerfacecolor=mk_face_color)
    plt.legend()


def print_plot():
    plt.show()
