import tkinter as tk

# Diccionario de enfermedades sexuales y sus síntomas
enfermedades = {
    "Clamidia": ["Dolor al orinar", "Secreción genital", "Dolor abdominal", "Sangrado fuera del ciclo menstrual"],
    "Gonorrea": ["Dolor al orinar", "Secreción genital anormal", "Dolor o hinchazón testicular", "Dolor pélvico"],
    "Sífilis": ["Úlceras indoloras", "Erupción cutánea", "Fiebre", "Ganglios linfáticos inflamados"],
    "Herpes Genital": ["Ampollas dolorosas", "Úlceras genitales", "Picazón", "Dolor al orinar"],
    "VPH (Virus del Papiloma Humano)": ["Verrugas genitales", "Picazón", "Molestias en el área genital"],
    "VIH/SIDA": ["Fiebre persistente", "Fatiga extrema", "Pérdida de peso", "Sudoración nocturna"],
    "Tricomoniasis": ["Secreción vaginal amarilla", "Picazón vaginal", "Dolor al orinar", "Irritación genital"],
    "Hepatitis B": ["Ictericia", "Dolor abdominal", "Fatiga", "Náuseas"],
    "Molluscum Contagiosum": ["Lesiones o protuberancias en la piel", "Picazón", "Irritación local"],
    "Linfogranuloma Venéreo": ["Úlcera genital", "Inflamación de ganglios linfáticos inguinales", "Fiebre", "Dolor rectal"],
    "Candidiasis Genital": ["Picazón intensa", "Secreción blanca y grumosa", "Enrojecimiento", "Dolor al orinar"],
    "Donovanosis": ["Úlceras genitales progresivas", "Sangrado genital", "Dolor en el área genital"],
}

def calcular_probabilidad(sintomas_seleccionados):
    probabilidades = {}
    for enfermedad, sintomas in enfermedades.items():
        coincidentes = sum(1 for sintoma in sintomas if sintoma in sintomas_seleccionados)
        probabilidad = (coincidentes / len(sintomas)) * 100
        probabilidades[enfermedad] = round(probabilidad)
    probabilidades_ordenadas = dict(sorted(probabilidades.items(), key=lambda item: item[1], reverse=True))
    return dict(list(probabilidades_ordenadas.items())[:3])