# pip install line-profiler memory-profiler
# para executar o codigo: python -m memory_profiler memoria.py (para memória) ////  python -m kernprof -l -v tempo.py (para tempo)

from line_profiler import profile

@profile
def tem_duplicados(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

lista_exemplo = [2, 3, 1, 3, 4, 5, 6, 2, 3, 1, 4, 6, 7]
tem_duplicados(lista_exemplo)