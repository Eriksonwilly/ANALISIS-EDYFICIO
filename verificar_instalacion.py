#!/usr/bin/env python3
"""
Script de verificación para CONSORCIO DEJ - Análisis Estructural
Verifica que todas las dependencias estén instaladas correctamente
"""

import sys
import importlib

def verificar_modulo(nombre_modulo, nombre_mostrar=None):
    """Verificar si un módulo está disponible"""
    if nombre_mostrar is None:
        nombre_mostrar = nombre_modulo
    
    try:
        importlib.import_module(nombre_modulo)
        print(f"✅ {nombre_mostrar} - OK")
        return True
    except ImportError:
        print(f"❌ {nombre_mostrar} - NO DISPONIBLE")
        return False

def main():
    print("=" * 60)
    print("   VERIFICACIÓN DE DEPENDENCIAS - CONSORCIO DEJ")
    print("=" * 60)
    print()
    
    # Verificar Python
    print(f"🐍 Python {sys.version}")
    print()
    
    # Lista de módulos a verificar
    modulos = [
        ("streamlit", "Streamlit"),
        ("pandas", "Pandas"),
        ("numpy", "NumPy"),
        ("matplotlib", "Matplotlib"),
        ("plotly", "Plotly"),
        ("reportlab", "ReportLab"),
        ("openpyxl", "OpenPyXL"),
    ]
    
    print("📦 Verificando dependencias:")
    print("-" * 40)
    
    modulos_ok = 0
    for modulo, nombre in modulos:
        if verificar_modulo(modulo, nombre):
            modulos_ok += 1
    
    print("-" * 40)
    print(f"📊 Resultado: {modulos_ok}/{len(modulos)} módulos disponibles")
    print()
    
    # Verificar archivos del proyecto
    print("📁 Verificando archivos del proyecto:")
    print("-" * 40)
    
    archivos_requeridos = [
        "APP2.py",
        "simple_payment_system.py",
        "admin_config.py",
        "admin_panel.py",
        "requirements.txt",
        ".streamlit/config.toml"
    ]
    
    import os
    archivos_ok = 0
    for archivo in archivos_requeridos:
        if os.path.exists(archivo):
            print(f"✅ {archivo} - OK")
            archivos_ok += 1
        else:
            print(f"❌ {archivo} - NO ENCONTRADO")
    
    print("-" * 40)
    print(f"📊 Resultado: {archivos_ok}/{len(archivos_requeridos)} archivos encontrados")
    print()
    
    # Resumen final
    print("=" * 60)
    print("   RESUMEN")
    print("=" * 60)
    
    if modulos_ok == len(modulos) and archivos_ok == len(archivos_requeridos):
        print("🎉 ¡Todo está listo! La aplicación debería funcionar correctamente.")
        print()
        print("🚀 Para ejecutar la aplicación:")
        print("   streamlit run APP2.py")
        print()
        print("🔑 Credenciales de prueba:")
        print("   admin / admin123 (Plan Empresarial)")
        print("   demo / demo (Plan Gratuito)")
    else:
        print("⚠️ Hay algunos problemas que resolver:")
        print()
        if modulos_ok < len(modulos):
            print("📦 Instalar dependencias faltantes:")
            print("   pip install -r requirements.txt")
            print()
        if archivos_ok < len(archivos_requeridos):
            print("📁 Verificar que todos los archivos del proyecto estén presentes")
            print()
        print("🔄 Después de resolver los problemas, ejecuta este script nuevamente.")

if __name__ == "__main__":
    main() 