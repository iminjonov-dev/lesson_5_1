from connect import Database

def create_table():
    product = """
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            description VARCHAR(500),
            title VARCHAR(350),
            price INTEGER,
            create_date TIMESTAMP DEFAULT now())
        """,

    category = """
            CREATE TABLE category(
                category_id SERIAL PRIMARY KEY,
                name VARCHAR(30),
                last_update TIMESTAMP DEFAULT now())
        """


    product_category = """
        CREATE TABLE product_category(
        product_category_id SERIAL  PRIMARY KEY,
        product_id INT REFERENCES product(product_id),
        category_id INT REFERENCES category(category_id))"""


    color = """
        CREATE TABLE color(
            color_id SERIAL PRIMARY KEY ,
            name VARCHAR(30),
            product_id INT REFERENCES product(product_id)
    """

    adres_table ="""
         CREATE TABLE adres(
            adres_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            last_update TIMESTAMP DEFAULT now())
    """

    store = """
        CREATE TABLE store(
            store_id SERIAL PRIMARY KEY,
            nmae VARCHAR(30),
            adres_id INT REFERENCES adress(adres_id))
    """

    customer = """
        CREATE TABLE customer(
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(30),
            password TEXT,
            brith_date DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """



    payment_table = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            card INT,
            cash INT)
    """



    data = {
        "product": product,
        "category": category,
        "product_category": product_category,
        "color": color,
        "adres_table": adres_table,
        "store": store,
        "customer": customer,
        "payment_table": payment_table
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()