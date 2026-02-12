# predavanje 4
# stringi

ime = "Kasper Madrugov"

# upper
print(ime.upper()) #pretvori v uppercase

# lower
print(ime.lower()) #pretvori v lowercase

# strip
print(ime.strip()) #umakne whitespace pred in za imenom

#split
print(ime.split()) #razbije string v list
spl = ime.split()
print(spl[0]) # izpise 0 element (prvi element)
print(spl[1])

#slicing stringov
print(ime[0]) #izpise prvo crko ali space (prvi element)
print(ime[0:8]) # od : do
print(ime[0:6:-3])
print(ime[::-1]) #izpise obratno

spl= ime.split()
print(spl)
print(spl[1][0])

#f- string
ime = "luka"
pri = "cola"
# moje ime je luka in pisem, se cola
print(f"moje ime je {ime} in pisem, se {pri}")