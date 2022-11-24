import cgi
import sys
import os
import inspect
import xml.etree.ElementTree as ET
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db


msg = ''

form = cgi.FieldStorage()
name_brend = form.getfirst("name_brend")
country = form.getfirst("country")

if (name_brend is not None) and (country is not None):
    db.add_brend(name_brend, country)
    msg = '''
        <br>
        <div class="card">
            <div class="card-body">
                Бренд успешно добавлен
            </div>
        </div>
    '''

brend_xml = form.getfirst("xml_file")
if brend_xml is not None:
    root = ET.fromstring(brend_xml.decode("utf-8"))
    success_cnt = 0
    for child in root:
        brend = {}
        for a_ch in child:
            if a_ch.tag == 'name_brend':
                brend['name_brend'] = a_ch.text
            if a_ch.tag == 'country':
                brend['country'] = a_ch.text
        if ('name_brend' in brend) and ('country' in brend):
            db.add_brend(brend['name_brend'], brend['country'])
            success_cnt += 1

    msg = f'''
        <br>
        <div class="card">
            <div class="card-body">
                Успешно загружено {success_cnt} брендов
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
            <h1>Создание бренда</h1>
            <a class="h3 link-primary" href="/">На главную</a>
            <div class="ps-4 pe-4">
                <form method="GET">
                    <label class="form-label" for="name_brend">Имя бренда</label>
                    <input class="form-control" type="text" name="name_brend" required>
                    <br>
                    <label class="form-label" for="country">Страна бренда</label>
                    <input class="form-control" type="text" name="country" required>
                    <br>
                    <input type="submit" class="btn btn-primary">
                </form>

                {msg}
            </div>
            <h1>Загрузить из XML</h1>
             <div class="ps-4 pe-4">
                <form method="post" enctype="multipart/form-data">
                    <label class="form-label" for="xml_file">XML Файл</label>
                    <input class="form-control" name="xml_file" type="file" accept=".xml">
                    <br>
                    <input type="submit" class="btn btn-primary">
                </form>
             </div>
        </body>
    </html>
'''


print("Content-Type: text/html\n")
print(template.format(msg=msg))