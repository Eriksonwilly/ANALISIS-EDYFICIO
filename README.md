# 🏗️ Análisis Estructural - CONSORCIO DEJ

Aplicación web para análisis estructural desarrollada con Streamlit.

## 📋 Características

- **Análisis de Vigas**: Cálculo de cortantes y momentos
- **Diseño de Elementos**: Vigas, columnas y zapatas
- **Ejercicios de Corte**: Cálculos detallados de refuerzo por cortante
- **Visualizaciones**: Gráficos interactivos y diagramas
- **Generación de PDFs**: Reportes detallados
- **Sistema de Pagos**: Planes premium y empresarial

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática (Recomendada)

1. **Windows**: Doble clic en `INSTALAR_DEPENDENCIAS.bat`
2. **Otros sistemas**: Ejecuta `python instalar_dependencias.py`

### Opción 2: Instalación Manual

```bash
# Instalar dependencias
pip install -r requirements.txt

# O instalar individualmente
pip install streamlit matplotlib numpy pandas plotly reportlab pillow scipy
```

### Opción 3: Instalación con Conda

```bash
conda install streamlit matplotlib numpy pandas plotly
conda install -c conda-forge reportlab pillow scipy
```

## 🎯 Ejecutar la Aplicación

```bash
streamlit run APP2.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📦 Dependencias Principales

| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| streamlit | ≥1.28.0 | Framework web |
| matplotlib | ≥3.5.0 | Gráficos estáticos |
| numpy | ≥1.21.0 | Cálculos numéricos |
| pandas | ≥1.3.0 | Manejo de datos |
| plotly | ≥5.0.0 | Gráficos interactivos |
| reportlab | ≥3.6.0 | Generación de PDFs |
| scipy | ≥1.7.0 | Cálculos científicos |
| Pillow | ≥9.0.0 | Procesamiento de imágenes |

## 🔧 Solución de Problemas

### Error: "Matplotlib no está instalado"

Si ves este error, sigue estos pasos:

1. **Instalación automática**: Usa el botón "🔧 Instalar Matplotlib Automáticamente" en la app
2. **Instalación manual**: Ejecuta `pip install matplotlib`
3. **Reiniciar**: Reinicia la aplicación después de instalar

### Error: "Streamlit no encontrado"

```bash
pip install streamlit
```

### Error: "Numpy no encontrado"

```bash
pip install numpy
```

## 📁 Estructura del Proyecto

```
📁 ANALISIS_EDIFICIO/
├── 📄 APP2.py                    # Aplicación principal
├── 📄 instalar_dependencias.py   # Script de instalación
├── 📄 requirements.txt           # Dependencias
├── 📄 INSTALAR_DEPENDENCIAS.bat  # Instalador Windows
└── 📄 README.md                  # Este archivo
```

## 🎨 Funcionalidades

### 📐 Análisis de Vigas
- Vigas simplemente apoyadas
- Vigas empotradas
- Vigas continuas
- Cálculo de cortantes y momentos

### 🔬 Diseño de Elementos
- **Vigas**: Diseño por flexión y cortante
- **Columnas**: Diseño por compresión y flexión
- **Zapatas**: Diseño por capacidad de carga

### ✂️ Ejercicios de Corte
- Cálculo de refuerzo por cortante
- Verificación de espaciamientos
- Visualización de estribos
- Generación de diagramas

### 📊 Visualizaciones
- Diagramas de cortantes y momentos
- Vista frontal de vigas
- Corte lateral de elementos
- Gráficos interactivos

## 💳 Planes Disponibles

### 🆓 Plan Gratuito
- Acceso básico a cálculos
- Gráficos limitados
- Sin generación de PDFs

### ⭐ Plan Premium
- Todos los cálculos
- Gráficos completos
- Generación de PDFs
- Ejercicios detallados

### 🏢 Plan Empresarial
- Todo del plan Premium
- Soporte prioritario
- Funcionalidades avanzadas

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📞 Soporte

- **Email**: soporte@consorciodej.com
- **Documentación**: [docs.consorciodej.com](https://docs.consorciodej.com)
- **Issues**: [GitHub Issues](https://github.com/consorciodej/analisis-estructural/issues)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- **Arthur H. Nilson**: Referencias de diseño de estructuras de concreto
- **McCormac**: Referencias de análisis estructural
- **ACI 318-19**: Código de diseño de concreto

---

**Desarrollado con ❤️ por CONSORCIO DEJ**
