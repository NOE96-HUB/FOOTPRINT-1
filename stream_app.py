import streamlit as st

# Base de datos ficticia para factores de emisión
FACTORES_EMISION = {
    'aparatos': {
        'Refrigerador': 0.1,
        'Horno de microondas': 0.05,
        'Computadora': 0.03,
        'Laptop': 0.02,
        'Consola de videojuegos': 0.04,
        'Estéreo': 0.01,
        'Televisión': 0.06,
        'Lavadora': 0.07,
        'Secadora de ropa': 0.08,
        'Lavatrastes': 0.09,
        'Aspiradora': 0.02,
        'Aire acondicionado': 0.15,
        'Ventiladores': 0.03
    },
    'gas': {
        'Gas natural': 1.0,
        'Gas LP': 1.2
    },
    'focos': {
        'LED': 0.1,
        'Ahorradores': 0.2,
        'Incandescentes': 0.5,
        'Desconozco': 0.3
    },
    'transporte': {
        'Auto': 1.0,
        'Autobus': 0.5,
        'Bicicleta': 0.01,
        'Combi': 0.6,
        'Metro': 0.2,
        'Metrobus': 0.3,
        'Motocicleta': 0.8,
        'Voy caminando': 0.0
    },
    'tiempo_transporte': {
        'Menos de 10 minutos': 0.1,
        'Entre 10 y 20 minutos': 0.2,
        'Entre 20 y 40 minutos': 0.3,
        'Entre 40 minutos y 1 hora': 0.4,
        'Una hora y media': 0.5,
        'Más de dos horas': 0.6,
        'Más de tres horas': 0.7
    },
    'vuelos': {
        'Viajero frecuente, más de dos vuelos internacionales y dos nacionales al año.': 3.0,
        'Aproximadamente un vuelo (ida y vuelta) internacional al año.': 2.0,
        'Más de un vuelo (ida y vuelta) nacional al año.': 1.5,
        'Aproximadamente un vuelo (ida y vuelta) nacional al año.': 1.0,
        'No suelo volar.': 0.0
    },
    'carne': {
        'Diario': 1.0,
        '4-6 días a la semana': 0.8,
        '1-3 días a la semana': 0.5,
        'No consumo': 0.0
    },
    'plasticos': {
        'Diario': 1.0,
        'De vez en cuando - 1 vez por semana.': 0.5,
        'Rara vez.': 0.2,
        'No uso plástico.': 0.0
    },
    'ropa': {
        'Siempre es nueva y de importación.': 2.0,
        'Siempre es nueva y nacional.': 1.5,
        'De segunda mano.': 0.5,
        'La reparo y reutilizo.': 0.2
    },
    'dispositivos': {
        'Cada 6 meses': 1.0,
        'Cada año': 0.8,
        'De 2 a 3 años': 0.5,
        'Más de 3 años': 0.2,
        'No tengo este dispositivo': 0.0
    }
}

# Function to display the introduction page
def mostrar_introduccion():
    st.markdown("<h1 style='color: #155724;'>Calculadora de Huella de Carbono</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #155724;'>¿Qué es una huella de carbono?</h2>", unsafe_allow_html=True)
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
        st.markdown("<h2 style='color: #155724;'>¿QUÉ APARATOS ELECTRÓNICOS TIENES EN CASA?</h2>", unsafe_allow_html=True)
        st.write("Selecciona todos los que tengas:")
        aparatos = FACTORES_EMISION['aparatos']
        for aparato in aparatos.keys():
            st.checkbox(aparato, key=f'aparato_{aparato}')
        if st.button('Siguiente'):
            st.session_state.pagina = 2

    elif pagina == 2:
        st.markdown("<h2 style='color: #155724;'>EN MI DOMICILIO UTILIZO EL SIGUIENTE TIPO DE GAS</h2>", unsafe_allow_html=True)
        gas = FACTORES_EMISION['gas']
        st.radio('Selecciona el tipo de gas que utilizas:', list(gas.keys()), key='tipo_gas')
        if st.button('Anterior'):
            st.session_state.pagina = 1
        if st.button('Siguiente'):
            st.session_state.pagina = 3

    elif pagina == 3:
        st.markdown("<h2 style='color: #155724;'>EN MI CASA LOS FOCOS SON</h2>", unsafe_allow_html=True)
        focos = FACTORES_EMISION['focos']
        st.radio('Selecciona el tipo de focos que utilizas:', list(focos.keys()), key='tipo_focos')
        if st.button('Anterior'):
            st.session_state.pagina = 2
        if st.button('Siguiente'):
            st.session_state.pagina = 4

    elif pagina == 4:
        st.markdown("<h2 style='color: #155724;'>¿QUE MEDIO DE TRANSPORTE UTILIZAS PARA LLEGAR AL TRABAJO O A LA ESCUELA?</h2>", unsafe_allow_html=True)
        transporte = FACTORES_EMISION['transporte']
        st.radio('Selecciona tu medio de transporte:', list(transporte.keys()), key='medio_transporte')
        if st.button('Anterior'):
            st.session_state.pagina = 3
        if st.button('Siguiente'):
            st.session_state.pagina = 5

    elif pagina == 5:
        st.markdown("<h2 style='color: #155724;'>¿EN CUÁNTO TIEMPO HACES ESE RECORRIDO?</h2>", unsafe_allow_html=True)
        tiempo_transporte = FACTORES_EMISION['tiempo_transporte']
        st.radio('Selecciona el tiempo que tardas:', list(tiempo_transporte.keys()), key='tiempo_transporte')
        if st.button('Anterior'):
            st.session_state.pagina = 4
        if st.button('Siguiente'):
            st.session_state.pagina = 6

    elif pagina == 6:
        st.markdown("<h2 style='color: #155724;'>¿CON QUÉ FRECUENCIA VUELAS EN AVIÓN?</h2>", unsafe_allow_html=True)
        vuelos = FACTORES_EMISION['vuelos']
        st.radio('Selecciona la frecuencia con la que vuelas:', list(vuelos.keys()), key='frecuencia_vuelos')
        if st.button('Anterior'):
            st.session_state.pagina = 5
        if st.button('Siguiente'):
            st.session_state.pagina = 7

    elif pagina == 7:
        st.markdown("<h2 style='color: #155724;'>¿CON QUÉ FRECUENCIA COMES CARNE DE?</h2>", unsafe_allow_html=True)
        carne = FACTORES_EMISION['carne']
        st.write("- Res")
        st.radio("", list(carne.keys()), key='carne_res')
        st.write("- Cerdo")
        st.radio("", list(carne.keys()), key='carne_cerdo')
        st.write("- Pollo")
        st.radio("", list(carne.keys()), key='carne_pollo')
        st.write("- Pescado")
        st.radio("", list(carne.keys()), key='carne_pescado')
        if st.button('Anterior'):
            st.session_state.pagina = 6
        if st.button('Siguiente'):
            st.session_state.pagina = 8

    elif pagina == 8:
        st.markdown("<h2 style='color: #155724;'>¿CON QUÉ REGULARIDAD UTILIZAS PLÁSTICOS DE UN SOLO USO?</h2>", unsafe_allow_html=True)
        plasticos = FACTORES_EMISION['plasticos']
        st.radio('Selecciona la regularidad:', list(plasticos.keys()), key='uso_plasticos')
        if st.button('Anterior'):
            st.session_state.pagina = 7
        if st.button('Siguiente'):
            st.session_state.pagina = 9

    elif pagina == 9:
        st.markdown("<h2 style='color: #155724;'>LA ROPA QUE UTILIZO...</h2>", unsafe_allow_html=True)
        ropa = FACTORES_EMISION['ropa']
        st.radio('Selecciona la opción que más te aplica:', list(ropa.keys()), key='uso_ropa')
        if st.button('Anterior'):
            st.session_state.pagina = 8
        if st.button('Siguiente'):
            st.session_state.pagina = 10

    elif pagina == 10:
        st.markdown("<h2 style='color: #155724;'>CADA CUÁNTO CAMBIO MIS DISPOSITIVOS ELECTRÓNICOS</h2>", unsafe_allow_html=True)
        dispositivos = FACTORES_EMISION['dispositivos']
        st.write("- Celular")
        st.radio("", list(dispositivos.keys()), key='cambio_celular')
        st.write("- Tableta")
        st.radio("", list(dispositivos.keys()), key='cambio_tableta')
        st.write("- Computadora")
        st.radio("", list(dispositivos.keys()), key='cambio_computadora')
        st.write("- Consola de videojuegos")
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

        st.markdown("<h2 style='color: #155724;'>Resultado</h2>", unsafe_allow_html=True)
        st.subheader('Tu Huella de Carbono Total es:')
        st.write(f'{total:.2f} kg CO2 por mes')
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
    h1, h2 {
        color: #155724;
    }
    div.stButton > button {
        background-color: #155724;
        color: white;
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
    </style>
    """,
    unsafe_allow_html=True
)

