# 🏗️ CONSORCIO DEJ - Análisis Estructural

Aplicación profesional de análisis estructural desarrollada con Streamlit y Python.

## 🚀 Instalación Rápida

### Opción 1: Instalación Automática (Recomendada)
```bash
# Clonar el repositorio
git clone <tu-repositorio>
cd analisis-edyficio

# Ejecutar instalación automática
python ejecutar_app_completo.py
```

### Opción 2: Instalación Manual
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
streamlit run APP2.py
```

## 📋 Dependencias

- Python 3.8+
- Streamlit 1.28.0+
- Pandas 1.5.0+
- NumPy 1.21.0+
- Matplotlib 3.5.0+
- Plotly 5.0.0+
- ReportLab 3.6.0+
- OpenPyXL 3.0.0+

## 🔑 Credenciales de Prueba

- **Administrador:** admin / admin123 (Plan Empresarial)
- **Demo:** demo / demo (Plan Gratuito)

## 🎯 Características

### Plan Gratuito
- ✅ Cálculos básicos de análisis estructural
- ✅ Resultados simples con gráficos básicos
- ✅ Reporte básico descargable
- ✅ Análisis de propiedades de materiales

### Plan Premium
- ⭐ Análisis completo con ACI 318-2025
- ⭐ Cálculos de predimensionamiento automáticos
- ⭐ Reportes técnicos en PDF
- ⭐ Gráficos interactivos avanzados
- ⭐ Verificaciones de estabilidad completas
- ⭐ Fórmulas de diseño estructural detalladas

## 🛠️ Solución de Problemas

### Error: ModuleNotFoundError
Si encuentras errores de módulos no encontrados:

1. **Verificar Python:**
   ```bash
   python --version
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Crear entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

### Error: Matplotlib no disponible
La aplicación maneja automáticamente la falta de matplotlib y muestra warnings apropiados.

## 📁 Estructura del Proyecto

```
analisis-edyficio/
├── APP2.py                    # Aplicación principal
├── requirements.txt           # Dependencias
├── setup.py                  # Script de instalación
├── simple_payment_system.py  # Sistema de pagos
├── admin_config.py           # Configuración admin
├── admin_panel.py            # Panel de administración
├── .streamlit/
│   └── config.toml          # Configuración Streamlit
└── README.md                # Este archivo
```

## 🌐 Despliegue en Streamlit Cloud

1. Sube tu código a GitHub
2. Conecta tu repositorio a Streamlit Cloud
3. La aplicación se desplegará automáticamente

## 📞 Soporte

- 📧 Email: contacto@consorciodej.com
- 📱 WhatsApp: +51 999 888 777
- 🌐 Web: www.consorciodej.com

## 📄 Licencia

Desarrollado por CONSORCIO DEJ - Ingeniería y Construcción
