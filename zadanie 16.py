samogłoski = ('a','ą','e','ę','i','o','ó','u','y') #mój zbiór samogłosek, lista
zdanie = []                                 #nie wiem czemu {},() to błąd i "" niszczyło równnanie, zdanie otacza znakiem
samogłoska =[]                              #musi być znak, dodaje do pierwszej samogłoski wybrany znak

tekst = input('podaj słowo: ')              #komputer pyta się o słowo
for znak in tekst:                          #pętla obiektowa for, każdemu elementowi w liście tekst daje wartość x
    if znak in samogłoski:                  #pętla zwykła, jeśli znak jest samogłoską
        samogłoska += znak                  #co robi z samogłoskami == usuwa, = nic nie robi
        zdanie.append(samogłoska)           #append to metoda dodająca do listy, do zbioru zdanie dodaje samogłoskę
        samogłoska = []                     #definiuje co otacza samogłoski, wstawienie innych znaków powoduje błąd
    else:
        zdanie += znak                      #co robi ze spółgłoskami == usuwa, = błąd, += idzie dalej
        
print(zdanie)                               
