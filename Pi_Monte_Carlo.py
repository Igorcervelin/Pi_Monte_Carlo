import math
import random
import multiprocessing
import time

#Gera um ponto X e Y entre(0,1)
def pontoxy():

	if (math.pow(random.random(),2) + math.pow(random.random(),2) ) < 1: 
    return 1 # x*x + y*y.
	else: return 0
    
# Cada vez que estiver entre 0 e 1, os acertos sobem
def montepi(rand_seed, tests):

	random.seed(rand_seed)
	circlepts = 0
	
	for i in range(int(tests)):
		circlepts += pontoxy()
		
	return [circlepts , tests]


def threads(nprocesso, return_dict, qtdPontos):

    """worker function"""
    py = []
    pi = montepi(random.random(),qtdPontos);
    return_dict[nprocesso] = pi


if __name__ == "__main__":

    manager = multiprocessing.Manager()
    return_dict = manager.dict() #resultado do worker
    job = [] #array dos resultados

    inicio = time.time()
    for i in range(8):
        p = multiprocessing.Process(target=threads, args=(i, return_dict, 1000000)) #parametros worker
        jobs.append(p)
        p.start()

    for proc in job:
        proc.join()
    print(return_dict.values())

    circlepts  = 0
    tests = 0

    for points in return_dict.values():
        tests += points[1]
        circlepts += points[0]
        
    fim = time.time()
    valor_pi = 4.0 * (circlepts)/tests

    print(("Valor estimado de Pi:", valor_pi))
    print(("Tempo de execucao:", str(fim-inicio)))
