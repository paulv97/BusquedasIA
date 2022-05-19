from algorithms.a_search import ASearch
from algorithms.best_first_search import BestFirstSearch
from algorithms.gradient_ascent_search import GradientAscentSearch
from algorithms.greedy_search import GreedySearch
from algorithms.iterative_deepening_df_search import IterativeDeepeningDepthFirstSearch
from algorithms.uniform_cost_search import UniformCostSearch
from algorithms.bidirectional_search import BidirectionalSearch
from algorithms.depth_first_search import DepthFirstSearch
from algorithms.breadth_first_search import BreadthFirstSearch

from utilities.utils import cargar_archivo, llenar_tabla

import time

lista_nodos = cargar_archivo('./assets/nodes.csv')
llenar_tabla(lista_nodos)


def run_development():
    src = 'A'
    dest = 'G'

    print('----------BREADTH FIRST SEARCH-----------')
    searcher = BreadthFirstSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos:')
    print(searcher.extracted)
    print('Nodo encontrado:')
    print(searcher.found)

    print('----------DEPTH FIRST SEARCH-----------')
    searcher = DepthFirstSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos:')
    print(searcher.extracted)
    print('Nodo encontrado:')
    print(searcher.found)

    print('----------BIDIRECTIONAL SEARCH-----------')
    searcher = BidirectionalSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos INICIO:')
    print(searcher.init_extracted)
    print('Nodos Extraidos FIN:')
    print(searcher.goal_extracted)

    print('----------ITERATIVE DEEPENING DEPTH FIRST SEARCH-----------')
    searcher = IterativeDeepeningDepthFirstSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos:')
    print(searcher.extracted)
    print('Nodo encontrado:')
    print(searcher.found)

    print('----------UNIFORM COST SEARCH-----------')
    searcher = UniformCostSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos:')
    print(searcher.extracted)
    print('Nodo encontrado:')
    print(searcher.found)

    print('----------GRADIENT ASCENT SEARCH-----------')
    searcher = GradientAscentSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos:')
    print(searcher.extracted)
    print('Nodo encontrado:')
    print(searcher.found)

    print('----------BEST FIRST SEARCH-----------')
    searcher = BestFirstSearch()
    searcher.search(src, dest)
    print('Nodos Extraidos:')
    print(searcher.extracted)
    print('Nodo encontrado:')
    print(searcher.found)


def run_production():
    opt = -1

    menu_options = {
        0: 'Amplitud [0]',
        1: 'Profundidad [1]',
        2: 'Profundidad Iterativa [2]',
        3: 'Bidireccional [3]',
        4: 'Costo uniforme [4]',
        5: 'Ascenso a la colina [5]',
        6: 'Primero el mejor [6]',
        7: 'A* [7]',
        8: 'Algoritmo voraz [8]',
        9: 'Todos [9]',
        10: 'Salir [10]'
    }

    while opt not in menu_options.keys():
        print('-----------------Algoritmos de busqueda-----------------')

        print('Seleccione una opcion:')
        for key in menu_options:
            print(menu_options[key])

        opt = int(input())
        try:
            menu_options[opt]
        except Exception as error:
            print('\nDebe seleccionar una opcion valida\n')
            opt = -1
            continue

        if opt == 10:
            exit(0)

        print('Ingrese nodo inicial')
        src = input().upper()
        print('Ingrese un nodo meta')
        dest = input().upper()

        if opt == 0:
            print('[AMPLITUD]')
            searcher = BreadthFirstSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos:')
            print(searcher.extracted)
            print('Nodo encontrado:')
            print(searcher.found)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 1:
            print('[PROFUNDIDAD]')
            searcher = DepthFirstSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos:')
            print(searcher.extracted)
            print('Nodo encontrado:')
            print(searcher.found)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 2:
            print('[PROFUNDIDAD ITERATIVA]')
            searcher = IterativeDeepeningDepthFirstSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos:')
            print(searcher.extracted)
            print('Nodo encontrado:')
            print(searcher.found)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 3:
            print('[BIDIRECCIONAL]')
            searcher = BidirectionalSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos INICIO:')
            print(searcher.init_extracted)
            print('Nodos Extraidos FIN:')
            print(searcher.goal_extracted)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 4:
            print('[COSTO UNIFORME]')
            searcher = UniformCostSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos:')
            print(searcher.extracted)
            print('Nodo encontrado:')
            print(searcher.found)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 5:
            print('[ASCENSO A LA COLINA]')
            searcher = GradientAscentSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos:')
            print(searcher.extracted)
            print('Nodo encontrado:')
            print(searcher.found)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 6:
            print('[PRIMERO EL MEJOR]')
            searcher = BestFirstSearch()
            tic = time.perf_counter()
            searcher.search(src, dest)
            toc = time.perf_counter()
            print('Nodos Extraidos:')
            print(searcher.extracted)
            print('Nodo encontrado:')
            print(searcher.found)
            print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 7:
            print('[A ESTRELLA]')
            print('Algoritmo no soportado')
            # searcher = ASearch()
            # tic = time.perf_counter()
            # searcher.search(src, dest)
            # toc = time.perf_counter()
            # print('Nodos Extraidos:')
            # print(searcher.extracted)
            # print('Nodo encontrado:')
            # print(searcher.found)
            # print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 8:
            print('[ALGORITMO VORAZ]')
            print('Algoritmo no soportado')
            # searcher = GreedySearch()
            # tic = time.perf_counter()
            # searcher.search(src, dest)
            # toc = time.perf_counter()
            # print('Nodos Extraidos:')
            # print(searcher.extracted)
            # print('Nodo encontrado:')
            # print(searcher.found)
            # print(f"Ejecutado en  {toc - tic:0.4f} segundos")
            opt = -1
            continue

        if opt == 9:
            print('[Todos los algoritmos]')
            run_all_algorithms(src, dest)
            opt = -1
            continue


def run_all_algorithms(src, dest):
    details = [['|Algoritmo|', '|Extraidos|', '|Segundos empleados|']]

    searcher = BreadthFirstSearch()
    tic = time.perf_counter()
    searcher.search(src, dest)
    toc = time.perf_counter()
    details.append(['|Amplitud|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    searcher = DepthFirstSearch()
    tic = time.perf_counter()
    searcher.search(src, dest)
    toc = time.perf_counter()
    details.append(['|Profundidad|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    searcher = IterativeDeepeningDepthFirstSearch()
    tic = time.perf_counter()
    searcher.search(src, dest)
    toc = time.perf_counter()
    details.append(['|Profundidad iterativa|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    searcher = BidirectionalSearch()
    tic = time.perf_counter()
    searcher.search(src, dest)
    toc = time.perf_counter()
    details.append(['|Bidireccional|', searcher.init_extracted + searcher.goal_extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    # searcher = UniformCostSearch()
    # tic = time.perf_counter()
    # searcher.search(src, dest)
    # toc = time.perf_counter()
    # details.append(['|Costo uniforme|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    searcher = GradientAscentSearch()
    tic = time.perf_counter()
    searcher.search(src, dest)
    toc = time.perf_counter()
    details.append(['|Ascenso a la colina|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    searcher = BestFirstSearch()
    tic = time.perf_counter()
    searcher.search(src, dest)
    toc = time.perf_counter()
    details.append(['|Primero el mejor|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    # searcher = ASearch()
    # tic = time.perf_counter()
    # searcher.search(src, dest)
    # toc = time.perf_counter()
    # details.append(['|A*|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    # searcher = GreedySearch()
    # tic = time.perf_counter()
    # searcher.search(src, dest)
    # toc = time.perf_counter()
    # details.append(['|Algoritmo voraz|', searcher.extracted, '|' + f"{toc - tic:0.4f} seg" + '|'])

    for result in details:
        print(result[0], result[1], result[2])


if __name__ == '__main__':
    is_development = False

    if is_development:
        run_development()
    else:
        run_production()



