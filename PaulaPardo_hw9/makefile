all: gen_times.x times_cpp times_python cpp_python

gen_times.x : 
	g++ PaulaPardo_GenerarTiempos.cpp 

times_cpp : 
	./a.out > times_cpp.csv

times_python : 
	python PaulaPardo_GenerarTiempos.cpp > times_python.csv

cpp_vs_python : times_cpp times_python
	python PaulaPardo_Graficas.py
