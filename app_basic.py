import streamlit as st

st.title("🏗️ CONSORCIO DEJ - Análisis Estructural")
st.write("### Aplicación de Prueba - Funcionando Correctamente")

st.success("✅ ¡La aplicación se ha desplegado correctamente!")

st.markdown("""
### Funcionalidades Disponibles:
- ✅ **Diseño de Zapatas**: Cálculos de cimentaciones
- ✅ **Diseño de Vigas**: Análisis de elementos de flexión  
- ✅ **Diseño de Columnas**: Verificación de elementos de compresión
- ✅ **Ejercicio de Corte**: Análisis de resistencia al corte

### Información Técnica:
- **Versión**: 2.0
- **Framework**: Streamlit
- **Estado**: Operativo
- **Despliegue**: Streamlit Cloud
""")

# Cálculo de ejemplo
st.subheader("🔧 Ejemplo de Cálculo")
fc = st.slider("f'c (kg/cm²)", 175, 700, 210)
b = st.slider("Ancho b (cm)", 20, 100, 25)
d = st.slider("Peralte d (cm)", 30, 100, 50)

if st.button("Calcular"):
    # Cálculo básico
    As_min = 0.8 * (fc**0.5) * b * d / 4200
    st.metric("As mínimo", f"{As_min:.1f} cm²")
    st.balloons()

st.markdown("---")
st.markdown("**CONSORCIO DEJ - Análisis Estructural v2.0**")
st.markdown("*Desarrollado para análisis y diseño estructural*") 