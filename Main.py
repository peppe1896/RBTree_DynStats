import Tree
import ChainedList as list
from timeit import default_timer as timer
import ArrayCreator as ac
import datetime as dt
import Plot
from decimal import *


def create_list_ordered(dim, array=None):
    list_ = list.linked_list()
    if array is None:
        array = ac.create_rand_array(dim)
    h_inizio = dt.datetime.now()
    start = timer()
    start_creaz_stru = timer()
    for i in range(0, dim):
        list_.add_ordered(array[i])
    end_creaz_stru = timer()
    list_.calc_size_ordered()
    end = timer()
    h_fine = dt.datetime.now()
    delta_tot = end - start  # Tempo di creazione totale
    delta_tot = Decimal(delta_tot)
    delta_insert = end_creaz_stru - start_creaz_stru  # Tempo per inserire i valori in lista
    delta_insert = Decimal(delta_insert)
    delta_size = end - end_creaz_stru  # Tempo inserimento parametro size
    delta_size = Decimal(delta_size)
    out = open("./Risultati/CreationTimes/ListaO-" + str(dim) + ".txt", "w+")
    out.write(str(delta_size) + "\n" + str(delta_insert) + "\n" + str(delta_tot) +
              "\n\nIn questo ordine, a partire dalla prima riga:"
              "\n - Tempo calcolo e inserimento parametro size ai nodi"
              "\n - Tempo inserimenti valori nella lista"
              "\n - Tempo totale della procedura."
              "\nTutti i tempi sono espressi in secondi. "
              "\n\nDimensione lista: " + str(dim) + "\n")
    out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
    out.write("\n\n" + str(str_start))
    out.write("\n" + str(str_end))
    print("Tempo creazione di lista ordinata:", end - start)
    out.close()
    return list_


def create_list_unordered(dim, array=None):
    list_ = list.linked_list()
    if array is None:
        array = ac.create_rand_array(dim)
    h_inizio = dt.datetime.now()
    start = timer()
    start_creaz_stru = timer()
    for i in range(0, dim):
        list_.add_unordered(array[i])
    end_creaz_stru = timer()
    list_.calc_size_unordered()
    end = timer()
    h_fine = dt.datetime.now()
    delta_tot = end - start  # Tempo di creazione totale
    delta_tot = Decimal(delta_tot)
    delta_insert = end_creaz_stru - start_creaz_stru  # Tempo per inserire i valori in lista
    delta_insert = Decimal(delta_insert)
    delta_size = end - end_creaz_stru  # Tempo inserimento parametro size
    delta_size = Decimal(delta_size)
    out = open("./Risultati/CreationTimes/ListaNO-" + str(dim) + ".txt", "w+")
    out.write(str(delta_size) + "\n" + str(delta_insert) + "\n" + str(delta_tot) +
              "\n\nIn questo ordine, a partire dalla prima riga:"
              "\n - Tempo calcolo e inserimento parametro size ai nodi"
              "\n - Tempo inserimenti valori nella lista"
              "\n - Tempo totale della procedura."
              "\nTutti i tempi sono espressi in secondi. "
              "\n\nDimensione lista: " + str(dim) + "\n")
    out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
    out.write("\n\n" + str(str_start))
    out.write("\n" + str(str_end))
    print("Tempo creazione di lista non ordinata:", end - start)
    out.close()
    return list_


def create_tree(dim, array=None, returnOSTree=True):
    tree = Tree.RedBlackTree()
    tree_without = Tree.RedBlackTree()
    if array is None:
        array = ac.create_rand_array(dim)
    h_inizio = dt.datetime.now()
    start = timer()
    for i in range(0, dim):
        tree.insert(array[i])
    end = timer()
    delta_size = end - start
    delta_size = Decimal(delta_size)  # Tempo creazione con parametro Size
    start = timer()
    for i in range(0, dim):
        tree_without.insert(array[i], withOS=False)
    end = timer()
    h_fine = dt.datetime.now()
    delta_non_size = end - start
    delta_non_size = Decimal(delta_non_size)
    out = open("./Risultati/CreationTimes/Albero-" + str(dim) + ".txt", "w+")
    out.write(str(delta_size) + "\n" + str(delta_non_size) +
              "\n\nIn questo ordine, a partire dalla prima riga:"
              "\n - Creazione albero di nodi con parametro size"
              "\n - Creazione albero R-B 'standard'"
              "\nTutti i tempi sono espressi in secondi. "
              "\n\nDimensione albero: " + str(dim) + "\n")
    out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
    str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
    str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
    out.write("\n\n" + str(str_start))
    out.write("\n" + str(str_end))
    print("Tempo creazione albero:", end - start)
    out.close()
    if returnOSTree:
        return tree
    else:
        return tree_without


def compare_tree_list(tree, list_or, list_un, dim, statistica):
    # Albero
    if tree != None:
        nome_file = "Dim-" + str(dim) + "_OS-" + str(statistica)
        out = open("./Risultati/" + nome_file + "-Albero.txt", "w")
        h_inizio = dt.datetime.now()
        start = timer()
        tree.OS_Select(tree.root, statistica)
        end = timer()
        h_fine = dt.datetime.now()
        delta = end - start
        delta = Decimal(delta)
        print("(ALBERO)Tempo per trovare", statistica, ":", delta)
        out.write(str(delta) + "\n\nIl tempo è in sec.\nDimensione Albero: " + str(dim) + "\n")
        out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
        str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
        str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
        out.write("\n\n" + str(str_start))
        out.write("\n" + str(str_end))
        out.close()

    # Lista ORDINATA
    if list_or != None:
        nome_file = "Dim-" + str(dim) + "_OS-" + str(statistica)
        out = open("./Risultati/" + nome_file + "-ListaO.txt", "w")
        h_inizio = dt.datetime.now()
        start = timer()
        list_or.list_select(statistica)
        end = timer()
        h_fine = dt.datetime.now()
        delta = end - start
        delta = Decimal(delta)
        print("(LISTA O)Tempo per trovare", statistica, ":", delta)
        out.write(str(delta) + "\n\nIl tempo è in sec.\nDimensione lista: " + str(dim) + "\n")
        out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
        str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
        str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
        out.write("\n\n" + str(str_start))
        out.write("\n" + str(str_end))
        out.close()

    # Lista NON ORDINATA
    if list_un != None:
        nome_file = "Dim-" + str(dim) + "_OS-" + str(statistica)
        out = open("./Risultati/" + nome_file + "-ListaNO.txt", "w")
        h_inizio = dt.datetime.now()
        start = timer()
        list_un.list_select(statistica)
        end = timer()
        h_fine = dt.datetime.now()
        delta = end - start
        delta = Decimal(delta)
        print("(LISTA NO)Tempo per trovare", statistica, ":", delta)
        out.write(str(delta) + "\n\nIl tempo è in sec.\nDimensione lista: " + str(dim) + "\n")
        out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
        str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
        str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
        out.write("\n\n" + str(str_start))
        out.write("\n" + str(str_end))
        out.close()


def print_graph():
    d = {1000: [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
         10000: [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
         20000: [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000],
         50000: [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],
         100000: [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]}
    list_dimensions = [1000, 10000, 20000, 50000, 100000]  # dimensione struttura
    data_structure = ["Albero", "ListaO", "ListaNO"]  # struttura
    for ds in data_structure:
        for i in list_dimensions:
            Plot.draw_graphic(i, d[i], str(ds))
            Plot.print_plot()


def print_structures_time(withOS):
    list_dimensions = [1000, 10000, 20000, 50000, 100000]  # dimensione struttura
    data_structure = ["Albero", "ListaO", "ListaNO"]  # struttura
    for ds in data_structure:
        Plot.draw_graphic(1, list_dimensions, str(ds), structur_times=True, withOS=withOS)
        Plot.print_plot()


if __name__ == "__main__":
    #####
    dim = 1000
    print_mode = True
    #####

    if not print_mode:
        array = ac.create_rand_array(dim)
        tree = create_tree(dim, array)
        # list_or = None
        # list_un = None
        list_or = create_list_ordered(dim, array)
        list_un = create_list_unordered(dim, array)

        still_inputs = True
        while still_inputs:
            inpt = int(input("Statistica d'ordine: (scrivi 0 per uscire)"))
            if int(inpt) == 0:
                still_inputs = False
            else:
                compare_tree_list(tree, list_or, list_un, dim, int(inpt))
    else:
        print_graph()
        print_structures_time(True)
        print_structures_time(False)
