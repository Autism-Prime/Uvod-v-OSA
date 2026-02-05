"""
starost = [20, 22, 29, 28]




# zanke - for
# izrnacunaj povprecno starost
starost = [20, 22, 29, 28]

sest_let = 0
n = 0
for s in starost:
    #sest_let = sest_let + s # dolga verzija
    sest_let += s # krajsa verzija
    #n = n + 1
    n += 1
print(sest_let / n)
print(sum (starost) / len(starost)) # najkrajsa verzija "/" pomeni deljeno

# sestej stevila od 0 do 1000
# range
#print(list(range(1001)))

for i in range(1001):
    print(i)

print(sum(range(1001)))    # "sum" sesteje


#zmnozi (*) stevila od 0 - 1000   
zmnozek = 1               #!!!!!!! pomembno da mnozis s 1 kr 0 * 1 = 0
for z in range (1, 1001):
    zmnozek *= z
print(zmnozek)
"""

# funkcije
# def ime_funkcije(parameter1; parameter2):

def sestej(a, b):
    return a + b
    

#sestej(8, 10)
#sestej(8, 2)

s = sestej(20, 30)
print(s + 10)



#  pogoji ali  vejitve ali if stavki

# funkcija ki prejme parameter n in virne 0 ce je n negativen in 1 ce je n pozitiven

def predznak(n):
    if n < 0:
        return 0
    else:
        return 1
print (predznak(10)) #1
print(predznak(-10)) #-1