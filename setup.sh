#!/bin/bash

# Script de configuración para Streamlit Cloud
# Este script se ejecuta automáticamente durante el despliegue

echo "🚀 Configurando CONSORCIO DEJ - Análisis Estructural..."

# Instalar dependencias del sistema
echo "📦 Instalando dependencias del sistema..."
apt-get update
apt-get install -y libgl1-mesa-glx libglib2.0-0 libgomp1 libfreetype6 libpng16-16

# Verificar instalación de Python
echo "🐍 Verificando Python..."
python --version

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r requirements.txt

# Verificar instalación
echo "🔍 Verificando instalación..."
python verificar_dependencias.py

echo "✅ Configuración completada!"
echo "🚀 La aplicación está lista para ejecutarse." 