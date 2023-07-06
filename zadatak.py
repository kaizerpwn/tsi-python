ime_i_prezime = input("Unesite Vaše ime i prezime:\n")
ime_i_prezime = ime_i_prezime.split()

ime = ime_i_prezime[0].capitalize()
prezime = ime_i_prezime[1].capitalize()

print("__________")
godine = input("Unesite Vaše godine:\n")
print("__________")
grad = input("Unesite Vaš grad:\n")
grad = grad.capitalize()
print("__________")

print(
    f"Ja se zovem {ime} i prezivam {prezime}. Imam {godine} godina i trenutno zivim u gradu {grad}.")
