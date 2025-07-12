#!/usr/bin/env python3
"""
Script específico para instalar matplotlib
"""

import subprocess
import sys
import os

def instalar_matplotlib():
    """Instala matplotlib y dependencias necesarias"""
    print("🔧 Instalando matplotlib...")
    
    try:
        # Actualizar pip primero
        print("📦 Actualizando pip...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
        
        # Instalar matplotlib
        print("📦 Instalando matplotlib...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
        
        # Instalar dependencias adicionales que matplotlib puede necesitar
        print("📦 Instalando dependencias adicionales...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
        
        print("✅ Matplotlib instalado correctamente")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante la instalación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def verificar_instalacion():
    """Verifica que matplotlib esté funcionando"""
    print("🔍 Verificando instalación...")
    
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle, Polygon, Patch
        
        # Crear una figura de prueba
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.plot([1, 2, 3], [1, 2, 1])
        ax.set_title("Prueba")
        plt.close(fig)
        
        print("✅ Matplotlib funciona correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error verificando matplotlib: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Instalador de Matplotlib para CONSORCIO DEJ")
    print("=" * 50)
    
    # Instalar matplotlib
    if instalar_matplotlib():
        # Verificar instalación
        if verificar_instalacion():
            print("\n🎉 ¡Matplotlib instalado y funcionando correctamente!")
            print("💡 Ya puedes ejecutar la aplicación con gráficos.")
        else:
            print("\n⚠️ Matplotlib se instaló pero hay problemas de configuración.")
            print("💡 Intenta reiniciar tu terminal/IDE.")
    else:
        print("\n❌ No se pudo instalar matplotlib.")
        print("💡 Verifica tu conexión a internet y permisos de administrador.")
    
    input("\nPresiona Enter para salir...") 