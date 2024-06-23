import streamlit as st

def calcular_huella_de_carbono(transporte, energia, consumo):
    # Factores de emisión aproximados (en kg CO2 por unidad)
    factores_emision = {
        'coche': 0.24,  # por km
        'moto': 0.12,   # por km
        'transporte_publico': 0.05,  # por km
        'electricidad': 0.233,  # por kWh
        'gas': 2.02  # por m3
    }
    
    huella_transporte = transporte['coche'] * factores_emision['coche'] + \
                        transporte['moto'] * factores_emision['moto'] + \
                        transporte['transporte_publico'] * factores_emision['transporte_publico']
    
    huella_energia = energia['electricidad'] * factores_emision['electricidad'] + \
                     energia['gas'] * factores_emision['gas']
    
    huella_total = huella_transporte + huella_energia + consumo
    return huella_total

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
        st.session_state.comenzar = True

# Function to display the calculator
def mostrar_calculadora():
    st.markdown("<h1 style='color: #155724;'>Calculadora de Huella de Carbono</h1>", unsafe_allow_html=True)

    # Sección de transporte
    st.markdown("<h2 style='color: #155724;'>Transporte</h2>", unsafe_allow_html=True)
    km_coche = st.number_input('Kilómetros en coche por semana', min_value=0.0, step=0.1)
    km_moto = st.number_input('Kilómetros en moto por semana', min_value=0.0, step=0.1)
    km_transporte_publico = st.number_input('Kilómetros en transporte público por semana', min_value=0.0, step=0.1)

    # Sección de energía
    st.markdown("<h2 style='color: #155724;'>Energía</h2>", unsafe_allow_html=True)
    kwh_electricidad = st.number_input('Consumo de electricidad (kWh por mes)', min_value=0.0, step=0.1)
    m3_gas = st.number_input('Consumo de gas (m3 por mes)', min_value=0.0, step=0.1)

    # Otros consumos
    st.markdown("<h2 style='color: #155724;'>Otros Consumos</h2>", unsafe_allow_html=True)
    consumo_otro = st.number_input('Otros consumos de carbono (kg CO2 por mes)', min_value=0.0, step=0.1)

    # Botón para calcular
    if st.button('Calcular Huella de Carbono'):
        transporte = {'coche': km_coche * 4, 'moto': km_moto * 4, 'transporte_publico': km_transporte_publico * 4}
        energia = {'electricidad': kwh_electricidad, 'gas': m3_gas}
        huella_total = calcular_huella_de_carbono(transporte, energia, consumo_otro)
        
        st.subheader('Tu Huella de Carbono Total es:')
        st.write(f'{huella_total:.2f} kg CO2 por mes')

# Main function
if 'comenzar' not in st.session_state:
    st.session_state.comenzar = False

if st.session_state.comenzar:
    mostrar_calculadora()
else:
    mostrar_introduccion()

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

