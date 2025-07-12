# 🔧 Instrucciones de Instalación - APP2.py

## Problema: "📊 Visualización no disponible - Matplotlib no está instalado"

Si ves este mensaje, significa que matplotlib no está instalado correctamente en tu entorno de Python.

## 🚀 Solución Rápida

### Opción 1: Script Automático (Recomendado)

**Windows:**
```bash
# Doble clic en el archivo
INSTALAR_DEPENDENCIAS.bat
```

**Linux/Mac:**
```bash
# Dar permisos de ejecución
chmod +x INSTALAR_DEPENDENCIAS.sh
# Ejecutar
./INSTALAR_DEPENDENCIAS.sh
```

### Opción 2: Comando Manual

```bash
pip install -r requirements.txt
```

### Opción 3: Script Python

```bash
python instalar_dependencias.py
```

## 🔍 Verificar Instalación

Después de instalar, ejecuta:

```bash
python verificar_instalacion.py
```

Deberías ver:
```
✅ Streamlit - OK
✅ NumPy - OK
✅ Pandas - OK
✅ Matplotlib - OK
✅ Plotly - OK
✅ ReportLab - OK
✅ Pillow - OK
✅ SciPy - OK
```

## 🚀 Ejecutar la Aplicación

```bash
streamlit run APP2.py
```

## 📦 Dependencias Incluidas

- **streamlit** >= 1.28.0 - Framework web
- **numpy** >= 1.21.0 - Cálculos numéricos
- **pandas** >= 1.3.0 - Manipulación de datos
- **matplotlib** >= 3.5.0 - Gráficos (¡CRÍTICO!)
- **plotly** >= 5.0.0 - Gráficos interactivos
- **reportlab** >= 3.6.0 - Generación de PDFs
- **Pillow** >= 9.0.0 - Procesamiento de imágenes
- **scipy** >= 1.7.0 - Funciones científicas

## ❗ Solución de Problemas

### Error: "matplotlib no está instalado"

1. **Verifica Python:**
   ```bash
   python --version
   ```

2. **Verifica pip:**
   ```bash
   pip --version
   ```

3. **Instala matplotlib específicamente:**
   ```bash
   pip install matplotlib
   ```

4. **Reinicia tu terminal/IDE**

### Error: "No module named 'matplotlib'"

1. **Verifica el entorno virtual:**
   ```bash
   # Si usas venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **Instala en el entorno correcto:**
   ```bash
   pip install matplotlib
   ```

### Error: "Backend no disponible"

1. **Instala dependencias adicionales:**
   ```bash
   pip install tkinter
   # O en Ubuntu/Debian:
   sudo apt-get install python3-tk
   ```

## 🎯 Resultado Esperado

Después de la instalación correcta, en la sección "Ejercicio Básico de Corte" deberías ver:

- ✅ **Vista Frontal de la Viga** con acero de temperatura
- ✅ **Gráficos de cortantes** 
- ✅ **Visualización de estribos**
- ✅ **Todas las gráficas funcionando**

## 📞 Soporte

Si sigues teniendo problemas:

1. Ejecuta `python verificar_instalacion.py`
2. Copia el resultado completo
3. Verifica que estás en el directorio correcto del proyecto
4. Asegúrate de que Python y pip están actualizados 