import mysql.connector as c
import streamlit as st
from random import randint

con = c.connect(user='root', password='qwertykp', host='localhost', database='cse202_endsem13')

cur = con.cursor()

nav = st.sidebar.radio("Navigation", ["Home", "Cart", "SignUp/ Login"])
if nav == "SignUp/ Login":
    st.title("Signup/ Login Page")
    login = st.selectbox("How do you want to login?", ["Signup as Customer", "Login as Customer"])
    if login == "Login as Customer":
        username = st.text_input("Username: ")
        queryx = "insert into rough(cust_id) values('{}')".format(username)
        cur.execute(queryx)
        con.commit()
        psswor = st.text_input("Password: ", type="password")
        c1,c2 = st.columns([7,1])
        query1 = "select cust_id from customer"
        cur.execute(query1)
        data1 = cur.fetchall()
        list1 = []
        for i in range(len(data1)):
            list1.append(data1[i][0])
        if c2.button("Submit"):
            if int(username) not in list1:
                st.error("Invalid Username")
            else:
                query2 = "select user_password from uses where cust_id =" + username
                cur.execute(query2)
                data2 = cur.fetchall()
                if psswor == data2[0][0]:
                    st.success("Logged in successfully")
                    st.success("Please go to HomePage")
                else:
                    st.error("Invalid Credentials")
    if login == "Signup as Customer":
        query3 = "select cust_id from customer"
        cur.execute(query3)
        data3 = cur.fetchall()
        query4 = "select email_address from account"
        first, last = st.columns(2)
        first_name = first.text_input("First name")
        last_name = last.text_input("Last name")
        email, space = st.columns([3,1])
        email_id = email.text_input("Email ID")
        cur.execute(query4)
        data4 = cur.fetchall()
        list2 = []
        for i in range(len(data4)):
            list2.append(data4[i][0])
        if email_id in list2:
            st.error("Email ID already registered")
        else:
            passw, phno = st.columns([3, 1])
            passwor = passw.text_input("Password: ", type="password")
            mob = phno.text_input("Phone number")
            st.write("Address")
            house_no, locality, landmark = st.columns([1,1,1])
            housenum = house_no.text_input("House Number")
            loc = locality.text_input("Locality")
            land = landmark.text_input("Landmark")
            city, state = st.columns(2)
            city1 = city.text_input("City")
            state1 = state.text_input("State")
            list = []
            for i in range(len(data3)):
                list.append(data3[i][0])
            n = 0
            while True:
                n = randint(10000, 99999)
                if n not in list:
                    break
                else:
                    continue
            queryy = "insert into rough(cust_id) values('{}')".format(str(n))
            cur.execute(queryy)
            con.commit()
            querzz = "insert into cart(cart_id, total_price) values({},{})".format(n,0)
            cur.execute(querzz)
            con.commit()
            c1, c2 = st.columns([7, 1])
            if c2.button("Submit"):
                query5 = "insert into customer(cust_id, first_name, last_name, contact_no) values({},'{}','{}',{})".format(n,first_name,last_name,mob)
                cur.execute(query5)
                con.commit()
                query6 = "insert into account(email_address, house_no, locality, landmark, city, state) values('{}','{}','{}','{}','{}','{}')".format(email_id, housenum, loc, land, city1, state1)
                cur.execute(query6)
                con.commit()
                query8 = "insert into uses(user_password, email_address, cust_id) values('{}','{}',{})".format(passwor, email_id, n)
                cur.execute(query8)
                con.commit()
                st.success("You have been successfully registered")
                st.info("Your Username is: " + str(n) + ". Please remember it")
                st.success("Now you can go to HomePage")

if nav == "Home":
    st.markdown("""# Home""")
    cat = st.radio("Categories",["Clothing", "Jewellery", "Home Appliances", "Health and Beauty", "Footwear", "Search Products"])
    if cat == "Clothing":
        order = st.selectbox("Sort By", ["Normal", "Price High to Low", "Price Low to High"])
        st.write(" ")
        x, y, z = st.columns([1, 3, 1])
        x.write("Products Name")
        z.write("Product Price")
        st.write("-------------------------------------------------------------------------------")
        if order == "Normal":
            query7 = "select * from products where category = 'clothing'"
            cur.execute(query7)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1,3,1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price High to Low":
            query9 = "select * from products where category = 'clothing' order by price desc"
            cur.execute(query9)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price Low to High":
            query10 = "select * from products where category = 'clothing' order by price asc"
            cur.execute(query10)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")
    if cat == "Jewellery":
        order = st.selectbox("Sort By", ["Normal", "Price High to Low", "Price Low to High"])
        st.write(" ")
        x, y, z = st.columns([1, 3, 1])
        x.write("Products Name")
        z.write("Product Price")
        st.write("-------------------------------------------------------------------------------")
        if order == "Normal":
            query7 = "select * from products where category = 'jewellery'"
            cur.execute(query7)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1,3,1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price High to Low":
            query9 = "select * from products where category = 'jewellery' order by price desc"
            cur.execute(query9)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price Low to High":
            query10 = "select * from products where category = 'jewellery' order by price asc"
            cur.execute(query10)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

    if cat == "Home Appliances":
        order = st.selectbox("Sort By", ["Normal", "Price High to Low", "Price Low to High"])
        st.write(" ")
        x, y, z = st.columns([1, 3, 1])
        x.write("Products Name")
        z.write("Product Price")
        st.write("-------------------------------------------------------------------------------")
        if order == "Normal":
            query7 = "select * from products where category = 'home appliances'"
            cur.execute(query7)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1,3,1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price High to Low":
            query9 = "select * from products where category = 'home appliances' order by price desc"
            cur.execute(query9)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price Low to High":
            query10 = "select * from products where category = 'appliances' order by price asc"
            cur.execute(query10)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")


    if cat == "Health and Beauty":
        order = st.selectbox("Sort By", ["Normal", "Price High to Low", "Price Low to High"])
        st.write(" ")
        x, y, z = st.columns([1, 3, 1])
        x.write("Products Name")
        z.write("Product Price")
        st.write("-------------------------------------------------------------------------------")
        if order == "Normal":
            query7 = "select * from products where category = 'health and beauty'"
            cur.execute(query7)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1,3,1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price High to Low":
            query9 = "select * from products where category = 'health and beauty' order by price desc"
            cur.execute(query9)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price Low to High":
            query10 = "select * from products where category = 'health and beauty' order by price asc"
            cur.execute(query10)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

    if cat == "Footwear":
        order = st.selectbox("Sort By", ["Normal", "Price High to Low", "Price Low to High"])
        st.write(" ")
        x, y, z = st.columns([1, 3, 1])
        x.write("Products Name")
        z.write("Product Price")
        st.write("-------------------------------------------------------------------------------")
        if order == "Normal":
            query7 = "select * from products where category = 'footwear'"
            cur.execute(query7)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1,3,1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price High to Low":
            query9 = "select * from products where category = 'footwear' order by price desc"
            cur.execute(query9)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

        if order == "Price Low to High":
            query10 = "select * from products where category = 'footwear' order by price asc"
            cur.execute(query10)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1, 3, 1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

    if cat == "Search Products":
        search = st.text_input("Search bar")
        sp, ent = st.columns([1,5])
        if sp.button("Enter"):
            x, y, z = st.columns([1, 3, 1])
            x.write("Products Name")
            z.write("Product Price")
            st.write("-------------------------------------------------------------------------------")
            query7 = "select * from products where product_name like '%" + search + "%'"
            cur.execute(query7)
            data5 = cur.fetchall()
            for i in range(len(data5)):
                name, space, price = st.columns([1,3,1])
                name.write(data5[i][2])
                price.write(data5[i][3])
                quantity = st.text_input("Quantity", key=i)
                space1, add_cart = st.columns([5, 1])
                st.write("-------------------------------------------------------------------------------")
                if add_cart.button("Add to Cart", key=i):
                    print("hello")
                    if int(quantity) < data5[i][4]:
                        query12 = "select cust_id from rough"
                        cur.execute(query12)
                        data7 = cur.fetchall()
                        username = data7[-1][0]
                        query10 = "select email_address from uses where cust_id =" + username
                        cur.execute(query10)
                        data6 = cur.fetchall()
                        query11 = "insert into manages(email_address, product_id, cart_id, quant) values('{}',{},{},{})".format(data6[0][0], data5[i][0], int(username), int(quantity))
                        cur.execute(query11)
                        con.commit()
                    else:
                        st.error("Not Available")

if nav == "Cart":
    query13 = "select cust_id from rough"
    cur.execute(query13)
    data8 = cur.fetchall()
    username = data8[-1][0]
    query14 = "select * from manages where cart_id =" + username
    cur.execute(query14)
    data9 = cur.fetchall()
    x, s1, y, s2, z = st.columns(5)
    x.write("Products Name")
    y.write("Quantity")
    z.write("Total Product Price")
    for i in range(len(data9)):
        query15 = "select product_name, price from products where product_id =" + str(data9[i][1])
        cur.execute(query15)
        data10 = cur.fetchall()
        p, s3, q, s4, pr = st.columns(5)
        p.write(data10[0][0])
        q.write(data9[i][3])
        pr.write(data9[i][3] * data10[0][1])
    s5, tot = st.columns([4,1])
    query20 = "select * from cart where cart_id =" + username
    cur.execute(query20)
    data100 = cur.fetchall()
    tot.write("Total Cost = " + str(data100[0][1]))
    pmethod = st.radio("Payment Method", ["Debit Card", "Credit Card", "NetBanking", "UPI"])
    s6, payment = st.columns([4, 1])
    pay = payment.button("Pay")
    if pay:
        if pmethod == "Debit Card" or "Credit Card" or "NetBanking" or "UPI":
            query22 = "select payment_id from payment"
            cur.execute(query22)
            data12 = cur.fetchall()
            st.success("Payment Success")
            list = []
            for i in range(len(data12)):
                list.append(data12[i][0])
            n1 = 0
            while True:
                n1 = randint(10000, 99999)
                if n1 not in list:
                    break
                else:
                    continue
            query23 = "insert into payment(payment_id, cart_id, total_cost, payment_method) values({},{},{},'{}')".format(n1, int(username), data100[0][1], pmethod)
            cur.execute(query23)
            con.commit()
            query21 = "Select current_date() + 4"
            cur.execute(query21)
            data11 = cur.fetchall()
            mn = str(data11[0][0])
            mn = mn[0:4] + "-" + mn[4: len(mn)]
            mn = mn[0:7] + "-" + mn[7:len(mn)]
            st.info("Your order will be delivered by " + mn)
            query24 = "update cart set total_price = 0 where cart_id =" + username
            cur.execute(query24)
            con.commit()
            query25 = "delete from manages where cart_id =" + username
            cur.execute(query25)
            con.commit()


