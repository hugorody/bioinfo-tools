#!/usr/bin/python3

from joblib import Parallel, delayed
import multiprocessing
from multiprocessing import Process, Manager

manager = Manager()
nascimentos = manager.dict() #se o dicionario for ser manipulado por Parallel, deve ser criado com o manager.dict()
num_cores = 3

def calc_nasc(nome,idade):
	ano_nascimento = 2020 - idade
	nascimentos[nome] = ano_nascimento


outrems = {"Edimercio":1985, "Tancredo":1999}

Parallel( n_jobs=num_cores) ( delayed(calc_nasc) (i[0],i[1]) for i in outrems.items() )


print (nascimentos)
