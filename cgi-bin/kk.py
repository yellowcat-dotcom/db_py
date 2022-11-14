import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import db

dances = db.get_all_kk_joined()
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
            <h1>Список продуктов:</h1>
            <table>
                <tr>
                    
                    <th>Имя</th>
                    <th>Начало</th>
                    <th>Конец </th>
                    <th>Процент</th>
                                       
                </tr>
                {rows_html}
            </table>
        </body>
    </html>
'''

rows_html = ""
for dance in dances:
    rows_html += "<tr>"
    rows_html += f"<td>{dance[0]}</td>"
    rows_html += f"<td>{dance[1]}</td>"
    rows_html += f"<td>{dance[2]}</td>"
    rows_html += f"<td>{dance[3]}</td>"



    rows_html += "</tr>"

print("Content-Type: text/html\n")
print(template.format(rows_html=rows_html))
