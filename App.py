#Importacion de flask para crear y ejecutar sitio web, renderizar plantillas
from flask import Flask, render_template

#Instanciacion de flask dentro de la variable app
app = Flask(__name__)

#Variables a utilizar
Colores = [];

#Creacion de la ruta principal del sitio web y texto de prueba
@app.route('/')
def Inicio():
    return render_template('Color.html', Colores = Colores)

#Inializacion del sitio web para correr(modo debug encendido para detectar cambios)
if __name__ == '__main__':
    app.run(debug=True)