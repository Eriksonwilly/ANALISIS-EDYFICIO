#!/usr/bin/env python3
"""
Script para instalar dependencias básicas
"""

import subprocess
import sys

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
    print("🚀 Instalando dependencias básicas")
    print("=" * 50)
    
    # Dependencias básicas
    dependencias = [
        "streamlit==1.28.1",
        "numpy==1.24.3",
        "pandas==2.0.3",
    ]
    
    print("📦 Instalando dependencias...")
    exitos = 0
    total = len(dependencias)
    
    for dep in dependencias:
        if instalar_dependencia(dep):
            exitos += 1
    
    print(f"\n📊 Progreso: {exitos}/{total} dependencias instaladas")
    
    print("\n" + "=" * 50)
    if exitos == total:
        print("🎉 ¡Todas las dependencias instaladas correctamente!")
        print("🚀 La aplicación está lista para ejecutarse.")
        print("\nPara ejecutar la aplicación:")
        print("   streamlit run streamlit_app.py")
    else:
        print("⚠️ Algunas dependencias no se pudieron instalar.")
        print("💡 Intenta ejecutar manualmente:")
        print("   pip install -r requirements.txt")

if __name__ == "__main__":
    main() 