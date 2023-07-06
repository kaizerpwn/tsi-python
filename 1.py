# ime = input("Unesite ime:\n")
# print(f"Vase ime je {ime.strip().title()}")


hobit = "Frodo Bagins"

ime_i_prezime = hobit.split()

print(f"Hobitovo ime je {ime_i_prezime[0]}")
print(f"Hobitovo prezime je {ime_i_prezime[1]}")

result = " ".join(word for word in ime_i_prezime if word)

print(f"Kompletan hobitov string je {result}")
