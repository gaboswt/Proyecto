import tkinter as tk
from PIL import Image, ImageTk

# Definir el diccionario de enfermedades
enfermedades = {
    "VIH/SIDA": ["Fiebre", "Fatiga", "Pérdida de peso", "Ganglios inflamados", "Sudores nocturnos"],
    "Clamidia": ["Dolor al orinar", "Secreción anormal", "Dolor abdominal", "Sangrado entre periodos"],
    "Gonorrea": ["Dolor al orinar", "Secreción anormal", "Dolor en los testículos", "Sangrado entre periodos"],
    "Sífilis": ["Úlceras indoloras", "Erupción cutánea", "Fiebre", "Ganglios inflamados"],
    "Herpes Genital": ["Ampollas dolorosas", "Picazón", "Dolor al orinar", "Fiebre"],
    "VPH (Virus del Papiloma Humano)": ["Verrugas genitales", "Picazón", "Irritación"],
    "Tricomoniasis": ["Secreción vaginal", "Mal olor", "Picazón", "Dolor al orinar"],
    "Hepatitis B": ["Fatiga", "Náuseas", "Coloración amarilla en la piel", "Dolor abdominal"],
    "Linfogranuloma Venéreo": ["Úlceras genitales", "Ganglios inflamados", "Fiebre", "Dolor rectal"],
    "Molluscum Contagiosum": ["Bultos pequeños", "Picazón", "Irritación"],
    "Vaginosis Bacteriana": ["Secreción vaginal", "Mal olor", "Picazón", "Dolor al orinar"],
    "Candidiasis": ["Picazón intensa", "Secreción blanca", "Irritación", "Dolor durante el sexo"],
}


# Variable global para la ventana de resultados
ventana_resultados = None

def calcular_probabilidad(sintomas_seleccionados):
    probabilidades = {}

    # Contar cuántos síntomas de cada enfermedad están marcados
    for enfermedad, sintomas in enfermedades.items():
        coincidentes = sum(1 for sintoma in sintomas if sintoma in sintomas_seleccionados)
        probabilidad = (coincidentes / len(sintomas)) * 100
        probabilidades[enfermedad] = round(probabilidad)

    # Ordenar las enfermedades por probabilidad de manera decreciente
    probabilidades_ordenadas = dict(sorted(probabilidades.items(), key=lambda item: item[1], reverse=True))

    # Retornar solo las tres enfermedades con mayor probabilidad
    return dict(list(probabilidades_ordenadas.items())[:3])