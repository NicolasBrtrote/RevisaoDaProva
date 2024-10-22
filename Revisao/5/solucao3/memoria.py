# pip install line-profiler memory-profiler
# para executar o codigo: python -m memory_profiler memoria.py (para memória) ////  python -m kernprof -l -v tempo.py (para tempo)

from memory_profiler import profile as mem_profile 

@mem_profile
def tem_duplicados(lista):
    elementos_vistos = set()
    for elemento in lista:
        if elemento in elementos_vistos:
            return True
        elementos_vistos.add(elemento)
    return False

lista_exemplo = [2, 3, 1, 3, 4, 5, 6, 2, 3, 1, 4, 6, 7]
tem_duplicados(lista_exemplo)