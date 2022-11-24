import cgi
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db


msg = ''
#name_product, catagory, type, id_brend, id_stock
form = cgi.FieldStorage()
name_product= form.getfirst("name_product")
catagory = form.getfirst("catagory")
type = form.getfirst("type")
id_brend = form.getfirst("id_brend")
id_stock = form.getfirst("id_stock")
if (name_product is not None) and (catagory is not None) and (type is not None) and (id_brend is not None) and (id_stock is not None):
    db.add_product(name_product, catagory, type, id_brend, id_stock)
    msg = '''
        <br>
        <div class="card">
            <div class="card-body">
                Продукт успешно добавлен
            </div>
        </div>
    '''

brends = db.get_all_brend_joined()
stocks = db.get_all_kk_joined()

template = '''
    <!DOCTYPE html>
    <html lang="en-US">
        <head>
            <meta charset="UTF-8">
            <!-- CSS only -->
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
            <!-- JavaScript Bundle with Popper -->
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
        </head>
        <body>
            <h1>Создание продукта</h1>
            <a class="h3 link-primary" href="/">На главную</a>
            <div class="ps-4 pe-4">
                <form method="GET">                    
                    <br>
                    <label class="form-label" for="name_product">Имя</label>
                    <input class="form-control" type="text" name="name_product" required>
                    <br>
                    <label class="form-label" for="catagory">Категория</label>
                    <input class="form-control" type="text" name="catagory" required>
                    <br>
                    <label class="form-label" for="type">Тип</label>
                    <input class="form-control" type="text" name="type" required>
                    <br>
                    <label class="form-label" for="id_brend">Бренд</label>
                    <select class="form-select" aria-label="Default select example" name="id_brend" required>
                        {brend_options}
                    </select>
                    <label class="form-label" for="id_stock">Скидка</label>
                    <select class="form-select" aria-label="Default select example" name="id_stock" required>
                        {stock_options}
                    </select>
                    <input type="submit" class="btn btn-primary">
                </form>

                {msg}
            </div>
        </body>
    </html>
'''

brend_options = ''
for brend in brends:
    brend_options += f'<option value="{brend[0]}">{brend[1]}</option>'

stock_options = ''
for stock in stocks:
    stock_options += f'<option value="{stock[0]}">{stock[1]}</option>'

print("Content-Type: text/html\n")
print(template.format(msg=msg, brend_options=brend_options,stock_options=stock_options))
