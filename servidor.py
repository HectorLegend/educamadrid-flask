from flask import Flask, request, render_template_string

app = Flask(__name__)

# Página con el formulario
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de favoritos</title>
</head>
<body>
    <h2>Rellena tus favoritos</h2>
    <form action="/enviar" method="post">
        Comida favorita: <input type="text" name="comida"><br>
        Animal favorito: <input type="text" name="animal"><br>
        Deporte favorito: <input type="text" name="deporte"><br>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(form_html)

# Ruta que recibe los datos del formulario
@app.route('/enviar', methods=['POST'])
def recibir_datos():
    comida = request.form.get('comida')
    animal = request.form.get('animal')
    deporte = request.form.get('deporte')

    # Guardar en un archivo
    with open("datos_favoritos.txt", "a") as f:
        f.write(f"Comida: {comida}, Animal: {animal}, Deporte: {deporte}\n")

    return f"Gracias! Datos recibidos: Comida={comida}, Animal={animal}, Deporte={deporte}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
