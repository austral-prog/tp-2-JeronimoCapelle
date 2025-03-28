def change():
    expense = 23.75
    money = 100

    expense = float(input("Ingresar gasto:\n"))
    print(expense)
    
    money = int(input("Dinero recibido\n"))
    print(f"{money}\n")
    
    print("Vuelto\n")
    
    print("Pesos:")
    print(f"{int(money - expense)}")
    

    print("Centavos:")
    print(f"{int((( money - expense ) % 1)*100)}")
