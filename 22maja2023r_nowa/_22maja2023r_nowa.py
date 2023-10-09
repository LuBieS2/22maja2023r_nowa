#https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Informatyka/MINP-R0-100-2305.pdf
#3.1
file=open("pi.txt", "r")
pi=list(map(str.strip, file.readlines()))
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
#rosnace=[]
#malejace=[]
#count=0

'''for n, i in enumerate(numbers):
        if n<len(numbers-2):
            if i<numbers[n+1] and chuj==0 and numbers[0]<numbers[1]:
                if len(rosnace)==0:
                    rosnace.append(i)
                rosnace.append(numbers[n+1])
            elif i>numbers[n+1]:
                chuj+=1
            else:
                kiurw+=1
            if len(rosnace)>=2 and numbers[n+1]>numbers[n+2] and kiurw>0:
                if len(malejace)==0:
                    malejace.append(numbers[n+1])
                malejace.append(numbers[n+2])
                chuj+=1
            elif len(malejace)>0:
                break
    if len(rosnace)+len(malejace)>biggest:
        biggest=len(rosnace)+len(malejace)
    malejace=[]
    rosnace=[]
print(biggest)'''
#2
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