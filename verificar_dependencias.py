#!/usr/bin/env python3
"""
Script para verificar que todas las dependencias estén instaladas correctamente
para la aplicación CONSORCIO DEJ - Análisis Estructural
"""

import sys
import importlib

def verificar_dependencia(nombre, import_name=None):
    """Verifica si una dependencia está instalada"""
    if import_name is None:
        import_name = nombre
    
    try:
        importlib.import_module(import_name)
        print(f"✅ {nombre} - INSTALADO")
        return True
    except ImportError:
        print(f"❌ {nombre} - NO INSTALADO")
        return False

def main():
    print("🔍 Verificando dependencias para CONSORCIO DEJ - Análisis Estructural")
    print("=" * 70)
    
    # Lista de dependencias principales
    dependencias = [
        ("Streamlit", "streamlit"),
        ("NumPy", "numpy"),
        ("Pandas", "pandas"),
        ("Matplotlib", "matplotlib"),
        ("Plotly", "plotly"),
        ("ReportLab", "reportlab"),
    ]
    
    # Dependencias opcionales
    dependencias_opcionales = [
        ("OpenPyXL", "openpyxl"),
        ("SciPy", "scipy"),
    ]
    
    print("📦 Verificando dependencias principales...")
    exitos = 0
    total = len(dependencias)
    
    for nombre, import_name in dependencias:
        if verificar_dependencia(nombre, import_name):
            exitos += 1
    
    print(f"\n📊 Progreso: {exitos}/{total} dependencias principales instaladas")
    
    print("\n📦 Verificando dependencias opcionales...")
    exitos_opc = 0
    total_opc = len(dependencias_opcionales)
    
    for nombre, import_name in dependencias_opcionales:
        if verificar_dependencia(nombre, import_name):
            exitos_opc += 1
    
    print(f"\n📊 Progreso: {exitos_opc}/{total_opc} dependencias opcionales instaladas")
    
    print("\n" + "=" * 70)
    if exitos == total:
        print("🎉 ¡Todas las dependencias principales están instaladas!")
        print("🚀 La aplicación está lista para ejecutarse.")
        print("\nPara ejecutar la aplicación:")
        print("   streamlit run APP2.py")
    else:
        print("⚠️ Algunas dependencias principales no están instaladas.")
        print("💡 Instala las dependencias faltantes:")
        print("   pip install -r requirements.txt")
        print("   o")
        print("   python instalar_dependencias.py")
    
    # Verificar versión de Python
    print(f"\n🐍 Versión de Python: {sys.version}")
    if sys.version_info >= (3, 8):
        print("✅ Versión de Python compatible")
    else:
        print("⚠️ Se recomienda Python 3.8 o superior")
    
    print("\n📋 Resumen de verificación:")
    print("   ✅ Streamlit - Framework web")
    print("   ✅ NumPy - Cálculos numéricos")
    print("   ✅ Pandas - Manipulación de datos")
    print("   ✅ Matplotlib - Gráficos básicos")
    print("   ✅ Plotly - Gráficos interactivos")
    print("   ✅ ReportLab - Generación de PDFs")
    
    if exitos < total:
        print("\n🔧 Dependencias faltantes:")
        for nombre, import_name in dependencias:
            try:
                importlib.import_module(import_name)
            except ImportError:
                print(f"   ❌ {nombre}")

if __name__ == "__main__":
    main() 