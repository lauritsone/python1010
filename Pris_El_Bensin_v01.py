# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: Thomas L
2024-11-04
This is a temporary script file.
"""


#Kjørte km pr år
KmTotal = 16000
#Årlig trafikkforsikring for både bensin og el
Trafikkforsikringsavgift = 8.38*365
#Forbruk pr km El
DrivstoffbrukEl = KmTotal*0.2*2
#Forbruk pr km bensin
DrivstofforbrukBensin = KmTotal*1
#Bomavgift El
BomavgiftEl = KmTotal*0.1
#Bomavgift Bensin
BomavgiftBensin = KmTotal*0.3
#Forsikring årlig
ForsikringEL = 5000
ForsikringBensin = 7500

#Funksjoner for å regne sammen totalen av kostnader 
KostnadElbil = Trafikkforsikringsavgift + DrivstoffbrukEl + BomavgiftEl + ForsikringEL
KostnadBensin = Trafikkforsikringsavgift + DrivstofforbrukBensin + BomavgiftBensin + ForsikringBensin

print("Dette koster en Elbil pr år:", KostnadElbil, "kr")
print("Dette koster en Bensinbil pr år:", KostnadBensin,"kr")

#Funksjon for å se kost differanse, samt printe hva som er billigst
KostnadForskjell =  KostnadBensin - KostnadElbil
print("Det er",KostnadForskjell,"kr forskjell pr år mellom bensin og elbil")

if KostnadBensin > KostnadElbil:
    print("Elbil er rimeligst med en totalkost pr år på",KostnadElbil,"kr")
    
elif KostnadBensin < KostnadElbil:
        print("Bensin er billigst med en totalkost pr år på",KostnadBensin,"kr")
    
    
    

    

#print(" er rimligst med en årskostnad på", KostnadElbil, "Bensin koster", KostnadForskjell, "mer per år" )
 