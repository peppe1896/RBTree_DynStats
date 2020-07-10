import Tree
import ChainedList as list
from timeit import default_timer as timer
import ArrayCreator as ac
import datetime as dt
import plot


def create_list_ordered(dim, array=None):
    list_ = list.linked_list()
    if array is None:
        array = ac.create_rand_array(dim)
    start = timer()
    for i in range(0, dim):
        list_.add_ordered(array[i])
    list_.calc_size_ordered()
    end = timer()
    print("Tempo creazione di lista ordinata:", end - start)
    return list_


def create_list_unordered(dim, array=None):
    list_ = list.linked_list()
    if array is None:
        array = ac.create_rand_array(dim)
    start = timer()
    for i in range(0, dim):
        list_.add_unordered(array[i])
    list_.calc_size_unordered()
    end = timer()
    print("Tempo creazione di lista non ordinata:", end - start)
    return list_


def create_tree(dim, array=None):
    tree = Tree.RedBlackTree()
    if array is None:
        array = ac.create_rand_array(dim)
    start = timer()
    for i in range(0, dim):
        tree.insert(array[i])
    end = timer()
    print("Tempo creazione albero: ", end - start)
    return tree


def compare_tree_list(tree, list_or, list_un, dim, statistica):
    # Albero
    if tree != None:
        nome_file = "Dim-" + str(dim)+"_OS-"+str(statistica)
        out = open("./Risultati/" + nome_file + "-Albero.txt", "w")
        h_inizio = dt.datetime.now()
        start = timer()
        tree.OS_Select(tree.root, statistica)
        end = timer()
        h_fine = dt.datetime.now()
        delta = end - start
        print("(ALBERO)Tempo per trovare", statistica, ":", delta)
        out.write(str(delta) + "\n\nIl tempo è in sec.\nDimensione Albero: " + str(dim)+"\n")
        out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
        str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
        str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
        out.write("\n\n" + str(str_start))
        out.write("\n" + str(str_end))
        out.close()

    # Lista ORDINATA
    if list_or != None:
        nome_file = "Dim-" + str(dim)+"_OS-"+str(statistica)
        out = open("./Risultati/" + nome_file + "-ListaO.txt", "w")
        h_inizio = dt.datetime.now()
        start = timer()
        list_or.list_select(statistica)
        end = timer()
        h_fine = dt.datetime.now()
        delta = end - start
        print("(LISTA O)Tempo per trovare", statistica, ":", delta)
        out.write(str(delta) + "\n\nIl tempo è in sec.\nDimensione lista: " + str(dim)+"\n")
        out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
        str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
        str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
        out.write("\n\n" + str(str_start))
        out.write("\n" + str(str_end))
        out.close()

    # Lista NON ORDINATA
    if list_un != None:
        nome_file = "Dim-" + str(dim)+"_OS-"+str(statistica)
        out = open("./Risultati/" + nome_file + "-ListaNO.txt", "w")
        h_inizio = dt.datetime.now()
        start = timer()
        list_un.list_select(statistica)
        end = timer()
        h_fine = dt.datetime.now()
        delta = end - start
        print("(LISTA NO)Tempo per trovare", statistica, ":", delta)
        out.write(str(delta) + "\n\nIl tempo è in sec.\nDimensione lista: " + str(dim)+"\n")
        out.write("Data " + str(h_inizio.day) + "/" + str(h_inizio.month) + "/" + str(h_inizio.year))
        str_start = "Inizio:: " + str(h_inizio.hour) + ":" + str(h_inizio.minute) + ":" + str(h_inizio.second)
        str_end = "Fine:: " + str(h_fine.hour) + ":" + str(h_fine.minute) + ":" + str(h_fine.second)
        out.write("\n\n" + str(str_start))
        out.write("\n" + str(str_end))
        out.close()


def print_graph():
    list_dimensions = [1000, 10000, 25000, 50000, 100000] # dimensione struttura
    list_statistiche = [250, 500, 750, 1000]
    data_structure = ["Albero", "ListaO", "ListaNO"]  # struttura
    for ds in data_structure:
        for i in list_dimensions:
            plot.draw_graphic(i, list_statistiche, str(ds))
        plot.print_plot()


if __name__ == "__main__":
    #####
    dim = 25000
    printmode = True
    #####
    if not printmode:
        array = ac.create_rand_array(dim)
        tree = create_tree(dim, array)
        list_or = create_list_ordered(dim, array)
        # list_or = None
        list_un = create_list_unordered(dim, array)
        #list_un = None

        still_inputs = True
        while still_inputs:
            inpt = int(input("Statistica d'ordine: (scrivi 0 per uscire)"))
            if int(inpt) == 0:
                still_inputs = False
            else:
                compare_tree_list(tree, list_or, list_un, dim, int(inpt))
    else:
        print_graph()
