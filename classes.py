from connect import Database

class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Database.connect(query, "select")

    @staticmethod
    def delete_id(table, id):
        query = f"DELETE FROM {table} WHERE student_id = {id}"
        return Database.connect(query, "delete")

    @staticmethod
    def update_id(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = {new_data} WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = '{new_data}' WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")


    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"
        return Database.connect(query, "delete")

    @staticmethod
    def delete_id(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Database.connect(query, "delete")

class Product(Base):
    def __init__(self, name, description, title,  price):
        self.name = name
        self.description = description
        self.price = price
        self.title = title


    def insert(self):
        query = f"INSERT INTO product(name, description, price, title) VALUES ('{self.name}', '{self.description}', '{self.price}', '{self.title}"
        return Database.connect(query, "insert")

    @staticmethod
    def update(colum_name, old_data, new_data):
        query = f"UPDATE product SET {colum_name} = {new_data} WHERE {colum_name} = '{old_data}"
        return Database.connect(query, "update")

    @staticmethod
    def select():
        query = f"SELECT * FROM product"
        return Database.connect(query, "Select")


    @staticmethod
    def delete(colum_name, old_data):
        if colum_name == int:
            query = f"DELETE FROM product WHERE {colum_name} ='{old_data}'"
        else:
            query = f"DELETE FROM product WHERE {colum_name} ={old_data}"
        return Database.connect(query, "Delete")



class Category(Base):
    def __init__(self, name, last_update):
        self.name = name
        self.last_update = last_update

    def insert(self):
        query = f"INSERT INTO category(name) VALUES ('{self.name}')"
        return Database.connect(query, "Insert")

    @staticmethod
    def update(colum_name, old_data, new_data):
        query = f"UPDATE category SET {colum_name} ='{old_data}' WHERE { colum_name} ='{new_data}'"
        return Database.connect(query, "Update")

    @staticmethod
    def select():
        query = f"SELECT * FROM category"
        return Database.connect(query, "Select")

    @staticmethod
    def delete(colum_name, old_data):
        if colum_name == int:
            query = f"DELETE FROM category WHERE { colum_name} ='{old_data}'"
        else:
            query = f"DELETE FROM category WHERE {colum_name} = ={old_data}"
        return Database.connect(query, "Delete")

class Color(Base):
    def __init__(self, name, last_update):
        self.name = name
        self.last_update = last_update

    def insert(self):
        query = f"INSERT INTO color(name) VALUES ('{self.name}')"
        return Database.connect(query, "Insert")

    @staticmethod
    def update(colum_name, old_data, new_data):
        query = f"UPDATE color SET {colum_name} =' {old_data}' WHERE { colum_name} ='{ new_data}"
        return Database.connect(query, "Update")

    @staticmethod
    def select(colum_name, old_data):
        if colum_name == int:
            query = f"SELECT * FROM color WHERE { colum_name} ='{old_data}'"
        else:
            query = f"DELETE FROM color WHERE {colum_name} = ={old_data}"
        return Database.connect(query, "Select")

    @staticmethod
    def delete(colum_name, old_data):
        if colum_name == int:
            query = f"DELETE FROM color WHERE { colum_name} ='{old_data}'"
        else:
            query = f"DELETE FROM color WHERE { colum_name} ={old_data}"
        return Database.connect(query, "Delete")



class Adress(Base):
    def __init__(self, name, last_update):
        self.name = name
        self.last_update = last_update

    def insert(self):
        query = f"INSERT INTO address(name) VALUES ('{self.name}')"
        return Database.connect(query, "Insert")

    @staticmethod
    def select():
        query = f"SELECT * FROM address"
        return Database.connect(query, "Select")

    @staticmethod
    def delete(colum_name, old_data):
        if colum_name == int:
            query = f"DELETE FROM address WHERE { colum_name} ='{old_data}' "
        else:
            query = f"DELETE FROM address WHERE { colum_name} ={old_data}"
        return Database.connect(query, f"Delete")


    @staticmethod
    def update(colum_name, old_data, new_data):
        if colum_name == int:
            query = f"UPDATE address SET {colum_name} ='{ new_data}' WHERE { colum_name} ='{old_data}'"
        else:
            query = f"UPDATE address SET {colum_name} ='{ new_data}' WHERE { colum_name} ={old_data}"
        return Database.connect(query, "Update")


class Store(Base):
    def __init__(self, name, address_id):
        self.name = name
        self.address_id = address_id

    def insert(self):
        query = f"INSERT INTO store(name) VALUES ('{self.name}')"
        return Database.connect(query, "Insert")

    @staticmethod
    def select():
        query = f"SELECT * FROM store"
        return Database.connect(query, "Select")

    @staticmethod
    def delete( colum_name, old_data ):
        if colum_name == int:
            query = f"DELETE FROM store WHERE { colum_name} ='{old_data}' "
        else:
            query = f"DELETE FROM store WHERE { colum_name} ={old_data} "
        return Database.connect(query, f"Delete")


    @staticmethod
    def update(colum_name, old_data, new_data):
        if colum_name == int:
            query = f"UPDATE store SET {colum_name} =' {new_data}' WHERE { colum_name} ='{old_data}'"
        else:
            query = f"UPDATE store SET {colum_name} =' {new_data}' WHERE { colum_name} ={old_data}"
        return Database.connect(query, "Update")


class Customer(Base):
    def __init__(self, first_name, last_name, email, password, brith_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.brith_date = brith_date

    def insert(self):
        query = f"INSERT INTO customer(first_name, last_name, email, password) VALUES ('{self.first_name} {self.last_name} {self.email}', '{self.password} {self.brith_date}')"
        return Database.connect(query, "Insert")


    @staticmethod
    def select():
        query = f"SELECT * FROM customer"
        return Database.connect(query, "Select")

    @staticmethod
    def delete( colum_name, old_data ):
        if colum_name == int:
            query = f"DELETE FROM customer WHERE { colum_name} =' {old_data}'"
        else:
            query = f"DELETE FROM customer WHERE { colum_name} = {old_data}"
        return Database.connect(query, "Delete")

    @staticmethod
    def update(colum_name, old_data, new_data):
        query = f"UPDATE customer SET {colum_name} =' {new_data}' WHERE { colum_name} ={old_data}"
        return Database.connect(query, "Update")

class Payment(Base):
    def __init__(self, card, cash):
        self.card = card
        self.cash = cash

    def insert(self):
        query = f"INSERT INTO payment(card, cash) VALUES ('{self.card}, {self.cash}')"
        return Database.connect(query, "Insert")


    @staticmethod
    def select():
        query = f"SELECT * FROM payment"
        return Database.connect(query, "Select")

    @staticmethod
    def delete( colum_name, old_data ):
        if colum_name == int:
            query = f"DELETE FROM payment WHERE { colum_name} =' {old_data}'"
        else:
            query = f"DELETE FROM payment WHERE { colum_name} = {old_data}"
        return Database.connect(query, "Delete")


    @staticmethod
    def update(colum_name, old_data, new_data):
        if colum_name == int:
            query = f"UPDATE payment SET {colum_name} =' { new_data}' WHERE { colum_name} = ' { old_data}'"
        else:
            query = f"UPDATE payment SET {colum_name} =' { new_data}' WHERE { colum_name} ={ old_data}"
        return Database.connect(query, "Update")

