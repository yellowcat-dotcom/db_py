# предметная область - косметика
# придумать три таблицы
# таблицы дожны состоять больше чем из 2
# таблицы должны быть между собой связаны
# и написать запросы
import sqlite3
import os

con = sqlite3.connect("cosmetics.db")
cur = con.cursor()


def setup_tables():
    cur.execute('''CREATE TABLE  product
                (id_product INTEGER PRIMARE KEY,
                 name_product TEXT,
                 catagory TEXT,
                 type TEXT,
                 id_brend INTEGER,
                 id_stock INTEGER,
                 FOREIGN KEY (id_brend) REFERENCES brend (id_brend),

                 FOREIGN KEY (id_stock) REFERENCES stock (id_stock));''')

    cur.execute('''CREATE TABLE IF NOT EXISTS brend
                (id_brend INTEGER PRIMARE KEY,
                 name_brend TEXT,
                 country TEXT);''')

    cur.execute('''CREATE TABLE IF NOT EXISTS stock
                (id_stock INTEGER PRIMARE KEY,
                 name_stock TEXT,
                 start_stock TEXT,
                 finish_stock TEXT,
                 percent_stock INTEGER);''')


def add_test_data():
    cur.execute("""INSERT INTO product(id_product, name_product, catagory, type, id_brend, id_stock) 
       VALUES('00001', 'pro perfect foundation stick', 'лицо', 'тональные средства','00001', '00002');""")

    cur.execute("""INSERT INTO product(id_product, name_product, catagory, type, id_brend, id_stock) 
       VALUES('00002', 'telescopic', 'глаза', 'тушь для ресниц','00002', '00002');""")

    cur.execute("""INSERT INTO product(id_product, name_product, catagory, type, id_brend, id_stock) 
       VALUES('00003', 'powder puff lippie', 'губы', 'губная помада','00003', '00002');""")

    cur.execute("""INSERT INTO product(id_product, name_product, catagory, type, id_brend, id_stock) 
       VALUES('00004', 'ideal eyebrow palette', ',брови', 'тени для бровей','00004', '00002');""")

    cur.execute("""INSERT INTO product(id_product, name_product, catagory, type, id_brend, id_stock) 
       VALUES('00005', 'eye shadow palette', 'глаза', 'тени для век','00004', '00002');""")

    cur.execute("""INSERT INTO brend(id_brend, name_brend, country) 
       VALUES('00001', 'BODYOGRAPHY', 'США') ;""")

    cur.execute("""INSERT INTO brend(id_brend, name_brend, country) 
       VALUES('00002', 'LOREAL PARIS', 'Франция') ;""")

    cur.execute("""INSERT INTO brend(id_brend, name_brend, country) 
       VALUES('00003', 'NYX PROFESSIONAL MAKEUP', 'США') ;""")

    cur.execute("""INSERT INTO brend(id_brend, name_brend, country) 
       VALUES('00004', 'EVA MOSAIC', 'Россия') ;""")

    cur.execute("""INSERT INTO stock(id_stock, name_stock, start_stock, finish_stock, percent_stock) 
       VALUES('00001', 'Black Friday', '21.11.2022', '30.11.2022', '70') ;""")

    cur.execute("""INSERT INTO stock(id_stock, name_stock, start_stock, finish_stock, percent_stock) 
       VALUES('00002', 'Подарок от Sesderma', '27.10.2022', '31.10.2022', '25') ;""")

    cur.execute("""INSERT INTO stock(id_stock, name_stock, start_stock, finish_stock, percent_stock) 
       VALUES('00003', 'Cкидка −15', '28.12.2022', '31.12.2022', '15') ;""")


def get_all_product_joined():
    cur = con.cursor()
    cur.execute('''
        select name_product, catagory, type,  name_brend, name_stock from product        
        JOIN brend on product.id_brend==brend.id_brend
        JOIN stock on product.id_stock==stock.id_stock
    ''')
    data = cur.fetchall()
    # for d in data:
    # print (d)
    cur.close()
    return data


def get_all_brend_joined():
    cur = con.cursor()
    cur.execute('''
        select name_brend, country from brend
    ''')
    data = cur.fetchall()
    # for d in data:
    # print (d)
    cur.close()
    return data


def get_all_kk_joined():
    cur = con.cursor()
    cur.execute( '''
        SELECT name_stock, start_stock, finish_stock, percent_stock from stock
''')
    data = cur.fetchall()
    for d in data:
        print (d)
    cur.close()
    return data
get_all_kk_joined()


'''def get_all_kk_joined():
    sql=
        SELECT * from stock

    cur=con.cursor()
    cur.execute(sql)
    data=cur.fetchall()
    cur.close()
    return data'''


#setup_tables()
#add_test_data()

# get_all_product_joined()
# get_all_product_joined_1()
# get_all_product_joined_2()

# print()

#con.commit()


print('igig')
