

numero_del_isuario1 = int(input("dime un numero:"))
numero_del_isuario2 = int(input("dime un numero:"))
numero_del_isuario3 = int(input("dime un numero:"))

resultado = float(max(numero_del_isuario1, numero_del_isuario2, numero_del_isuario3))

type(float(max(numero_del_isuario3, numero_del_isuario2, numero_del_isuario1)))




print("el numero mas gradnde es {}".format(resultado))


user_number = int(input("introduce un numero:"))

if user_number >= 5:
    print("el numero es mayor q 5")




number_to_guess = 2
user_number = int(input("adivina un numero; "))

if user_number == number_to_guess:
    print("has ganado")
else:
    print("has perdido")




