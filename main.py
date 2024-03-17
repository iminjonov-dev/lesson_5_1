
import classes


def main():
    table = input("""
        1.Product
        2.Category
        3.Color
        4.Adress
        5.Store
        6.Customer
        7.Payment
                >>>>
    """)


    if table == "1":
        print("Product.")
        def tanlash():
            status = """
                1.Insert
                2.Update
                3.Delete
                4.Select
                 """
            if status == "1":
                return classes.Product.insert()
            elif status == "2":
                return classes.Product.update()
            elif status == "3":
                return classes.Product.delete()
            elif status == "4":
                return classes.Product.select()
            else:
                print("Invalid")
                return tanlash()
    elif table == "2":
        print("Category.")

        def tanlash():
            status = """
                        1.Insert
                        2.Update
                        3.Insert
                        4.Select
                         """
            if status == "1":
                return classes.Category.insert()
            elif status == "2":
                return classes.Category.update()
            elif status == "3":
                return classes.Category.delete()
            elif status == "4":
                return classes.Product.select()
            else:
                print("Invalid")
                return tanlash()
    elif table == "3":
        print("Color.")
        def tanlash():
            status = """
                        1.Insert
                        2.Update
                        3.Delete
                        4.Select
                         """
            if status == "1":
                return classes.Color.insert()
            elif status == "2":
                return classes.Color.update()
            elif status == "3":
                return classes.Color.delete()
            elif status == "4":
                return classes.Color.select()
            else:
                print("Invalid")
                return tanlash()
    elif table == "4":
        print("Adress.")
        def tanlash():
            status = """
                        1.Insert
                        2.Update
                        3.Delete
                        4.Select
                         """
            if status == "1":
                return classes.Adress.insert()
            elif status == "2":
                return classes.Adress.update()
            elif status == "3":
                return classes.Adress.delete()
            elif status == "4":
                return classes.Adress.select()
            else:
                print("Invalid")
                return tanlash()
    elif table == "5":
        print("Store.")
        def tanlash():
            status = """
                        1.Insert
                        2.Update
                        3.Delete
                        4.Select
                         """
            if status == "1":
                return classes.Store.insert()
            elif status == "2":
                return classes.Store.update()
            elif status == "3":
                return classes.Store.delete()
            elif status == "4":
                return classes.Store.select()
            else:
                print("Invalid")
                return tanlash()
    elif table == "6":
        print("Customer.")
        def tanlash():
            status = """
                        1.Insert
                        2.Update
                        3.Delete
                        4.Select
                         """
            if status == "1":
                return classes.Customer.insert()
            elif status == "2":
                return classes.Customer.update()
            elif status == "3":
                return classes.Customer.delete()
            elif status == "4":
                return classes.Customer.select()
            else:
                print("Invalid")
                return tanlash()
    elif table == "7":
        print("Payment.")
        def tanlash():
            status = """
                        1.Insert
                        2.Update
                        3.Delete
                        4.Select
                         """
            if status == "1":
                return classes.Payment.insert()
            elif status == "2":
                return classes.Payment.update()
            elif status == "3":
                return classes.Payment.delete()
            elif status == "4":
                return classes.Payment.select()
            else:
                print("Invalid")
                return tanlash()
    else:
        print("Invalid.")
        return main()








if __name__ == "__main__":
    main()




