#! /usr/bin/python
#-*-coding: utf-8 -*-
#HSR_PYTHON
#EliasBulk

import math

H = "H"
H5 = H + H + H + H + H
space = " "
space2 = "  "
space3 = "   "
I = "I"

opdrscheiding = "===================================================================================================="

opdr3som = 100+200-10

opdr4soma = 2+3
opdr4somb = 8*opdr4soma
opdr4som = opdr4somb+3

#8.5((8.1+4.8)(8*10))+3
opdr5soma = 8*10
opdr5somb = 8.1+4.8
opdr5somc = opdr5soma*opdr5somb
opdr5somd = 8.5*opdr5somc
opdr5som = opdr5somd+3

#opdr8soma = math.pow()

opdr9error = "Error!"
opdr9functied = opdr9error
opdr9functiec = opdr9functied
opdr9functieb = opdr9functiec
opdr9functiea = opdr9functieb

#START
print("Hallo!")

#Voor opdracht6, 7
print("Gelieve in te vullen voor opdrachten 6 en 7")
username = input("Vul uw gebruikernaam in: ")
name = input("Vul uw naam in: ")
agestart = int(input("Vul uw geboortejaar in: "))
age = 2016-agestart

print(opdrscheiding)

input("Enter voor meer!")

print(opdrscheiding)

def opdracht2():
    print("OPDRACHT2")
    print(H + space3 + H + space2 + I)
    print(H + space3 + H)
    print(H + space3 + H + space2 + I)
    print(H5 + space2 + I)
    print(H + space3 + H + space2 + I)
    print(H + space3 + H + space2 + I)
    print(H + space3 + H + space2 + I)

def opdracht3():
    print("OPDRACHT3")
    print(opdr3som)

def opdracht4():
    print("OPDRACHT4")
    print("Het resultaat van 8(2+3)+3 is", opdr4som, "!!!")

def opdracht5():
    print("OPDRACHT5")
    print("Het antwoord van de berekening is:", opdr5som)

def opdracht6():
    print("OPDRACHT6")
    print("Welkom", username, ", je bent nu ingelogd")

def opdracht7():
    print("OPDRACHT7")
    print("Hallo", name, ". In het jaar 2016 was/wordt je", age, ".")

def opdracht8():
    print("OPDRACHT8")
    #print(opdr8som)

def opdracht9():
    print("OPDRACHT9")
    print(opdr9error)

opdracht2()
print(opdrscheiding)
opdracht3()
print(opdrscheiding)
opdracht4()
print(opdrscheiding)
opdracht5()
print(opdrscheiding)
opdracht6()
print(opdrscheiding)
opdracht7()
print(opdrscheiding)
opdracht8()
print(opdrscheiding)
opdracht9()
print(opdrscheiding)
