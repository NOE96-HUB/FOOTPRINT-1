import streamlit as st

# Base de datos con factores de emisión reales (aproximados)
FACTORES_EMISION = {
    'aparatos': {
        'Refrigerador': 400,  # basado en estimaciones comunes
        'Horno de microondas': 60,  # basado en estimaciones comunes
        'Computadora': 300,  # basado en estimaciones comunes
        'Laptop': 100,  # basado en estimaciones comunes
        'Consola de videojuegos': 50,  # basado en estimaciones comunes
        'Estéreo': 30,  # basado en estimaciones comunes
        'Televisión': 200,  # basado en estimaciones comunes
        'Lavadora': 300,  # basado en estimaciones comunes
        'Secadora de ropa': 700,  # basado en estimaciones comunes
        'Lavatrastes': 200,  # basado en estimaciones comunes
        'Aspiradora': 50,  # basado en estimaciones comunes
        'Aire acondicionado': 1000,  # basado en estimaciones comunes
        'Ventiladores': 70  # basado en estimaciones comunes
    },
    'gas': {
        'Gas natural': 2250,  # en kg CO2/año, basado en datos de la EPA
        'Gas LP': 2500  # en kg CO2/año, basado en datos de la EPA
    },
    'focos': {
        'LED': 10,  # en kg CO2/año, basado en datos del Carbon Trust
        'Ahorradores': 20,  # en kg CO2/año, basado en datos del Carbon Trust
        'Incandescentes': 50,  # en kg CO2/año, basado en datos del Carbon Trust
        'Desconozco': 30  # en kg CO2/año, estimación promedio
    },
    'transporte': {
        'Auto': 4500,  # en kg CO2/año, basado en estimaciones comunes
        'Autobus': 1050,  # en kg CO2/año, basado en estimaciones comunes
        'Bicicleta': 0,  # en kg CO2/año, sin emisiones directas
        'Combi': 1800,  # en kg CO2/año, basado en estimaciones comunes
        'Metro': 700,  # en kg CO2/año, basado en estimaciones comunes
        'Metrobus': 800,  # en kg CO2/año, basado en estimaciones comunes
        'Motocicleta': 2000,  # en kg CO2/año, basado en estimaciones comunes
        'Voy caminando': 0  # en kg CO2/año, sin emisiones directas
    },
    'tiempo_transporte': {
        'Menos de 10 minutos': 100,  # en kg CO2/año, estimación promedio
        'Entre 10 y 20 minutos': 200,  # en kg CO2/año, estimación promedio
        'Entre 20 y 40 minutos': 400,  # en kg CO2/año, estimación promedio
        'Entre 40 minutos y 1 hora': 600,  # en kg CO2/año, estimación promedio
        'Una hora y media': 900,  # en kg CO2/año, estimación promedio
        'Más de dos horas': 1200,  # en kg CO2/año, estimación promedio
        'Más de tres horas': 1500  # en kg CO2/año, estimación promedio
    },
    'vuelos': {
        'Viajero frecuente, más de dos vuelos internacionales y dos nacionales al año.': 11000,  # en kg CO2/año, basado en datos de la EPA
        'Aproximadamente un vuelo (ida y vuelta) internacional al año.': 5000,  # en kg CO2/año, basado en datos de la EPA
        'Más de un vuelo (ida y vuelta) nacional al año.': 3000,  # en kg CO2/año, basado en datos de la EPA
        'Aproximadamente un vuelo (ida y vuelta) nacional al año.': 1500,  # en kg CO2/año, basado en datos de la EPA
        'No suelo volar.': 0  # en kg CO2/año, sin emisiones directas
    },
    'carne': {
        'Diario': 2000,  # en kg CO2/año, basado en estimaciones comunes
        '4-6 días a la semana': 1500,  # en kg CO2/año, basado en estimaciones comunes
        '1-3 días a la semana': 800,  # en kg CO2/año, basado en estimaciones comunes
        'No consumo': 0  # en kg CO2/año, sin emisiones directas
    },
    'plasticos': {
        'Diario': 1000,  # en kg CO2/año, basado en estimaciones comunes
        'De vez en cuando - 1 vez por semana.': 400,  # en kg CO2/año, basado en estimaciones comunes
        'Rara vez.': 200,  # en kg CO2/año, basado en estimaciones comunes
        'No uso plástico.': 0  # en kg CO2/año, sin emisiones directas
    },
    'ropa': {
        'Siempre es nueva y de importación.': 1800,  # en kg CO2/año, basado en datos del Carbon Trust
        'Siempre es nueva y nacional.': 1200,  # en kg CO2/año, basado en datos del Carbon Trust
        'De segunda mano.': 300,  # en kg CO2/año, basado en datos del Carbon Trust
        'La reparo y reutilizo.': 150  # en kg CO2/año, basado en datos del Carbon Trust
    },
    'dispositivos': {
        'Cada 6 meses': 1000,  # en kg CO2/año, basado en estimaciones comunes
        'Cada año': 800,  # en kg CO2/año, basado en estimaciones comunes
        'De 2 a 3 años': 500,  # en kg CO2/año, basado en estimaciones comunes
        'Más de 3 años': 300,  # en kg CO2/año, basado en estimaciones comunes
        'No tengo este dispositivo': 0  # en kg CO2/año, sin emisiones directas
    }
}

# Function to display the introduction page
def mostrar_introduccion():
    st.markdown("<h1 style='color: #155724; text-align: center;'>Calculadora de Huella de Carbono 🌍</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #155724;'>¿Qué es una huella de carbono? 🌱</h2>", unsafe_allow_html=True)
    st.write("""
    La huella de carbono es la totalidad de gases de efecto invernadero emitidos por efecto directo o indirecto de un individuo, organización, evento o producto. 
    Se mide en unidades de dióxido de carbono equivalente (CO2e) y se calcula considerando diversas actividades como el transporte, el consumo de energía, 
    la alimentación, entre otros.
    """)
    st.write("""
    La importancia de medir nuestra huella de carbono radica en la necesidad de comprender el impacto que nuestras actividades tienen sobre el medio ambiente 
    y tomar acciones para reducirlo.
    """)
    if st.button('COMENZAR'):
        st.session_state.pagina = 1

# Function to display the calculator step by step
def mostrar_calculadora():
    pagina = st.session_state.pagina

    if pagina == 1:
        st.markdown("<h2 style='color: #155724;'>¿QUÉ APARATOS ELECTRÓNICOS TIENES EN CASA? 💻</h2>", unsafe_allow_html=True)
        st.write("Selecciona todos los que tengas:")
        aparatos = FACTORES_EMISION['aparatos']
        for aparato in aparatos.keys():
            st.checkbox(aparato, key=f'aparato_{aparato}')
        if st.button('Siguiente'):
            st.session_state.pagina = 2

    elif pagina == 2:
        st.markdown("<h2 style='color: #155724;'>EN MI DOMICILIO UTILIZO EL SIGUIENTE TIPO DE GAS 🔥</h2>", unsafe_allow_html=True)
        gas = FACTORES_EMISION['gas']
        st.radio('Selecciona el tipo de gas que utilizas:', list(gas.keys()), key='tipo_gas')
        if st.button('Anterior'):
            st.session_state.pagina = 1
        if st.button('Siguiente'):
            st.session_state.pagina = 3

    elif pagina == 3:
        st.markdown("<h2 style='color: #155724;'>EN MI CASA LOS FOCOS SON 💡</h2>", unsafe_allow_html=True)
        focos = FACTORES_EMISION['focos']
        st.radio('Selecciona el tipo de focos que utilizas:', list(focos.keys()), key='tipo_focos')
        if st.button('Anterior'):
            st.session_state.pagina = 2
        if st.button('Siguiente'):
            st.session_state.pagina = 4

    elif pagina == 4:
        st.markdown("<h2 style='color: #155724;'>¿QUÉ MEDIO DE TRANSPORTE UTILIZAS PARA LLEGAR AL TRABAJO O A LA ESCUELA? 🚗</h2>", unsafe_allow_html=True)
        transporte = FACTORES_EMISION['transporte']
        st.radio('Selecciona tu medio de transporte:', list(transporte.keys()), key='medio_transporte')
        if st.button('Anterior'):
            st.session_state.pagina = 3
        if st.button('Siguiente'):
            st.session_state.pagina = 5

    elif pagina == 5:
        st.markdown("<h2 style='color: #155724;'>¿EN CUÁNTO TIEMPO HACES ESE RECORRIDO? ⏰</h2>", unsafe_allow_html=True)
        tiempo_transporte = FACTORES_EMISION['tiempo_transporte']
        st.radio('Selecciona el tiempo que tardas:', list(tiempo_transporte.keys()), key='tiempo_transporte')
        if st.button('Anterior'):
            st.session_state.pagina = 4
        if st.button('Siguiente'):
            st.session_state.pagina = 6

    elif pagina == 6:
        st.markdown("<h2 style='color: #155724;'>¿CON QUÉ FRECUENCIA VUELAS EN AVIÓN? ✈️</h2>", unsafe_allow_html=True)
        vuelos = FACTORES_EMISION['vuelos']
        st.radio('Selecciona la frecuencia con la que vuelas:', list(vuelos.keys()), key='frecuencia_vuelos')
        if st.button('Anterior'):
            st.session_state.pagina = 5
        if st.button('Siguiente'):
            st.session_state.pagina = 7

    elif pagina == 7:
        st.markdown("<h2 style='color: #155724;'>¿CON QUÉ FRECUENCIA COMES CARNE DE? 🍖</h2>", unsafe_allow_html=True)
        carne = FACTORES_EMISION['carne']
        st.write("<div style='color: #155724;'>- Res</div>", unsafe_allow_html=True)
        st.radio("", list(carne.keys()), key='carne_res')
        st.write("<div style='color: #155724;'>- Cerdo</div>", unsafe_allow_html=True)
        st.radio("", list(carne.keys()), key='carne_cerdo')
        st.write("<div style='color: #155724;'>- Pollo</div>", unsafe_allow_html=True)
        st.radio("", list(carne.keys()), key='carne_pollo')
        st.write("<div style='color: #155724;'>- Pescado</div>", unsafe_allow_html=True)
        st.radio("", list(carne.keys()), key='carne_pescado')
        if st.button('Anterior'):
            st.session_state.pagina = 6
        if st.button('Siguiente'):
            st.session_state.pagina = 8

    elif pagina == 8:
        st.markdown("<h2 style='color: #155724;'>¿CON QUÉ REGULARIDAD UTILIZAS PLÁSTICOS DE UN SOLO USO? 🛍️</h2>", unsafe_allow_html=True)
        plasticos = FACTORES_EMISION['plasticos']
        st.radio('Selecciona la regularidad:', list(plasticos.keys()), key='uso_plasticos')
        if st.button('Anterior'):
            st.session_state.pagina = 7
        if st.button('Siguiente'):
            st.session_state.pagina = 9

    elif pagina == 9:
        st.markdown("<h2 style='color: #155724;'>LA ROPA QUE UTILIZO... 👚</h2>", unsafe_allow_html=True)
        ropa = FACTORES_EMISION['ropa']
        st.radio('Selecciona la opción que más te aplica:', list(ropa.keys()), key='uso_ropa')
        if st.button('Anterior'):
            st.session_state.pagina = 8
        if st.button('Siguiente'):
            st.session_state.pagina = 10

    elif pagina == 10:
        st.markdown("<h2 style='color: #155724;'>CADA CUÁNTO CAMBIO MIS DISPOSITIVOS ELECTRÓNICOS 🖥️</h2>", unsafe_allow_html=True)
        dispositivos = FACTORES_EMISION['dispositivos']
        st.write("<div style='color: #155724;'>- Celular</div>", unsafe_allow_html=True)
        st.radio("", list(dispositivos.keys()), key='cambio_celular')
        st.write("<div style='color: #155724;'>- Tableta</div>", unsafe_allow_html=True)
        st.radio("", list(dispositivos.keys()), key='cambio_tableta')
        st.write("<div style='color: #155724;'>- Computadora</div>", unsafe_allow_html=True)
        st.radio("", list(dispositivos.keys()), key='cambio_computadora')
        st.write("<div style='color: #155724;'>- Consola de videojuegos</div>", unsafe_allow_html=True)
        st.radio("", list(dispositivos.keys()), key='cambio_consola')
        if st.button('Anterior'):
            st.session_state.pagina = 9
        if st.button('Calcular Huella de Carbono'):
            st.session_state.pagina = 11

    elif pagina == 11:
        # Realizar los cálculos
        total = 0
        aparatos = FACTORES_EMISION['aparatos']
        for aparato in aparatos.keys():
            if st.session_state.get(f'aparato_{aparato}', False):
                total += aparatos[aparato]
        
        total += FACTORES_EMISION['gas'].get(st.session_state.get('tipo_gas', ''), 0)
        total += FACTORES_EMISION['focos'].get(st.session_state.get('tipo_focos', ''), 0)
        total += FACTORES_EMISION['transporte'].get(st.session_state.get('medio_transporte', ''), 0)
        total += FACTORES_EMISION['tiempo_transporte'].get(st.session_state.get('tiempo_transporte', ''), 0)
        total += FACTORES_EMISION['vuelos'].get(st.session_state.get('frecuencia_vuelos', ''), 0)
        total += FACTORES_EMISION['carne'].get(st.session_state.get('carne_res', ''), 0)
        total += FACTORES_EMISION['carne'].get(st.session_state.get('carne_cerdo', ''), 0)
        total += FACTORES_EMISION['carne'].get(st.session_state.get('carne_pollo', ''), 0)
        total += FACTORES_EMISION['carne'].get(st.session_state.get('carne_pescado', ''), 0)
        total += FACTORES_EMISION['plasticos'].get(st.session_state.get('uso_plasticos', ''), 0)
        total += FACTORES_EMISION['ropa'].get(st.session_state.get('uso_ropa', ''), 0)
        total += FACTORES_EMISION['dispositivos'].get(st.session_state.get('cambio_celular', ''), 0)
        total += FACTORES_EMISION['dispositivos'].get(st.session_state.get('cambio_tableta', ''), 0)
        total += FACTORES_EMISION['dispositivos'].get(st.session_state.get('cambio_computadora', ''), 0)
        total += FACTORES_EMISION['dispositivos'].get(st.session_state.get('cambio_consola', ''), 0)
        total += FACTORES_EMISION['dispositivos'].get(st.session_state.get('cambio_consola', ''), 0)

        # Convertir a toneladas
        total_toneladas = total / 1000

        st.markdown("<h2 style='color: #155724; text-align: center;'>Resultado</h2>", unsafe_allow_html=True)
        st.subheader('Tu Huella de Carbono Total es:')
        st.write(f'{total_toneladas:.2f} toneladas de CO2 por año')

        # Mostrar mensajes según el resultado
        if total_toneladas > 6:
            st.write("😢 🌳 Lamentablemente estás por encima del promedio nacional (México), sin embargo no te desanimes, aquí hay algunos consejos que te pueden ayudar con tu producción anual y el cuidado del medio ambiente:")
            st.write("""
            - Consumir menos carne roja.
            - Usar transporte público o bicicleta.
            - Mejorar eficiencia energética en casa.
            - Reducir plásticos desechables.
            - Elegir energía renovable.
            - Reducir desperdicio de alimentos.
            - Promover prácticas sostenibles en el trabajo.
            """)
        else:
            st.balloons()
            st.write("🎉 🌿 ¡FELICIDADES! ESTÁS POR DEBAJO DEL PROMEDIO NACIONAL, MENOR A 6 TONELADAS DE CO2 POR AÑO... PERO NO BAJEMOS LA GUARDIA. AQUÍ HAY ALGUNAS COSAS QUE PUEDES MEJORAR:")
            st.write("""
            1. Ahorrar agua cerrando llaves mientras no se use.
            2. Reciclar correctamente desechos y separar la basura.
            3. Practicar la economía circular.
            4. Apoyar iniciativas locales de conservación y restauración ambiental.
            5. Reducir el consumo de productos empaquetados.
            """)
        
        if st.button('Volver al inicio'):
            st.session_state.pagina = 0

# Main function
if 'pagina' not in st.session_state:
    st.session_state.pagina = 0

if st.session_state.pagina == 0:
    mostrar_introduccion()
else:
    mostrar_calculadora()

# Custom CSS to change the background color, text color, and button style
st.markdown(
    """
    <style>
    .stApp {
        background-color: #d4edda;
        color: #155724;
    }
    h1, h2, div, p {
        color: #155724 !important;
    }
    .stButton>button {
        background-color: #84CF96 !important;  /* Fondo verde claro */
        color: #ffffff !important;  /* Texto blanco */
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stRadio > label > div > div > div > div, .stCheckbox > label > div {
        color: #155724 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)




