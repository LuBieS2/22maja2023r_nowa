#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Informatyka/MINP-R0-100-2305.pdf
from winreg import KEY_CREATE_LINK


def wczytaj_liczby(nazwa_pliku):
    file=open(nazwa_pliku, "r")
    pi=list(map(str.strip, file.readlines()))
    return pi
def czy_rosnaca_malejacy(ciag):
    a0=ciag[0]
    a1=ciag[1]
    i=2
    if a0>=a1:
        return False
    while a0<a1:
        a0=a1
        a1=ciag[i]
        i+=1
        if i==len(ciag):
            if a0>a1:
                return True
            return False
    if a0==a1:
        a0=a1
        a1=ciag[i]
        i+=1
        if i==len(ciag):
           if a0>a1:
                return True
           return False
    while a0>a1:
        a0=a1
        a1=ciag[i]
        i+=1
        if i==len(ciag):
            if a0>a1:
                return True
            return False
    return False

def wczytaj_ciagi(liczby):
    i=0
    tablice=[]
    while i<=len(liczby)-6:
        tablice.append([])
        for j in range(6):
            tablice[i].append(liczby[j+i])
        i+=1
    return tablice
#3.1
def zad1():
    pi=wczytaj_liczby("pi_przyklad.txt")
    n=0
    numbers_2=[]
    c=""
    for n, i in enumerate(pi):
        if n<(len(pi)-1):
            c=i+(pi[n+1])
            numbers_2.append(c)
#print(numbers_2)
#print(numbers_2)
    nw1=[]
    for i in numbers_2:
        if i[0]=='9' and i[0]!='0':
            nw1.append(i)
    print(len(nw1))
#3.2
def zad2():
    pi=wczytaj_liczby("pi_przyklad.txt")    
    shortest=0
    c_shortest=100
    longest=0
    c_longest=0
    for i in numbers_2:
        if c_shortest>numbers_2.count(i):
            c_shortest=numbers_2.count(i)
            shortest=i
        if c_longest<numbers_2.count(i):
            c_longest=numbers_2.count(i)
            longest=i
    for i in range(9, 100):
        #print(i)
        if i==9:
            if not "00" in numbers_2:
                c_shortest=0
                shortest='00'
        elif not str(i) in numbers_2:
            c_shortest=0
            shortest=str(i)
    
    print(c_longest, longest)
    print(c_shortest, shortest)
#3.3
def zad3():
    pi=wczytaj_liczby("pi_przyklad.txt")
    ciagi=wczytaj_ciagi(pi)

    rosnaca_malejacy=[]
    for ciag in ciagi:
    
        if czy_rosnaca_malejacy(ciag):
            rosnaca_malejacy.append(ciag)
    print(len(rosnaca_malejacy))
    print(len(pi))
    print(len(ciagi))
#3.4
def zad4():
    pi=wczytaj_liczby("pi.txt")    
    najdluzszy_index=0
    najdluzsza_dlugosc=0
    index=0
    czy_koniec=False
    while index+4<=len(pi) or czy_koniec:
        dlugosc_ciagu=4    
        ciag=pi[index:index+dlugosc_ciagu]
    
        index_kopia = index
        while czy_rosnaca_malejacy(ciag):
            index_kopia-=1
            dlugosc_ciagu+=1
            ciag=pi[index_kopia:index_kopia+dlugosc_ciagu]
        
        ciag=ciag[1:]
        index_kopia+=1
        dlugosc_ciagu-=1
    
        while czy_rosnaca_malejacy(ciag):
            dlugosc_ciagu+=1
            if index_kopia+dlugosc_ciagu==len(pi):
                czy_koniec=True
                break
            ciag=pi[index_kopia:index_kopia+dlugosc_ciagu]
    
        dlugosc_ciagu-=1
    
        if dlugosc_ciagu>najdluzsza_dlugosc:
            najdluzsza_dlugosc=dlugosc_ciagu
            najdluzszy_index=index_kopia
        index+=1
    print(najdluzsza_dlugosc)
    print(najdluzszy_index+1, pi[najdluzszy_index:najdluzszy_index+najdluzsza_dlugosc])
#2
def zad22():
    file1=open("bin_przyklad.txt","r")
    n=list(map(str.strip, file1.readlines()))
    counter=0
    highest_number=0
    xor_bin=[]
    for num in n:
        number=(int(num, 2))    
        nb=num
        c=0
        for i  in range(len(nb)-1):
            if nb[i]!=nb[i+1]:
                 c+=1
        if c>0:
            c+=1
        if c<=2:
            counter+=1    
        print(c, nb)
        if number>highest_number:
            highest_number=number
        print(number)
        number=0
    print(bin(highest_number))
    print((123^45)^45)
    for num in n:
        number=(int(num, 2))    
        xor_bin.append(number^(int(number/2)))
    for x in xor_bin:
        print(bin(x))

def znajdz_rosnacy(ciag):
    i=0
    
    while i < len(ciag) - 1 and ciag[i+1] > ciag[i]:
        i+=1
    
    return i

def znajdz_malejacy(ciag):
    i = len(ciag) - 1
    
    while i > 0 and ciag[i] < ciag[i-1]:
        i-=1
        
    return i

def znajdz_malejacy_2(ciag):
    i = 0
    
    while i < len(ciag) - 1 and ciag[i+1] < ciag[i]:
        i+=1
        
    return i

def zadanie3():
    pi=wczytaj_liczby("pi_przyklad.txt")
    ciagi=wczytaj_ciagi(pi)
    rosnaco_malejace=[]
    
    for ciag in ciagi:
        if znajdz_malejacy - znajdz_rosnacy(ciag) <= 1:
            rosnaco_malejace.append(ciag)
            
    print(rosnaco_malejace)

'''
def zadanie4():
    pi=wczytaj_liczby("pi_przyklad.txt")
    najdluzszy = 0    
    najdluzszy_index = 0
    
    index = 0
    while index + 1 < len(pi):
        rosnacy = znajdz_rosnacy(pi[index:])
        if rosnacy != 0:
            
            index_malejacy = index + rosnacy
            malejacy = 0
            if pi[index_malejacy] == pi[index_malejacy + 1]:
                malejacy = znajdz_malejacy_2(pi[index+1])
            else:
                malejacy = znajdz_malejacy_2(pi[index])
            if malejacy != 0:
                dlugosc = rosnacy + malejacy
                if dlugosc > najdluzszy:
                    najdluzszy = dlugosc
                    najdluzszy_index = rosnacy
            index += rosnacy + malejacy
        else:
            index += 1
            
    print(najdluzszy)
    print(najdluzszy_index)'''
    
'''zajebcie mnie'''
    