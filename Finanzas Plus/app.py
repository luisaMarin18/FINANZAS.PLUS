from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave-secreta'  # Necesaria para flash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['name']
    correo = request.form['email']
    mensaje = request.form['message']

    # Aquí podrías integrar envío real por correo
    print(f"Mensaje recibido de {nombre} ({correo}): {mensaje}")

    flash('¡Gracias por tu mensaje! Te responderemos pronto.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
