def input_product():
    products = {}
    while True:
        name = input("Введіть назву товару або 'stop' щоб закінчити: ")
        if name.lower() == 'stop':
            break
        try:
            price = float(input(f"Введіть ціну для товару {name}: "))
            stock = int(input(f"Введіть кількість на складі для {name}: "))
        except ValueError:
            print("Помилка! Введіть правильні дані (ціна - число, кількість - ціле).")
            continue

        products[name] = {'Ціна': price, 'Залишок': stock}

    return products
