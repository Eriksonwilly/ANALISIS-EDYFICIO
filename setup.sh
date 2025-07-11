#!/bin/bash

echo "🚀 Configurando CONSORCIO DEJ - Análisis Estructural..."

# Instalar dependencias del sistema
echo "📦 Instalando dependencias del sistema..."
apt-get update
apt-get install -y libgl1-mesa-glx libglib2.0-0

# Verificar instalación de Python
echo "🐍 Verificando Python..."
python --version

# Instalar dependencias de Python
echo "📦 Instalando dependencias de Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Configuración completada!"
echo "🚀 La aplicación está lista para ejecutarse." 