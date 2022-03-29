import sort, time, multiprocessing

n = int(input("Quantos elementos no array a ser ordenado? "))

# Pior caso: um array decrescente a ser ordenado de forma crescente
array = list(range(n, 0, -1))

ms = multiprocessing.Process(target=sort.MergeSort, args=(array,))
bs = multiprocessing.Process(target=sort.BubbleSort, args=(array,))

ms_estourado = False
bs_estourado = False

inicio_ms = time.time()
ms.start()

ms.join(60)
if ms.is_alive():
    ms_estourado = True
    ms.terminate()
    ms.join()
fim_ms = time.time()

inicio_bs = time.time()
bs.start()

bs.join(60)
if bs.is_alive():
    bs_estourado = True
    bs.terminate()
    bs.join()
fim_bs = time.time()

if ms_estourado:
    print("MergeSort não conseguiu rodar em 1 minuto...")
else:
    print("MergeSort demorou", "%.4f" % ((fim_ms - inicio_ms) * 1000), "ms para rodar!")

if bs_estourado:
    print("BubbleSort não conseguiu rodar em 1 minuto...")
else:
    print("BubbleSort demorou", "%.4f" % ((fim_bs - inicio_bs) * 1000), "ms para rodar!")