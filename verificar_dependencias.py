#!/usr/bin/env python3
"""
Script para verificar dependencias básicas
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
    print("🔍 Verificando dependencias básicas")
    print("=" * 50)
    
    # Dependencias básicas
    dependencias = [
        ("Streamlit", "streamlit"),
        ("NumPy", "numpy"),
        ("Pandas", "pandas"),
    ]
    
    print("📦 Verificando dependencias...")
    exitos = 0
    total = len(dependencias)
    
    for nombre, import_name in dependencias:
        if verificar_dependencia(nombre, import_name):
            exitos += 1
    
    print(f"\n📊 Progreso: {exitos}/{total} dependencias instaladas")
    
    print("\n" + "=" * 50)
    if exitos == total:
        print("🎉 ¡Todas las dependencias están instaladas!")
        print("🚀 La aplicación está lista para ejecutarse.")
    else:
        print("⚠️ Algunas dependencias no están instaladas.")
        print("💡 Instala las dependencias: pip install -r requirements.txt")
    
    print(f"\n🐍 Versión de Python: {sys.version}")

if __name__ == "__main__":
    main() 