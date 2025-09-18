def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Ціна'] * details['Залишок']
        print(f"Вартість залишку для {product}: {stock_value} грн (ціна: {details['Ціна']}, кількість: {details['Залишок']})")


def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Залишок'] < 10:
            discount = details['Ціна'] * 0.05
            new_price = details['Ціна'] - discount
            print(f"Знижка для {product}: {discount:.2f} грн. Нова ціна: {new_price:.2f} грн (залишок: {details['Залишок']})")
        else:
            print(f"Для {product} знижка не застосовується (залишок: {details['Залишок']})")
