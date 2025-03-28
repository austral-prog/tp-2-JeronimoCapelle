def change():
    expense = 23.75
    money = 100

    expense = float(input("Ingresar gasto:\n"))
    print(expense)
    money = float(input("Dinero recibido\n"))
    print(int(money))
    
    print
    print(f"\nVuelto\n\nPesos:\n{int(money - expense)}\nCentavos:\n{int(((money - expense) % 1)*100)}")
