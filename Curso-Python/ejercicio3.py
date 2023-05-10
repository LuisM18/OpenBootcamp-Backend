peso = float(input("Digita su peso corporal(kg): "))
altura = float(input("Digita su altura(m): "))

imc = peso/(altura**2)

print("Tu índice de masa corporal es ", round(imc,2)) 
