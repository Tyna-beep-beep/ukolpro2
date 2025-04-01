#úkol A
jidloJedna=str(input("jaké bylo 1 jidlo"))
jidloDva=str(input("jake bylo 2 jidlo"))
jidloTri=str(input("jake bylo 3 jidlo"))
pocetA=int(input("kolik melo 1 jidlo kalorii"))
pocetB=int(input("kolik melo 2 jidlo kalorii"))
celkove_kalorie=pocetA+pocetB+(int(input("kolik melo 3 jidlo kalorii")))
print(celkove_kalorie)

#ukol B
sportJedna=str(input("Jaký byl váš první sport?"))
sportDva=str(input("Jaký byl váš druhý sport?"))
 
minutJedna=int(input("Jak dlouho trval první sport?"))
minutDva=int(input("Jak dlouho trval druhý sport?"))
#1 minuta je 5 kalorií
 
celkovy_minuty=minutJedna+minutDva
celkovy_vydej=celkovy_minuty*5
print(celkovy_vydej)

#spolecny úkol
#pavlova úkol A
#klickova úkol B
print(celkove_kalorie)
print(celkovy_vydej)
if (celkovy_vydej>celkove_kalorie):
    print("nedostatek")
else: 
    print("prebytek")
print("{celkove_kalorie:.5f}")
