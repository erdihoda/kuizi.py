print("Mire se erdhe ne kuiz!")

playing = input("A doni te luani? ")

if playing.lower() != "po":
    quit()

print("Suksese :)")
print("\n")

score = 0

## Pyetja e pare
answer = input("Kush krijoi python? ")

if answer.lower() == "guido van rossum":
    print("E sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E pasakte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pyetja e dyte
answer = input("Humoristi me i njohuri ne bote? ")

if answer.lower() == "mr bean":
    print("E sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E pasakte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pyetje e Trete
answer = input("Pronari i Tesles? ")

if answer.lower() == "elon musk":
    print("E sakte!")
    score += 10
    print("Rezulati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pyetja e Katert
answer = input("hard-disku a eshte me e shpejte se ssd ? ")

if answer.lower() == "jo":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pytetja e peste
answer = input("qka eshte turtle? ")

if answer.lower() == "eshte ne librarine e pythonit dhe perdoret per te vizatuar":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pytetja e gjashte
answer = input("Kur eshte eshte Pavaresia? ")

if answer.lower() == "me 17 shkurt 2008":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pytetja e shtate
answer = input("shteti qe ka toke me se shumti ne bote? ")

if answer.lower() == "rusia":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pytetja e tete
answer = input("shteti qe prodhon me se shumti mjete? ")

if answer.lower() == "kina":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pytetja e nente
answer = input("shteti me i pasur ne bote? ")

if answer.lower() == "usa":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")

## Pytetja e dhjete
answer = input("cila eshte akademia me e mire per kodim? ")

if answer.lower() == "probit academy":
    print("e sakte!")
    score += 10
    print("Rezultati juaj eshte ", score)
    print("\n")
else:
    print("E paskte")
    print("Rezultati juaj eshte ende ", score)
    print("\n")


print("Ti ke " + str(score) + " Pyetje e sakte!")
print("Cili eshte " + str((score / 10) * 10) + "%")