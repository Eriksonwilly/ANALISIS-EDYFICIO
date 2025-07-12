#!/usr/bin/env python3
"""
Script para instalar automáticamente todas las dependencias necesarias para la app de análisis estructural
"""

import subprocess
import sys
import os

def instalar_dependencia(package):
    """Instala una dependencia específica"""
    try:
        print(f"Instalando {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} instalado correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error instalando {package}: {e}")
        return False

def verificar_import(module_name):
    """Verifica si un módulo se puede importar correctamente"""
    try:
        __import__(module_name)
        print(f"✅ {module_name} está disponible")
        return True
    except ImportError:
        print(f"❌ {module_name} no está disponible")
        return False

def main():
    print("🔧 Instalador de Dependencias para APP2.py")
    print("=" * 50)
    
    # Lista de dependencias principales
    dependencias = [
        "streamlit>=1.28.0",
        "numpy>=1.21.0", 
        "pandas>=1.3.0",
        "matplotlib>=3.5.0",
        "plotly>=5.0.0",
        "reportlab>=3.6.0",
        "Pillow>=9.0.0",
        "scipy>=1.7.0"
    ]
    
    print("📦 Instalando dependencias...")
    exitos = 0
    total = len(dependencias)
    
    for dep in dependencias:
        if instalar_dependencia(dep):
            exitos += 1
    
    print(f"\n📊 Resumen: {exitos}/{total} dependencias instaladas correctamente")
    
    # Verificar imports críticos
    print("\n🔍 Verificando imports críticos...")
    modulos_criticos = ["streamlit", "numpy", "pandas", "matplotlib", "plotly"]
    
    for modulo in modulos_criticos:
        verificar_import(modulo)
    
    print("\n🎉 Instalación completada!")
    print("💡 Si hay errores, ejecuta: pip install -r requirements.txt")
    print("🚀 Para ejecutar la app: streamlit run APP2.py")

if __name__ == "__main__":
    main() 