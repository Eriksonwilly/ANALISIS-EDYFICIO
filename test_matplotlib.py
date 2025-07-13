#!/usr/bin/env python3
"""
Script de prueba para verificar la instalación y funcionamiento de matplotlib
"""

import sys
import subprocess

def test_matplotlib_installation():
    """Prueba la instalación de matplotlib"""
    print("🔍 Probando instalación de matplotlib...")
    
    try:
        import matplotlib
        print("✅ matplotlib importado correctamente")
        
        import matplotlib.pyplot as plt
        print("✅ matplotlib.pyplot importado correctamente")
        
        from matplotlib.patches import Rectangle, Patch
        print("✅ matplotlib.patches importado correctamente")
        
        # Probar creación de figura
        fig, ax = plt.subplots(figsize=(6, 4))
        rect = Rectangle((0, 0), 1, 1, facecolor='blue')
        ax.add_patch(rect)
        plt.close(fig)
        print("✅ Creación de figura y patches exitosa")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error importando matplotlib: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def install_matplotlib():
    """Instala matplotlib si no está disponible"""
    print("🔧 Instalando matplotlib...")
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "matplotlib", "--quiet"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print("✅ matplotlib instalado exitosamente")
            return True
        else:
            print(f"❌ Error en instalación: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error instalando matplotlib: {e}")
        return False

def main():
    """Función principal"""
    print("=" * 50)
    print("🧪 PRUEBA DE MATPLOTLIB")
    print("=" * 50)
    
    # Probar si matplotlib está disponible
    if test_matplotlib_installation():
        print("\n🎉 matplotlib funciona correctamente!")
        return True
    
    # Si no está disponible, intentar instalar
    print("\n📦 matplotlib no está disponible, intentando instalar...")
    if install_matplotlib():
        print("\n🔄 Reintentando prueba después de instalación...")
        if test_matplotlib_installation():
            print("\n🎉 matplotlib instalado y funcionando correctamente!")
            return True
    
    print("\n❌ No se pudo instalar o configurar matplotlib")
    return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 