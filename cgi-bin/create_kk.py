import cgi
import sys
import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db

#name_stock, start_stock, finish_stock, percent_stock

msg = ''

form = cgi.FieldStorage()
name_stock = form.getfirst("name_stock")
start_stock = form.getfirst("start_stock")
finish_stock = form.getfirst("finish_stock")
percent_stock = form.getfirst("percent_stock")
if (name_stock is not None) and (start_stock is not None) and (finish_stock is not None) and (percent_stock is not None):
    db.add_stock(name_stock, start_stock, finish_stock, percent_stock)
    msg = '''
        <br>
        <div class="card">
            <div class="card-body">
                Скидка успешно добавлена
            </div>
        </div>
    '''

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
            <h1>Создание артиста</h1>
            <a class="h3 link-primary" href="/">На главную</a>
            <div class="ps-4 pe-4">
                <form method="GET">
                    <label class="form-label" for="name_stock">Имя</label>
                    <input class="form-control" type="text" name="name_stock" required>
                    <br>
                    <label class="form-label" for="start_stock">Начало</label>
                    <input class="form-control" type="text" name="start_stock" required>
                    <br>
                    <label class="form-label" for="finish_stock">Конец</label>
                    <input class="form-control" type="text" name="finish_stock" required>
                    <br>
                    <label class="form-label" for="percent_stock">Процент</label>
                    <input class="form-control" type="text" name="percent_stock" required>
                    <br>
                    <input type="submit" class="btn btn-primary">
                </form>

                {msg}
            </div>
        </body>
    </html>
'''


print("Content-Type: text/html\n")
print(template.format(msg=msg))