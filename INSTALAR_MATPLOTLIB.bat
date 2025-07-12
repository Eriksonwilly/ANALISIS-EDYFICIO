@echo off
chcp 65001 >nul
echo.
echo ========================================
echo    INSTALADOR DE MATPLOTLIB
echo    CONSORCIO DEJ - Análisis Estructural
echo ========================================
echo.

echo 🔧 Instalando matplotlib...
python -m pip install --upgrade pip
python -m pip install matplotlib
python -m pip install numpy
python -m pip install pillow

echo.
echo 🔍 Verificando instalación...
python test_matplotlib.py

echo.
echo ✅ Proceso completado
echo 💡 Si todo está bien, ya puedes ejecutar la aplicación
echo.
pause 