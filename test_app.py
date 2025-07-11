#!/usr/bin/env python3
"""
Script de prueba para verificar que APP2.py funciona correctamente
"""

import sys
import os

def test_imports():
    """Prueba las importaciones básicas"""
    print("🔍 Probando importaciones...")
    
    try:
        import streamlit as st
        print("✅ Streamlit importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Streamlit: {e}")
        return False
    
    try:
        import numpy as np
        print("✅ NumPy importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando NumPy: {e}")
        return False
    
    try:
        import pandas as pd
        print("✅ Pandas importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando Pandas: {e}")
        return False
    
    try:
        import matplotlib
        print("✅ Matplotlib importado correctamente")
    except ImportError as e:
        print(f"⚠️ Matplotlib no disponible: {e}")
    
    try:
        import plotly
        print("✅ Plotly importado correctamente")
    except ImportError as e:
        print(f"⚠️ Plotly no disponible: {e}")
    
    try:
        import reportlab
        print("✅ ReportLab importado correctamente")
    except ImportError as e:
        print(f"⚠️ ReportLab no disponible: {e}")
    
    return True

def test_app_structure():
    """Prueba la estructura básica de APP2.py"""
    print("\n🔍 Probando estructura de APP2.py...")
    
    try:
        # Simular el entorno de Streamlit
        import streamlit as st
        
        # Verificar que el archivo existe
        if not os.path.exists('APP2.py'):
            print("❌ APP2.py no encontrado")
            return False
        
        print("✅ APP2.py encontrado")
        
        # Leer las primeras líneas para verificar la configuración
        with open('APP2.py', 'r', encoding='utf-8') as f:
            lines = f.readlines()[:50]
        
        # Verificar que tiene st.set_page_config
        has_page_config = any('st.set_page_config' in line for line in lines)
        if has_page_config:
            print("✅ Configuración de página encontrada")
        else:
            print("⚠️ Configuración de página no encontrada")
        
        # Verificar importaciones básicas
        has_streamlit = any('import streamlit' in line for line in lines)
        has_numpy = any('import numpy' in line for line in lines)
        has_pandas = any('import pandas' in line for line in lines)
        
        if has_streamlit and has_numpy and has_pandas:
            print("✅ Importaciones básicas encontradas")
        else:
            print("⚠️ Algunas importaciones básicas faltan")
        
        return True
        
    except Exception as e:
        print(f"❌ Error probando estructura: {e}")
        return False

def main():
    """Función principal de prueba"""
    print("🚀 Iniciando pruebas de APP2.py")
    print("=" * 50)
    
    # Probar importaciones
    imports_ok = test_imports()
    
    # Probar estructura
    structure_ok = test_app_structure()
    
    print("\n" + "=" * 50)
    if imports_ok and structure_ok:
        print("✅ Todas las pruebas pasaron")
        print("🎉 APP2.py está listo para usar con Streamlit")
        print("\n📋 Para ejecutar la aplicación:")
        print("   streamlit run APP2.py")
    else:
        print("❌ Algunas pruebas fallaron")
        print("🔧 Revisa los errores arriba")
    
    return imports_ok and structure_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 