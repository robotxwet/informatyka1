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
