#!/usr/bin/env python3
"""
Script para instalar automáticamente las dependencias necesarias para la aplicación
de análisis estructural.
"""

import subprocess
import sys
import os
import platform

def print_banner():
    """Imprime el banner del instalador"""
    print("=" * 60)
    print("🔧 INSTALADOR DE DEPENDENCIAS - ANÁLISIS ESTRUCTURAL")
    print("=" * 60)
    print("📦 Instalando dependencias necesarias...")
    print()

def check_python_version():
    """Verifica la versión de Python"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: Se requiere Python 3.7 o superior")
        print(f"   Versión actual: {version.major}.{version.minor}.{version.micro}")
        return False
    else:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True

def install_package(package_name, description=""):
    """Instala un paquete usando pip"""
    print(f"📦 Instalando {package_name}... {description}")
    
    try:
        # Comando de instalación
        cmd = [sys.executable, "-m", "pip", "install", package_name, "--upgrade", "--quiet"]
        
        # Ejecutar instalación
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print(f"✅ {package_name} instalado correctamente")
            return True
        else:
            print(f"❌ Error instalando {package_name}: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout instalando {package_name}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado instalando {package_name}: {e}")
        return False

def install_dependencies():
    """Instala todas las dependencias necesarias"""
    dependencies = [
        ("streamlit", "Framework web para la aplicación"),
        ("matplotlib", "Biblioteca para gráficos"),
        ("numpy", "Biblioteca para cálculos numéricos"),
        ("pandas", "Biblioteca para manejo de datos"),
        ("plotly", "Biblioteca para gráficos interactivos"),
        ("reportlab", "Biblioteca para generación de PDFs"),
        ("scipy", "Biblioteca para cálculos científicos"),
        ("pillow", "Biblioteca para procesamiento de imágenes")
    ]
    
    success_count = 0
    total_count = len(dependencies)
    
    for package, description in dependencies:
        if install_package(package, description):
            success_count += 1
        print()
    
    return success_count, total_count

def verify_installation():
    """Verifica que las dependencias se instalaron correctamente"""
    print("🔍 Verificando instalación...")
    
    packages_to_check = [
        "streamlit", "matplotlib", "numpy", "pandas", 
        "plotly", "reportlab", "scipy", "PIL"
    ]
    
    success_count = 0
    total_count = len(packages_to_check)
    
    for package in packages_to_check:
        try:
            if package == "PIL":
                import PIL
            else:
                __import__(package)
            print(f"✅ {package} - OK")
            success_count += 1
        except ImportError:
            print(f"❌ {package} - NO DISPONIBLE")
    
    return success_count, total_count

def create_batch_file():
    """Crea un archivo .bat para Windows"""
    if platform.system() == "Windows":
        batch_content = """@echo off
echo Instalando dependencias para Analisis Estructural...
python instalar_dependencias.py
pause
"""
        with open("INSTALAR_DEPENDENCIAS.bat", "w", encoding="utf-8") as f:
            f.write(batch_content)
        print("📄 Archivo INSTALAR_DEPENDENCIAS.bat creado")

def main():
    """Función principal"""
    print_banner()
    
    # Verificar versión de Python
    if not check_python_version():
        input("Presiona Enter para salir...")
        return
    
    print()
    
    # Instalar dependencias
    print("🚀 Iniciando instalación de dependencias...")
    print()
    
    success_install, total_install = install_dependencies()
    
    print("=" * 60)
    print(f"📊 RESUMEN DE INSTALACIÓN:")
    print(f"   Paquetes instalados: {success_install}/{total_install}")
    print("=" * 60)
    
    # Verificar instalación
    print()
    success_verify, total_verify = verify_installation()
    
    print("=" * 60)
    print(f"📊 RESUMEN DE VERIFICACIÓN:")
    print(f"   Paquetes verificados: {success_verify}/{total_verify}")
    print("=" * 60)
    
    # Crear archivo batch para Windows
    create_batch_file()
    
    print()
    if success_verify == total_verify:
        print("🎉 ¡Todas las dependencias se instalaron correctamente!")
        print("🚀 Puedes ejecutar la aplicación con: streamlit run APP2.py")
    else:
        print("⚠️ Algunas dependencias no se instalaron correctamente.")
        print("💡 Intenta ejecutar manualmente: pip install matplotlib numpy pandas streamlit")
    
    print()
    input("Presiona Enter para salir...")

if __name__ == "__main__":
    main() 