# IMPORTAR LAS HERRAMIENTAS DE FLASK
from flask import Flask, render_template, request

app = Flask(__name__)

# MENU PRINCIPAL
@app.route("/")
def inicio():
    return render_template("index.html")

# EJERCICIO 1: FORMULARIO DE NOTAS
@app.route("/ejercicio1")
def ejercicio1():
    return render_template("ejercicio1.html")

# PROCESAR NOTAS
@app.route("/procesar_notas", methods=["POST"])
def procesar_notas():
    try:
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])
        asistencia = float(request.form["asistencia"])

        # Validar rangos de notas y asistencia
        if not all(10 <= nota <= 70 for nota in
                   [nota1, nota2, nota3]):
            raise ValueError("Las notas deben estar entre 10 y 70.")

        if not 0 <= asistencia <= 100:
            raise ValueError("La asistencia debe estar entre 0 y 100.")

        # Validar números enteros
        if not all(valor.is_integer() for valor in
                   [nota1, nota2, nota3, asistencia]):
            raise ValueError("Ingrese solamente números enteros.")

        # Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Determinar estado
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template(
            "ejercicio1.html",
            nota1=int(nota1),
            nota2=int(nota2),
            nota3=int(nota3),
            promedio=round(promedio, 2),
            asistencia=int(asistencia),
            estado=estado
        )

    except (ValueError, KeyError) as error:
        return render_template(
            "ejercicio1.html",
            error=f"Datos inválidos: {error}"
        )


# EJERCICIO 2: FORMULARIO DE NOMBRES
@app.route("/ejercicio2")
def ejercicio2():
    return render_template("ejercicio2.html")

# PROCESAR NOMBRES
@app.route("/procesar_nombres", methods=["POST"])
def procesar_nombres():
    try:
        nombre1 = request.form["nombre1"].strip()
        nombre2 = request.form["nombre2"].strip()
        nombre3 = request.form["nombre3"].strip()

        nombres = [nombre1, nombre2, nombre3]

        # Validar campos vacíos
        if not all(nombres):
            raise ValueError("Debe ingresar los tres nombres.")

        # Validar que los nombres contengan solamente letras
        for nombre in nombres:
            if not nombre.replace(" ", "").isalpha():
                raise ValueError(
                    "Los nombres solo pueden contener letras y espacios."
                )


        # Validar nombres repetidos
        nombres_minusculas = [nombre.lower() for nombre in nombres]

        if len(set(nombres_minusculas)) != 3:
            raise ValueError("Los nombres no deben repetirse.")

        # Identificar el nombre más largo
        nombre_largo = max(nombres, key=len)
        cantidad = len(nombre_largo)

        return render_template(
            "ejercicio2.html",
            nombre1=nombre1,
            nombre2=nombre2,
            nombre3=nombre3,
            nombre=nombre_largo,
            cantidad=cantidad
        )


    except (ValueError, KeyError) as error:

        return render_template(
            "ejercicio2.html",
            nombre1=request.form.get("nombre1", "").strip(),
            nombre2=request.form.get("nombre2", "").strip(),
            nombre3=request.form.get("nombre3", "").strip(),
            error=f"Datos inválidos: {error}"
        )


# EJECUTAR APLICACION
if __name__ == "__main__":
    app.run(debug=True)
