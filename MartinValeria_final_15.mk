MartinValeria_final_15.pdf: plot.py datoslp.dat
	python plot.py
datoslp.dat: a.out
	./a.out
a.out: particula.cpp
	g++ particula.cpp