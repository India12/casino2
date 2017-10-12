#-*- coding: utf-8 -*-

secret = 7
min = 1
max = 50

guess = raw_input("Ugani skrito številko med 1 in 50. Prosimo, vnesite številko: ")

if guess.isdigit():
    guess = int(guess)
    if guess == secret:
        print "Čestitamo, uganili ste skrito številko."
    elif guess < min:
        print "Napaka! Niste vnesli številke med 1 in 50. Vnesli ste manjše število, t.j.: " + str(guess)
    elif guess > max:
        print "Napaka! Niste vnesli številke med 1 in 50. Vnesli ste večje število, t.j.: " + str(guess)
    else:
        print "Žal, niste uganili skrite številke. Skrita številka je: " + str(secret)
else:
    print "Napaka! Niste vnesli števila, vnesli ste črko: " + str(guess)