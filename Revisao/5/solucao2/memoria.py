# pip install line-profiler memory-profiler
# para executar o codigo: python -m memory_profiler memoria.py (para memória) ////  python -m kernprof -l -v tempo.py (para tempo)

from memory_profiler import profile as mem_profile

@mem_profile
def tem_duplicados(lista):
    lista_ordenada = sorted(lista)
    for i in range(len(lista_ordenada) - 1):
        if lista_ordenada[i] == lista_ordenada[i + 1]:
            return True
    return False

lista_exemplo = [2, 3, 1, 3, 4, 5, 6, 2, 3, 1, 4, 6, 7]
tem_duplicados(lista_exemplo)