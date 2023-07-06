def vracam_zbir_razliku_i_kub(broj):
    zbir = broj+256
    razlika = broj-13
    kub = pow(broj, 2)
    return print(f"{zbir}, {razlika}, {kub}")

broj = int(input("Unesite neki broj\n"))

vracam_zbir_razliku_i_kub(broj) 