import Tree
import ChainedList as list
from timeit import default_timer as timer
import array_creator as ac
import datetime as dt


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


def main(dim, statistica):
    array = ac.create_rand_array(dim)
    tree = create_tree(dim, array)
    list_or = create_list_ordered(dim, array)
    list_un = create_list_unordered(dim, array)
    compare_tree_list(tree, list_or, list_un, dim, statistica)


if __name__ == "__main__":
    #####
    dim = 10
    stat = 50
    #####

    # main(dim, stat)
    array = ac.create_rand_array(dim, 0, 10)
    # list_or = create_list_ordered(dim, array)
    list_un = create_list_unordered(dim, array)
    list_un.print()










    # bst = create_random_tree(100000)
    # start = timer()
    #print(bst.OS_Select(bst.root, stat))
    #end = timer()
    #print("Temp per la statistica ", stat, " con tree:", end - start)
    # print(bst.OS_Rank(bst.OS_Select(bst.root, 14)))

    #lista = create_random_list(100000)
    #start = timer()
    #print(lista.list_select(stat))
    #end = timer()
    #print("Temp per la statistica ", stat, " con lista:", end - start)
