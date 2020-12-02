#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przedmiot: Informatyka
# Kierunek studiów: Energetyka
# Semestr: zimowy
# Rok akademicki: 2020/2021
# Data (dzień.miesiąc.rok): 02.12.2020
# Imię: Zbigniew
# Nazwisko: Wereszczyński
# Numer albumu ZUT: wz49676

"""
Napisz program który wygeneruje listę dziesięciu tysięcy pseudolosowych liczb całkowitych większych niż zero
i mniejszych niż dwadzieścia tysięcy. Liczby nie mają się powtarzać. Oblicz ile wynosi średnia, czyli suma wszystkich
wylosowanych liczb podzielona przez dziesięć tysięcy. Oblicz ile wynosi mediana,
czyli taka z nich że połowa wylosowanych liczb jest mniejsza (lub równa) od niej, a połowa jest większa.
"""

Low = 1                                                         #Najmniejsza liczba do wygenerowania

High = 20000                                                    #Największa liczba, której nie osiągniemy

Zasięg = 10000                                                  #Liczba Generowanych liczb
                              
import random                                                   #importujemy funkcje random by wylosować losowe liczby

zbiór = set(random.sample(range(Low, High), Zasięg))            #Program, który generuje liczby, nie powtarza ich

print(zbiór)                                                    #Drukuje wartości w konsoli

import statistics                                               #importujemy funkcje statistics dla mediany i średniej

mediana = statistics.median(zbiór)                              #funkcja oblicza medianę

średnia = statistics.mean(zbiór)                                #funkcja oblicza średnią

print(mediana)                                                  #drukuje medianę

print(średnia)                                                  #drukuje średnią
