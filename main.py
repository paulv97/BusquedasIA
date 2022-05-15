from best_first_search import BestFirstSearch
from gradient_ascent_search import GradientAscentSearch
from iterative_deepening_df_search import IterativeDeepeningDepthFirstSearch
from uniform_cost_search import UniformCostSearch
from bidirectional_search import BidirectionalSearch
from depth_first_search import DepthFirstSearch
from breadth_first_search import BreadthFirstSearch

from utils import cargar_archivo, llenar_tabla

lista_nodos = cargar_archivo()
llenar_tabla(lista_nodos)

if __name__ == '__main__':
    #print('Ingrese el nodo inicial:')
    #nodoInicial = input()
    #nodoInicial = nodoInicial.upper()

    #print('Ingrese el nodo final:')
    #nodoFinal = input()
    #nodoFinal = nodoFinal.upper()

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
    #searcher = UniformCostSearch()
    #searcher.search(src, dest)
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


