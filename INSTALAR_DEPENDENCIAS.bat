@echo off
echo 🔧 Instalador de Dependencias para APP2.py
echo ============================================
echo.

echo 📦 Instalando dependencias desde requirements.txt...
pip install -r requirements.txt

echo.
echo 🔍 Verificando instalación...
python -c "import matplotlib; print('✅ matplotlib instalado correctamente')"
python -c "import streamlit; print('✅ streamlit instalado correctamente')"
python -c "import numpy; print('✅ numpy instalado correctamente')"
python -c "import pandas; print('✅ pandas instalado correctamente')"
python -c "import plotly; print('✅ plotly instalado correctamente')"

echo.
echo 🎉 Instalación completada!
echo 🚀 Para ejecutar la app: streamlit run APP2.py
echo.
pause 