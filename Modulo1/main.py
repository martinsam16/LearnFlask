from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def antesPeticion():
    print('Antes de la petición!')

@app.after_request
def despuesPeticion(response): #La respuesta de la función de la petición
    print('Después de la petición')
    return response

@app.route('/')
def index():
    name = 'Martin'
    is_premium = True
    cursos = ['Python', 'Java', 'Elixir']
    return render_template('index.html', username=name, is_premium=is_premium, cursos=cursos)

# Para rutas dinámicas
@app.route('/usuario/<username>/<int:id>')
def usuario(username, id):
    return 'Hola ' + username + ', tu id es: ' + str(id)

# Para Query Strings
@app.route('/datos')
def datos():
    nombre = request.args.get('nombre')  # Retorna un dict
    curso = request.args.get('curso')
    #http://localhost:5000/datos?nombre=data1&curso=demo
    return 'Listado de datos '+nombre+' tu curso es: '+curso


@app.route('/about')
def about():
    print('About')
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
