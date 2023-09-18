from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    resultado = None
    
    if request.method == 'POST':
        inicio = int(request.form['inicio'])
        fin = int(request.form['fin'])
        
        # Calcula la suma de números pares en el rango
        suma_pares = sum(x for x in range(inicio, fin + 1) if x % 2 == 0)
        resultado = f"La suma de números pares entre {inicio} y {fin} es {suma_pares}"
    
    return render_template('formulario.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
