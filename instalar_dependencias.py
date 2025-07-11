#!/usr/bin/env python3
"""
Script para instalar todas las dependencias necesarias para la aplicación
CONSORCIO DEJ - Análisis Estructural
"""

import subprocess
import sys
import os

def instalar_dependencia(package):
    """Instala una dependencia usando pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} instalado correctamente")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Error instalando {package}")
        return False

def main():
    print("🚀 Instalando dependencias para CONSORCIO DEJ - Análisis Estructural")
    print("=" * 70)
    
    # Lista de dependencias principales
    dependencias = [
        "streamlit>=1.28.0",
        "numpy>=1.24.0", 
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "plotly>=5.15.0",
        "reportlab>=4.0.0",
        "stripe>=6.0.0"
    ]
    
    # Dependencias opcionales
    dependencias_opcionales = [
        "openpyxl>=3.0.0",
        "xlrd>=2.0.0",
        "scipy>=1.10.0"
    ]
    
    print("📦 Instalando dependencias principales...")
    exitos = 0
    total = len(dependencias)
    
    for dep in dependencias:
        if instalar_dependencia(dep):
            exitos += 1
    
    print(f"\n📊 Progreso: {exitos}/{total} dependencias principales instaladas")
    
    print("\n📦 Instalando dependencias opcionales...")
    exitos_opc = 0
    total_opc = len(dependencias_opcionales)
    
    for dep in dependencias_opcionales:
        if instalar_dependencia(dep):
            exitos_opc += 1
    
    print(f"\n📊 Progreso: {exitos_opc}/{total_opc} dependencias opcionales instaladas")
    
    print("\n" + "=" * 70)
    if exitos == total:
        print("🎉 ¡Todas las dependencias principales instaladas correctamente!")
        print("🚀 La aplicación está lista para ejecutarse.")
        print("\nPara ejecutar la aplicación:")
        print("   streamlit run APP2.py")
    else:
        print("⚠️ Algunas dependencias no se pudieron instalar.")
        print("💡 Intenta ejecutar manualmente:")
        print("   pip install -r requirements.txt")
    
    print("\n📋 Dependencias instaladas:")
    print("   ✅ Streamlit - Framework web")
    print("   ✅ NumPy - Cálculos numéricos")
    print("   ✅ Pandas - Manipulación de datos")
    print("   ✅ Matplotlib - Gráficos básicos")
    print("   ✅ Plotly - Gráficos interactivos")
    print("   ✅ ReportLab - Generación de PDFs")
    print("   ✅ Stripe - Sistema de pagos")

if __name__ == "__main__":
    main() 