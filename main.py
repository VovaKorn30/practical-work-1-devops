from data_input import input_product
from calculations import calculate_stock_value, calculate_discount
from general import print_product_names, find_product_by_name


def main():
    products = input_product()
    print("\nВведені товари:")
    print(products)

    print("\nРозрахунок вартості залишків:")
    calculate_stock_value(products)

    print("\nРозрахунок знижок:")
    calculate_discount(products)

    print("\nСписок товарів:")
    product_names = list(products.keys())
    print_product_names(product_names)

    print("\nПошук товару:")
    find_product_by_name(products, "Товар2")


if __name__ == "__main__":
    main()
