# предметная область - косметика
# придумать три таблицы
# таблицы дожны состоять больше чем из 2
# таблицы должны быть между собой связаны
# и написать запросы
import sqlite3
import os

con = sqlite3.connect("cosmetics.db")
#cur = con.cursor()
tables_whitelist = [
    'brends',
    'stocks',
    'produkts'
]

def setup_tables():
    con.execute('''CREATE TABLE IF NOT EXISTS brend
                (id_brend INTEGER PRIMARY KEY autoincrement,
                 name_brend TEXT,
                 country TEXT);''')

    con.execute('''CREATE TABLE IF NOT EXISTS stock
                (id_stock INTEGER PRIMARY KEY autoincrement,
                 name_stock TEXT,
                 start_stock TEXT,
                 finish_stock TEXT,
                 percent_stock INTEGER);''')

    con.execute('''CREATE TABLE  product
                    (id_product INTEGER PRIMARY KEY autoincrement,
                     name_product TEXT,
                     catagory TEXT,
                     type TEXT,
                     id_brend INTEGER,
                     id_stock INTEGER,
                     FOREIGN KEY (id_brend) REFERENCES brend (id_brend),
                     FOREIGN KEY (id_stock) REFERENCES stock (id_stock));''')

#INSERT INTO brend(id_brend, name_brend, country) VALUES
def add_test_data():
    con.execute("""
        INSERT INTO brend(name_brend, country) VALUES
        ('BODYOGRAPHY', 'США'),
        ('LOREAL PARIS', 'Франция'),
        ('NYX PROFESSIONAL MAKEUP', 'США'),
        ('EVA MOSAIC', 'Россия')
    """)
#INSERT INTO stock(id_stock, name_stock, start_stock, finish_stock, percent_stock) VALUES
    con.execute("""
        INSERT INTO stock(name_stock, start_stock, finish_stock, percent_stock) VALUES
        ('Black Friday', '21.11.2022', '30.11.2022', 70),
        ('Подарок от Sesderma', '27.10.2022', '31.10.2022', 25),
        ('Cкидка −15%', '28.12.2022', '31.12.2022', 15)
    """)
#INSERT INTO product(name_product, catagory, type, id_brend, id_stock) VALUES
    con.execute("""
            INSERT INTO product(name_product, catagory, type, id_brend, id_stock) VALUES
           ('pro perfect foundation stick', 'лицо', 'тональные средства',1, 2),
           ('telescopic', 'глаза', 'тушь для ресниц',2, 2),
           ('powder puff lippie', 'губы', 'губная помада',3, 2),
           ('ideal eyebrow palette', 'брови', 'тени для бровей',4, 2),
           ('eye shadow palette', 'глаза', 'тени для век',4, 2)      
    """)


def get_all_product_joined():
    cur = con.cursor()
    cur.execute('''
        select name_product, catagory, type,  name_brend, name_stock from product        
        JOIN brend on product.id_brend==brend.id_brend
        JOIN stock on product.id_stock==stock.id_stock
    ''')
    data = cur.fetchall()
    #for d in data:
        #print(d)

    cur.close()
    return data


def get_all_brend_joined():
    cur = con.cursor()
    cur.execute('''
        select id_brend,name_brend, country from brend
    ''')
    data = cur.fetchall()
    # for d in data:
    # print (d)
    cur.close()
    return data


def get_all_kk_joined():
    cur = con.cursor()
    cur.execute( '''
        SELECT id_stock, name_stock, start_stock, finish_stock, percent_stock from stock
''')
    data = cur.fetchall()
    #for d in data:
     #   print (d)
    cur.close()
    return data

def execute_fetch(sql):  # новая функция
    cur = con.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data

def execute_insert_commit(sql, data):  # новая функция
    cur = con.cursor()
    cur.execute(sql, data)
    con.commit()


def add_brend(name_brend, country):
    sql = 'INSERT INTO brend(name_brend, country) VALUES (?, ?)'
    execute_insert_commit(sql, (name_brend, country))


def add_stock(name_stock, start_stock, finish_stock, percent_stock):
    sql = 'INSERT INTO stock(name_stock,start_stock, finish_stock, percent_stock) VALUES (?, ?, ?, ?)'
    execute_insert_commit(sql, (name_stock, start_stock, finish_stock, percent_stock))

def add_product(name_product, catagory, type, id_brend, id_stock):
    sql = 'INSERT INTO Tracks(name_product, catagory, type, id_brend, id_stock ) VALUES (?, ?, ?, ?, ?)'
    execute_insert_commit(sql, (name_product, catagory, type, id_brend, id_stock))


#name_product, catagory, type, id_brend, id_stock
#setup_tables()
#add_test_data()
#con.commit()


print('igig')
