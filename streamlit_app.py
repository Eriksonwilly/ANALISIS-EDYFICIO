import streamlit as st
import numpy as np
import pandas as pd
import math

# Configuración de la página con manejo de errores
try:
    st.set_page_config(
        page_title="CONSORCIO DEJ - Análisis Estructural",
        page_icon="🏗️",
        layout="wide"
    )
except:
    pass

# Título principal
st.title("🏗️ CONSORCIO DEJ - Análisis Estructural")
st.markdown("### Aplicación de Análisis y Diseño Estructural")

# Verificar dependencias básicas
st.sidebar.title("🔧 Estado del Sistema")

# Verificar numpy
try:
    st.sidebar.success("✅ NumPy instalado")
except:
    st.sidebar.error("❌ NumPy no disponible")

# Verificar pandas
try:
    st.sidebar.success("✅ Pandas instalado")
except:
    st.sidebar.error("❌ Pandas no disponible")

# Menú principal
st.sidebar.title("📋 Menú Principal")
opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ["🏠 Inicio", "🔧 Diseño de Zapatas", "🔧 Diseño de Vigas", "🏢 Diseño de Columnas", "✂️ Ejercicio Básico de Corte"]
)

if opcion == "🏠 Inicio":
    st.header("🏠 Bienvenido a CONSORCIO DEJ")
    st.markdown("""
    ### Aplicación de Análisis y Diseño Estructural
    
    Esta aplicación te permite realizar:
    
    - **🔧 Diseño de Zapatas**: Cálculos de cimentaciones
    - **🔧 Diseño de Vigas**: Análisis de elementos de flexión
    - **🏢 Diseño de Columnas**: Verificación de elementos de compresión
    - **✂️ Ejercicio Básico de Corte**: Análisis de resistencia al corte
    
    ### Características:
    - ✅ Cálculos según ACI 318 y Norma E.060
    - ✅ Verificaciones automáticas
    - ✅ Reportes técnicos
    """)
    
    # Mostrar información del sistema
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Versión", "2.0")
    with col2:
        st.metric("Python", "3.8+")
    with col3:
        st.metric("Streamlit", "1.28+")

elif opcion == "🔧 Diseño de Zapatas":
    st.header("🔧 Diseño de Zapatas")
    
    # Datos de entrada básicos
    col1, col2 = st.columns(2)
    with col1:
        fc = st.number_input("f'c (kg/cm²)", 175, 700, 210)
        fy = st.number_input("fy (kg/cm²)", 2800, 6000, 4200)
        Pu = st.number_input("Carga Última Pu (kg)", 10000, 1000000, 100000)
    
    with col2:
        qu = st.number_input("Capacidad Portante qu (kg/cm²)", 0.5, 10.0, 2.0)
        FS = st.number_input("Factor de Seguridad", 2.0, 5.0, 3.0)
    
    if st.button("Calcular"):
        # Cálculo básico de zapata
        area_requerida = Pu / qu
        lado_zapata = math.sqrt(area_requerida)
        
        st.success("¡Cálculo completado!")
        st.metric("Área Requerida", f"{area_requerida:.0f} cm²")
        st.metric("Lado de Zapata", f"{lado_zapata:.1f} cm")

elif opcion == "🔧 Diseño de Vigas":
    st.header("🔧 Diseño de Vigas")
    
    # Datos de entrada básicos
    col1, col2 = st.columns(2)
    with col1:
        fc = st.number_input("f'c (kg/cm²)", 175, 700, 210, key="fc_viga")
        fy = st.number_input("fy (kg/cm²)", 2800, 6000, 4200, key="fy_viga")
        b = st.number_input("Ancho b (cm)", 20, 100, 25, key="b_viga")
    
    with col2:
        d = st.number_input("Peralte d (cm)", 30, 100, 50, key="d_viga")
        Mu = st.number_input("Momento Mu (kg·cm)", 10000, 10000000, 500000, key="Mu_viga")
    
    if st.button("Calcular", key="calc_viga"):
        # Cálculo básico de viga
        As_min = 0.8 * math.sqrt(fc) * b * d / fy
        As_max = 0.75 * 0.85 * 0.85 * (fc / fy) * (6000 / (6000 + fy)) * b * d
        
        st.success("¡Cálculo completado!")
        st.metric("As mínimo", f"{As_min:.1f} cm²")
        st.metric("As máximo", f"{As_max:.1f} cm²")

elif opcion == "🏢 Diseño de Columnas":
    st.header("🏢 Diseño de Columnas")
    
    # Datos de entrada básicos
    col1, col2 = st.columns(2)
    with col1:
        fc = st.number_input("f'c (kg/cm²)", 175, 700, 210, key="fc_col")
        fy = st.number_input("fy (kg/cm²)", 2800, 6000, 4200, key="fy_col")
        lado = st.number_input("Lado de columna (cm)", 20, 100, 30, key="lado_col")
    
    with col2:
        Pu = st.number_input("Carga axial Pu (kg)", 10000, 1000000, 100000, key="Pu_col")
        Ast = st.number_input("Acero longitudinal (cm²)", 5, 50, 15, key="Ast_col")
    
    if st.button("Calcular", key="calc_col"):
        # Cálculo básico de columna
        Ag = lado * lado
        rho = Ast / Ag * 100
        
        st.success("¡Cálculo completado!")
        st.metric("Área de concreto", f"{Ag:.0f} cm²")
        st.metric("Cuantía de acero", f"{rho:.1f}%")

elif opcion == "✂️ Ejercicio Básico de Corte":
    st.header("✂️ Ejercicio Básico de Corte")
    
    # Datos de entrada básicos
    col1, col2 = st.columns(2)
    with col1:
        fc = st.number_input("f'c (kg/cm²)", 175, 700, 210, key="fc_corte")
        b = st.number_input("Ancho b (cm)", 20, 100, 25, key="b_corte")
        d = st.number_input("Peralte d (cm)", 30, 100, 54, key="d_corte")
    
    with col2:
        Vu = st.number_input("Cortante Vu (kg)", 1000, 100000, 16600, key="Vu_corte")
        fy = st.number_input("fy (kg/cm²)", 2800, 6000, 4200, key="fy_corte")
    
    if st.button("Calcular", key="calc_corte"):
        # Cálculo básico de corte
        Vc = 0.53 * math.sqrt(fc) * b * d
        
        st.success("¡Cálculo completado!")
        st.metric("Corte del concreto Vc", f"{Vc:.0f} kg")
        
        if Vu > Vc:
            st.warning("⚠️ Se requiere refuerzo por corte")
        else:
            st.info("✅ No se requiere refuerzo por corte")

# Footer
st.markdown("---")
st.markdown("**CONSORCIO DEJ - Análisis Estructural v2.0**")
st.markdown("*Desarrollado para análisis y diseño estructural*") 