#spremenljivke

##password: "12789"

#print
#print(starost, password, sep =" & ")

# seznami / list

# povprecje visin dijakov v razredu 

visine = [180, 178, 160, 177, 187, 188] # seznam celih stevil / intiger list / altgr +f za oklepaj []
print(visine)
# dostop do indeksev seznama
print(visine[0])
print(visine[5])
print(len(visine))
print(max(visine))
print(min(visine))

povprecje = sum(visine)  / len(visine)
print(povprecje)

ime = "aleksander veliki"
#ime = "A", "l", 
print(ime[0])



# pogojni stavki / if statement

#izpisi ce je oseba polnoletna ali ni

starost = 15
# starost = input("vensi svojo starost")
#if pogoj:
#    koda 1
#    koda 2
# koda 3
if starost >= 18:
    print("oseba je polnoletna")
else:
    print("oseba ni polnoletna")