#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

min = 1
max = 30

def main():
    again = "da"

    while again.lower() == "da":
        secret = random.randint(0, 30)
        guess = raw_input("Ugani skrito številko med 1 in 30. Prosimo, vnesite številko: ")


        if guess.isdigit():
            guess = int(guess)
            if guess == secret:
                print ("Čestitamo, uganili ste skrito številko.")
                break
            elif guess < min or guess > max:
                print ("Napaka! Niste vnesli številke med 1 in 30. Vnesli ste večje ali manjše število, t.j.: " + str(guess))
                print ("Skrita številka je: " + str(secret))
            else:
                print ("Žal niste uganili skrite številke.")
            again = raw_input("Ali želite ponovno ugibati? (da/ne) ")

        else:
            print ("Napaka! Niste vnesli števila med 1 in 30, vnesli ste: " + str(guess))
            again = raw_input("Ali želite ponovno ugibati? (da/ne) ")

if __name__ == "__main__":
    main()