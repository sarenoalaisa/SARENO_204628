
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code, property):
    return products[code][property]

def main():

    customer_order = {}
    total = 0

    while (True):
        order = input("Please input the customer's order in this format: {product_code},{quantity}. ")

        if order != "/":
            code = order.split(",")[0]
            quantity = int(order.split(",")[1])

            if code not in customer_order:
                customer_order[code] = quantity
            else:
                customer_order[code] += quantity

        elif order == "/":
            break

        with open('receipt.txt', 'w') as f:

            f.write("""
        ==
        CODE\t\t\t\t\t\t\t\tNAME\t\t\t\t\t\t\t\t  QUANTITY\t\t\t\t\t\t\t\tSUBTOTAL\n""")

            for i in sorted(customer_order):
                name = get_product(i)["name"]
                subtotal = float(get_property(i, "price") * quantity)
                f.write("        {:<14}      {:<20}\t{:<20}\t\t{:<20}\n".format(i, name, customer_order[i], subtotal))
                total += subtotal

            f.write("""
        Total:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{:<8}
        ==
        """.format(total))

main()
