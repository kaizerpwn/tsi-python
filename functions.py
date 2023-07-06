def predstavi_me(ime, prezime, godine):
    print(f"Ja se zovem {ime}, prezivam se {prezime} i imam {godine} godina")

ime_i_prezime = input("Unesite Vase ime i prezime\n")
ime_i_prezime = ime_i_prezime.split()

ime = ime_i_prezime[0].capitalize()
prezime = ime_i_prezime[1].capitalize()

godine = input("Unesite Vase godine\n")

predstavi_me(ime, prezime, godine)