#!/C:\git\python
# .*. coding: utf-8 -*-

# Ein einfacher ChatBot
# (c) 2020 by me, Lizenz GPLv3
#import
import  random

# zufällige Antworten
zufallsantworten = ["Oh wirklich..", "interessant", "Das kann man so sehen", "Ich verstehe..."]

# Stopwörter
reaktionen = {"hallo": "Hali hallo",
                "wie geht es dir?": "Mir geht es auch gut",
                "schmeckt": "Ich habe keinen Geschmacksinn",
                 "warum?" : "Weil ich machine bin :)",
                 "nein": "Gut", "gut":"Danke", "danke" : "Bitte"}

# Ausgabe Head..
print ("Wilkommen beim ChatBot  (v1)")
print("Worüber wollen Sie sprechen")
print("Zum Beenden geben Sie bye ein...")
print("")

# main
nutzereingabe = ""
while nutzereingabe != "bye":
    nutzereingabe = ""
    while nutzereingabe == "":
         nutzereingabe = input("Ihre Fragen oder Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()

    intelligentAntworten = False
    for einzelworter in nutzerwoerter:
        if einzelworter in reaktionen:
            print(reaktionen[einzelworter])
            intelligentAntworten = True
    if not intelligentAntworten:         
         print(random.choice(zufallsantworten))
print("einen schönen Tag.")
