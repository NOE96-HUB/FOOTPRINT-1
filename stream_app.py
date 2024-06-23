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

# Título
st.title('Calculadora de Huella de Carbono')

# Sección de transporte
st.header('Transporte')
km_coche = st.number_input('Kilómetros en coche por semana', min_value=0.0, step=0.1)
km_moto = st.number_input('Kilómetros en moto por semana', min_value=0.0, step=0.1)
km_transporte_publico = st.number_input('Kilómetros en transporte público por semana', min_value=0.0, step=0.1)

# Sección de energía
st.header('Energía')
kwh_electricidad = st.number_input('Consumo de electricidad (kWh por mes)', min_value=0.0, step=0.1)
m3_gas = st.number_input('Consumo de gas (m3 por mes)', min_value=0.0, step=0.1)

# Otros consumos
st.header('Otros Consumos')
consumo_otro = st.number_input('Otros consumos de carbono (kg CO2 por mes)', min_value=0.0, step=0.1)

# Botón para calcular
if st.button('Calcular Huella de Carbono'):
    transporte = {'coche': km_coche * 4, 'moto': km_moto * 4, 'transporte_publico': km_transporte_publico * 4}
    energia = {'electricidad': kwh_electricidad, 'gas': m3_gas}
    huella_total = calcular_huella_de_carbono(transporte, energia, consumo_otro)
    
    st.subheader('Tu Huella de Carbono Total es:')
    st.write(f'{huella_total:.2f} kg CO2 por mes')
