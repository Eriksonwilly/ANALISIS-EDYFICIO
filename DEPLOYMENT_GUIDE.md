# 🚀 Guía de Despliegue - CONSORCIO DEJ

## 📋 Despliegue en Streamlit Cloud

### ✅ Archivos Necesarios

Asegúrate de tener estos archivos en tu repositorio:

```
📁 Tu Repositorio/
├── 📄 APP2.py                    # Aplicación principal
├── 📄 requirements.txt           # Dependencias de Python
├── 📄 packages.txt              # Dependencias del sistema
├── 📄 .streamlit/config.toml    # Configuración de Streamlit
├── 📄 setup.sh                  # Script de configuración
├── 📄 verificar_dependencias.py # Verificador de dependencias
└── 📄 README.md                 # Documentación
```

### 🔧 Pasos para el Despliegue

#### 1. Preparar el Repositorio
```bash
# Asegúrate de que todos los archivos estén en tu repositorio
git add .
git commit -m "Preparar para despliegue en Streamlit Cloud"
git push origin main
```

#### 2. Conectar con Streamlit Cloud
1. Ve a [share.streamlit.io](https://share.streamlit.io)
2. Inicia sesión con tu cuenta de GitHub
3. Selecciona tu repositorio
4. Configura el archivo principal: `APP2.py`
5. Haz clic en "Deploy!"

#### 3. Configuración Recomendada
- **Main file path**: `APP2.py`
- **Python version**: 3.8 o superior
- **Requirements file**: `requirements.txt`

### 📦 Dependencias Incluidas

#### requirements.txt
```
streamlit>=1.28.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
plotly>=5.15.0
reportlab>=4.0.0
```

#### packages.txt
```
libgl1-mesa-glx
libglib2.0-0
libgomp1
libfreetype6
libpng16-16
```

### 🔍 Verificación del Despliegue

#### Verificar Dependencias
```bash
# Ejecutar el verificador
python verificar_dependencias.py
```

#### Verificar Funcionalidades
1. ✅ **Autenticación**: Login/Registro
2. ✅ **Diseño de Zapatas**: Cálculos y gráficos
3. ✅ **Diseño de Vigas**: Cálculos y dibujos
4. ✅ **Diseño de Columnas**: Cálculos y visualizaciones
5. ✅ **Ejercicio de Corte**: Cálculos y diagramas
6. ✅ **Gráficos**: Plotly y Matplotlib
7. ✅ **PWA**: Funcionalidades offline

### 🛠️ Solución de Problemas

#### Error: "Error al instalar requisitos"
**Solución:**
1. Verifica que `requirements.txt` esté en la raíz del repositorio
2. Asegúrate de que las versiones sean compatibles
3. Revisa los logs de Streamlit Cloud

#### Error: "ModuleNotFoundError"
**Solución:**
1. Ejecuta `python verificar_dependencias.py`
2. Instala dependencias faltantes: `pip install -r requirements.txt`
3. Verifica que `packages.txt` esté presente

#### Error: "Gráficos no aparecen"
**Solución:**
1. Verifica instalación de matplotlib: `pip install matplotlib`
2. Verifica instalación de plotly: `pip install plotly`
3. Revisa los logs de la aplicación

### 📊 Monitoreo

#### Logs de Streamlit Cloud
- Ve a tu aplicación en Streamlit Cloud
- Haz clic en "Manage app"
- Revisa la pestaña "Logs"

#### Métricas de Rendimiento
- Tiempo de carga inicial
- Uso de memoria
- Errores de dependencias

### 🔄 Actualizaciones

#### Actualizar la Aplicación
```bash
# Hacer cambios en tu código
git add .
git commit -m "Actualizar aplicación"
git push origin main

# Streamlit Cloud se actualizará automáticamente
```

#### Actualizar Dependencias
1. Modifica `requirements.txt`
2. Haz commit y push
3. Streamlit Cloud reinstalará las dependencias

### 📱 Funcionalidades PWA

#### Configuración PWA
- La aplicación incluye funcionalidades PWA
- Se puede instalar en dispositivos móviles
- Funciona offline con cache

#### Generar PWA
```bash
python generar_pwa.py
```

### 🎯 Optimizaciones

#### Para Mejor Rendimiento
1. **Caché de datos**: Usar `@st.cache_data`
2. **Caché de funciones**: Usar `@st.cache_resource`
3. **Lazy loading**: Cargar módulos solo cuando se necesiten

#### Para Menor Uso de Memoria
1. **Limpiar variables**: Usar `del` para variables grandes
2. **Optimizar gráficos**: Reducir tamaño de figuras
3. **Manejo de errores**: Capturar excepciones apropiadamente

### 📞 Soporte

#### Recursos Útiles
- [Documentación de Streamlit](https://docs.streamlit.io)
- [Streamlit Cloud](https://share.streamlit.io)
- [Foros de Streamlit](https://discuss.streamlit.io)

#### Contacto
- **Desarrollador**: CONSORCIO DEJ
- **Versión**: 2.0
- **Fecha**: 2024

---

**¡Tu aplicación CONSORCIO DEJ está lista para el despliegue! 🚀✨** 