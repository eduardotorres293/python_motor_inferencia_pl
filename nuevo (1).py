#representacion de hechos, lista de diccionarios
HECHOS = [
    {
        "id": "H1",
        "descripcion": "La actividad fisica incrementa el gasto energetico de una persona.",
        "categoria": "gasto_energetico"
    },
    {
        "id": "H2",
        "descripcion": "Una alimentacion saludable se basa en 4 principios: adecuacion, equilibrio, moderacion y diversidad.",
        "categoria": "principios_nutricion"
    },
    {
        "id": "H3",
        "descripcion": "El exceso de azucares puede aumentar el riesgo de problemas de salud.",
        "categoria": "riesgo_salud"
    },
    {
        "id": "H4",
        "descripcion": "El consumo adecuado de proteinas contribuye al mantenimiento y desarrollo de la masa muscular.",
        "categoria": "macronutrientes"
    },
    {
        "id": "H5",
        "descripcion": "El consumo de frutas y verduras forma parte de una alimentacion saludable.",
        "categoria": "alimentos_recomendados"
    },
    {
        "id": "H6",
        "descripcion": "Una alimentacion adecuada debe proporcionar la energia y nutrientes que necesita la persona.",
        "categoria": "requerimiento_diario"
    },
    {
        "id": "H7",
        "descripcion": "Las calorias que el cuerpo gasta en reposo se estiman con edad, peso, estatura y sexo.",
        "categoria": "metabolismo_basal",
        "valor": {"peso": 10, "estatura": 6.25, "edad": -5, "sexo": {"M": 5, "F": -161}},
        "fuente": "F7"
    },
    {
        "id": "H8",
        "descripcion": "El IMC clasifica a un adulto en peso bajo, normal, sobrepeso u obesidad.",
        "categoria": "diagnostico_imc",
        "valor": {"peso_bajo": 18.5, "normal": 25, "sobrepeso": 30},
        "unidad": "kg/m2",
        "fuente": "OMS"
    },
    {
        "id": "H9",
        "descripcion": "Una alimentacion saludable debe tener bajo contenido de grasas no saludables, azucares libres y sodio.",
        "categoria": "restricciones"
    },
    {
        "id": "H10",
        "descripcion": "Las necesidades de proteina pueden aumentar segun el nivel de actividad fisica y los objetivos relacionados con el desarrollo o mantenimiento muscular.",
        "categoria": "hipertrofia",
        "valor": {"bajar_peso_preservar": 2.2, "bajar_peso": 2.0, "ganar_musculo": 2.2, "mantenimiento": 1.6},
        "unidad": "g de proteina por kg de peso",
        "fuente": "F5"
    },
    {
        "id": "H11",
        "descripcion": "Un desequilibrio energetico sostenido es uno de los factores que puede contribuir al sobrepeso y la obesidad.",
        "categoria": "balance_energetico"
    },
    {
        "id": "H12",
        "descripcion": "Los adultos deben hacer actividad fisica moderada cada semana y ejercicios de fuerza.",
        "categoria": "actividad_fisica"
    },
    {
        "id": "H13",
        "descripcion": "Cualquier actividad fisica es mejor que el sedentarismo.",
        "categoria": "actividad_fisica"
    },
    {
        "id": "H14",
        "descripcion": "Se recomienda reducir ultraprocesados, carnes rojas y bebidas azucaradas.",
        "categoria": "restricciones"
    },
    {
        "id": "H15",
        "descripcion": "El gasto energetico total considera el gasto en reposo y la energia utilizada durante las actividades fisicas.",
        "categoria": "gasto_energetico"
    },
    {
        "id": "H16",
        "descripcion": "Para perder grasa se requiere un deficit calorico y para ganar masa muscular un superavit calorico. En mantenimiento el ajuste es cero.",
        "categoria": "balance_energetico",
        "valor": {"bajar_peso": -500, "ganar_musculo": 300, "mantenimiento": 0},
        "unidad": "kcal/dia",
        "fuente": "F6"
    },
    {
        "id": "H17",
        "descripcion": "Las grasas deben aportar entre el 20 % y el 35 % de la energia. sS propone el 25 %.",
        "categoria": "macronutrientes",
        "valor": 0.25,
        "rango": (0.20, 0.35),
        "fuente": "F8"
    },
    {
        "id": "H18",
        "descripcion": "Las calorias diarias no deberian bajar de un minimo segun el sexo.",
        "categoria": "seguridad",
        "valor": {"F": 1200, "M": 1500},
        "unidad": "kcal/dia",
        "fuente": "criterio del equipo"
    },
    {
        "id": "H19",
        "descripcion": "Los azucares libres deben aportar menos del 10 % de la energia total.",
        "categoria": "restricciones",
        "valor": 0.10,
        "fuente": "F1"
    },
    {
        "id": "H20",
        "descripcion": "Las proteinas y los carbohidratos aportan 4 kcal por gramo y las grasas 9 kcal por gramo.",
        "categoria": "macronutrientes",
        "valor": {"proteina": 4, "carbos": 4, "grasas": 9},
        "unidad": "kcal/g",
        "fuente": "factores de Atwater"
    },
    {
        "id": "H21",
        "descripcion": "Un factor de actividad de 1.55 o mayor (actividad moderada o mas) se considera nivel de actividad alto.",
        "categoria": "actividad_fisica",
        "valor": 1.55,
        "fuente": "criterio del equipo"
    }
]

HECHO = {h["id"]: h for h in HECHOS}
HECHOS_POR_ID = {h["id"]: h["descripcion"] for h in HECHOS}

def val(id_hecho):
    return HECHO[id_hecho]["valor"]

def clasificar_imc(imc):
    limites = val("H8")
    if imc < limites["peso_bajo"]:
        return "peso_bajo"
    if imc < limites["normal"]:
        return "normal"
    if imc < limites["sobrepeso"]:
        return "sobrepeso"
    return "obesidad"


NOMBRE_IMC = {
    "peso_bajo": "Peso bajo",
    "normal": "Peso normal",
    "sobrepeso": "Sobrepeso",
    "obesidad": "Obesidad",
}

REGLAS = {
    # R1: objetivo de perdida de peso (la proteina la deciden R7 y R16)
    "R1": {
        "si": lambda m: m["objetivo"] == "bajar_peso",
        "entonces": lambda m: {"factor_calorias": val("H16")["bajar_peso"]},
        "hechos_soporte": ["H1", "H6", "H11", "H16"]
    },
    # R2: objetivo de ganancia muscular
    "R2": {
        "si": lambda m: m["objetivo"] == "ganar_musculo",
        "entonces": lambda m: {
            "factor_calorias": val("H16")["ganar_musculo"],
            "proteina_g_kg": val("H10")["ganar_musculo"]
        },
        "hechos_soporte": ["H4", "H6", "H10", "H16"]
    },
    # R3: objetivo de mantenimiento
    "R3": {
        "si": lambda m: m["objetivo"] == "mantenimiento",
        "entonces": lambda m: {
            "factor_calorias": val("H16")["mantenimiento"],
            "proteina_g_kg": val("H10")["mantenimiento"]
        },
        "hechos_soporte": ["H2", "H6", "H15", "H10", "H16"]
    },
    # R4: nivel elevado de actividad fisica (su efecto numerico esta en R12 via factor_actividad)
    "R4": {
        "si": lambda m: m["factor_actividad"] >= val("H21"),
        "entonces": lambda m: {
            "aviso_R4": "Tu nivel de actividad fisica es alto, este valor ya es considerado en el gasto energetico total."
        },
        "hechos_soporte": ["H1", "H7", "H15", "H21"]
    },
    # R5: habitos alimenticios poco saludables
    "R5": {
        "si": lambda m: m.get("habitos_inadecuados", False),
        "entonces": lambda m: {
            "aviso_R5": "Procura mejorar la calidad de tu alimentacion, se recomiendan alimentos variados y de alto valor nutricional."
        },
        "hechos_soporte": ["H2", "H5", "H9", "H14"]
    },
    # R6: consumo elevado de azucar -> tope de azucares libres
    "R6": {
        "si": lambda m: m.get("alto_consumo_azucar", False) and "calorias_objetivo" in m,
        "entonces": lambda m: {
            "azucar_max_g": round(m["calorias_objetivo"] * val("H19") / val("H20")["carbos"]),
            "aviso_R6": f"Limita los azucares libres y las bebidas azucaradas a menos del {val('H19') * 100:.0f} % de tus calorias."
        },
        "hechos_soporte": ["H3", "H9", "H14", "H19", "H20"]
    },
    # R7: preservacion muscular durante la perdida de peso
    "R7": {
        "si": lambda m: m["objetivo"] == "bajar_peso" and m.get("preservar_musculo", True),
        "entonces": lambda m: {"proteina_g_kg": val("H10")["bajar_peso_preservar"]},
        "hechos_soporte": ["H4", "H6", "H10"]
    },
    # R8: recomendaciones generales para el mantenimiento
    "R8": {
        "si": lambda m: m["objetivo"] == "mantenimiento",
        "entonces": lambda m: {
            "aviso_R8": "Mantener actividad fisica regular, incluir ejercicios de fortalecimiento muscular "
                        "y procurar una alimentacion equilibrada."
        },
        "hechos_soporte": ["H2", "H12", "H13"]
    },
    # R9: distribucion de grasas
    "R9": {
        "si": lambda m: "calorias_objetivo" in m,
        "entonces": lambda m: {"grasas_g": m["calorias_objetivo"] * val("H17") / val("H20")["grasas"]},
        "hechos_soporte": ["H6", "H9", "H17", "H20"]
    },
    # R10: distribucion de carbohidratos (calorias restantes)
    "R10": {
        "si": lambda m: all(k in m for k in ("calorias_objetivo", "proteina_g", "grasas_g")),
        "entonces": lambda m: {
            "carbos_g": (m["calorias_objetivo"]
                         - val("H20")["proteina"] * m["proteina_g"]
                         - val("H20")["grasas"] * m["grasas_g"]) / val("H20")["carbos"]
        },
        "hechos_soporte": ["H6", "H20"]
    },
    # R11: tasa metabolica basal (Mifflin-St Jeor, coeficientes en H7)
    "R11": {
        "si": lambda m: all(k in m for k in ("peso", "estatura", "edad", "sexo")),
        "entonces": lambda m: {
            "tmb": val("H7")["peso"] * m["peso"] + val("H7")["estatura"] * m["estatura"]
                   + val("H7")["edad"] * m["edad"] + val("H7")["sexo"][m["sexo"]]
        },
        "hechos_soporte": ["H7"]
    },
    # R12: gasto energetico total
    "R12": {
        "si": lambda m: "tmb" in m and "factor_actividad" in m,
        "entonces": lambda m: {"get": m["tmb"] * m["factor_actividad"]},
        "hechos_soporte": ["H15"]
    },
    # R13: calorias objetivo
    "R13": {
        "si": lambda m: "get" in m and "factor_calorias" in m,
        "entonces": lambda m: {"calorias_objetivo": m["get"] + m["factor_calorias"]},
        "hechos_soporte": ["H6", "H11"]
    },
    # R14: gramos de proteina
    "R14": {
        "si": lambda m: "peso" in m and "proteina_g_kg" in m,
        "entonces": lambda m: {"proteina_g": m["proteina_g_kg"] * m["peso"]},
        "hechos_soporte": ["H4", "H10"]
    },
    # R15: porcentaje de carbohidratos
    "R15": {
        "si": lambda m: "carbos_g" in m and "calorias_objetivo" in m,
        "entonces": lambda m: {
            "pct_carbos": round(m["carbos_g"] * val("H20")["carbos"] / m["calorias_objetivo"] * 100, 1),
            "conclusion": "Dieta inicial generada"
        },
        "hechos_soporte": ["H6", "H2", "H20"]
    },
    # R16: perdida de peso sin interes en preservar musculo (excluyente con R7)
    "R16": {
        "si": lambda m: m["objetivo"] == "bajar_peso" and not m.get("preservar_musculo", True),
        "entonces": lambda m: {"proteina_g_kg": val("H10")["bajar_peso"]},
        "hechos_soporte": ["H4", "H6", "H10"]
    },
    # R17: advertencia si las calorias objetivo quedan por debajo del minimo segun el sexo
    "R17": {
        "si": lambda m: "calorias_objetivo" in m and m["calorias_objetivo"] < val("H18")[m["sexo"]],
        "entonces": lambda m: {
            "advertencia_R17": f"Tus calorias objetivo ({m['calorias_objetivo']:.0f} kcal) estan por debajo del minimo"
                               f"recomendado de {val('H18')[m['sexo']]} kcal/dia. Esta recomendacion no es adecuada"
                               f"para seguirse sin supervision: consulta a un nutriologo o medico."
        },
        "hechos_soporte": ["H6", "H18"]
    },
    # R18: calculo y diagnostico del IMC (estatura en cm, limites en H8)
    "R18": {
        "si": lambda m: "peso" in m and "estatura" in m,
        "entonces": lambda m: {
            "imc": round(m["peso"] / (m["estatura"] / 100) ** 2, 1),
            "diagnostico_imc": clasificar_imc(m["peso"] / (m["estatura"] / 100) ** 2)
        },
        "hechos_soporte": ["H8"]
    },
    # R19: advertencia si la persona ya tiene peso bajo y su objetivo es bajar de peso
    "R19": {
        "si": lambda m: m.get("diagnostico_imc") == "peso_bajo" and m["objetivo"] == "bajar_peso",
        "entonces": lambda m: {
            "advertencia_R19": f"Tu IMC ({m['imc']}) indica peso bajo y tu objetivo es bajar de peso."
                               f"Esta meta no es recomendable, consulta a un nutriologo o medico."
        },
        "hechos_soporte": ["H6", "H8"]
    },
    # R20: aviso informativo para sobrepeso u obesidad
    "R20": {
        "si": lambda m: m.get("diagnostico_imc") in ("sobrepeso", "obesidad") and m["objetivo"] == "ganar_musculo",
        "entonces": lambda m: {
            "aviso_R20": f"Tu IMC ({m['imc']}) indica {NOMBRE_IMC[m['diagnostico_imc']].lower()}, cuida que el superavit calorico se mantenga moderado."
        },
        "hechos_soporte": ["H8", "H11"]
    },
}

# motor de inferencia, recibe los datos del caso y verifica con los hechos para obtener un resultado
def motor_inferencia(caso):
    datos = dict(caso)
    reglas = set()
    traza = []
    ciclo = 0
    nuevo = True

    while nuevo:
        nuevo = False
        ciclo += 1
        for id_r, regla in REGLAS.items():
            if id_r in reglas:
                continue
            if not all(h in HECHO for h in regla["hechos_soporte"]):
                continue
            if regla["si"](datos):
                derivados = regla["entonces"](datos)
                for k, v in derivados.items():
                    if k in datos and datos[k] != v:
                        raise ValueError(f"Error de valor, {id_r} intenta cambiar '{k}' de {datos[k]} a {v}")
                datos.update(derivados)
                reglas.add(id_r)
                traza.append((ciclo, id_r, derivados, regla["hechos_soporte"]))
                nuevo = True

    return datos, traza

# intervalos para los datos numericos
INTERVALOS = {
    "edad":     (18, 65, "años"),
    "peso":     (30, 250, "kg"),
    "estatura": (120, 230, "cm"),
}

OPCIONES_SEXO = {
    "1": ("M", "Masculino"),
    "2": ("F", "Femenino"),
}

OPCIONES_OBJETIVO = {
    "1": ("bajar_peso", "Bajar de peso"),
    "2": ("ganar_musculo", "Ganar masa muscular"),
    "3": ("mantenimiento", "Mantener el peso"),
}

OPCIONES_ACTIVIDAD = {
    "1": (1.2,   "Sedentario (poco o nada de ejercicio)"),
    "2": (1.375, "Ligera (1-3 dias por semana)"),
    "3": (1.55,  "Moderada (3-5 dias por semana)"),
    "4": (1.725, "Intensa (6-7 dias por semana)"),
    "5": (1.9,   "Muy intensa (entrenamiento doble o trabajo fisico pesado)"),
}

def pedir_numero(nombre):
    minimo, maximo, unidad = INTERVALOS[nombre]
    while True:
        texto = input(f"{nombre.capitalize()} ({minimo}-{maximo} {unidad}): ").strip()
        try:
            valor = float(texto)
        except ValueError:
            print("  Escribe un numero valido.")
            continue
        if minimo <= valor <= maximo:
            return int(valor) if valor.is_integer() else valor
        print(f"  El valor debe estar entre {minimo} y {maximo} {unidad}.")

def pedir_opcion(titulo, opciones):
    print(f"\n{titulo}")
    for clave, (_, texto) in opciones.items():
        print(f"  {clave}) {texto}")
    while True:
        eleccion = input("Elige una opcion: ").strip()
        if eleccion in opciones:
            return opciones[eleccion][0]
        print(f"  Opcion invalida. Elige entre {', '.join(opciones)}.")

def pedir_si_no(pregunta):
    while True:
        r = input(f"{pregunta} (s/n): ").strip().lower()
        if r in ("s", "si", "si"):
            return True
        if r in ("n", "no"):
            return False
        print("  Responde con 's' o 'n'.")

# se obtienen los datos introducidos por el usuario para su uso
def capturar_caso():
    print("=== Datos del caso ===")
    caso = {
        "edad": pedir_numero("edad"),
        "peso": pedir_numero("peso"),
        "estatura": pedir_numero("estatura"),
    }
    caso["sexo"] = pedir_opcion("Sexo:", OPCIONES_SEXO)
    caso["factor_actividad"] = pedir_opcion("Nivel de actividad fisica:", OPCIONES_ACTIVIDAD)
    caso["objetivo"] = pedir_opcion("Objetivo:", OPCIONES_OBJETIVO)

    print()
    caso["habitos_inadecuados"] = pedir_si_no("¿Tienes habitos alimenticios poco saludables?")
    caso["alto_consumo_azucar"] = pedir_si_no("¿Consumes azucar en exceso?")
    if caso["objetivo"] == "bajar_peso":
        caso["preservar_musculo"] = pedir_si_no("¿Quieres preservar tu masa muscular?")
    return caso

# para dar un formato a los datos
def _fmt(v):
    return round(v, 1) if isinstance(v, float) else v

# funcion para mostrar los resultados y multiples datos finales
def mostrar_resultado(datos, traza):
    kcal = datos["calorias_objetivo"]
    e = val("H20")
    prot, gras, carb = datos["proteina_g"], datos["grasas_g"], datos["carbos_g"]

    print("\n=== Recomendacion inicial ===")
    print(f"IMC: {datos['imc']} ({NOMBRE_IMC[datos['diagnostico_imc']]})")
    print(f"Metabolismo basal: {datos['tmb']:.0f} kcal")
    print(f"Gasto energetico total: {datos['get']:.0f} kcal")
    print(f"Calorias objetivo: {kcal:.0f} kcal/dia")
    print(f"  Proteinas:     {prot:.0f} g ({prot * e['proteina'] / kcal * 100:.0f} %)")
    print(f"  Grasas:        {gras:.0f} g ({gras * e['grasas'] / kcal * 100:.0f} %)")
    print(f"  Carbohidratos: {carb:.0f} g ({datos['pct_carbos']:.0f} %)")
    if "azucar_max_g" in datos:
        print(f"  Azucares libres: maximo {datos['azucar_max_g']} g")

    advertencias = [v for k, v in datos.items() if k.startswith("advertencia_")]
    if advertencias:
        print("\n!!! ADVERTENCIA !!!")
        for a in advertencias:
            print(f"  {a}")

    avisos = [v for k, v in datos.items() if k.startswith("aviso_")]
    if avisos:
        print("\nRecomendaciones:")
        for a in avisos:
            print(f"  - {a}")

    print("\n\n\n=== Explicacion y reglas aplicadas ===")
    for ciclo, id_r, derivados, soporte in traza:
        resumen = ", ".join(f"{k}={_fmt(v)}" for k, v in derivados.items() if not k.startswith(("aviso_", "advertencia_")))
        print(f"[Ciclo {ciclo}] {id_r}" + (f": {resumen}" if resumen else " (aviso)"))
        for h in soporte:
            print(f"    {h}: {HECHOS_POR_ID[h]}")


if __name__ == "__main__":
    caso = capturar_caso()
    datos, traza = motor_inferencia(caso)
    mostrar_resultado(datos, traza)
