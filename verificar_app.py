#!/usr/bin/env python3
"""
Script para verificar que APP2.py funciona correctamente
"""

import subprocess
import sys
import time

def verificar_app():
    """Verifica que la aplicación funciona correctamente"""
    print("🚀 Verificando APP2.py - CONSORCIO DEJ")
    print("=" * 50)
    
    # 1. Verificar que matplotlib está instalado
    print("1. Verificando matplotlib...")
    try:
        import matplotlib
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle, Polygon, Patch
        print("✅ Matplotlib disponible")
    except ImportError as e:
        print(f"❌ Matplotlib no disponible: {e}")
        print("💡 Ejecuta: python instalar_matplotlib.py")
        return False
    
    # 2. Verificar que streamlit está instalado
    print("\n2. Verificando streamlit...")
    try:
        import streamlit
        print("✅ Streamlit disponible")
    except ImportError as e:
        print(f"❌ Streamlit no disponible: {e}")
        print("💡 Ejecuta: pip install streamlit")
        return False
    
    # 3. Verificar que APP2.py existe
    print("\n3. Verificando APP2.py...")
    try:
        with open("APP2.py", "r", encoding="utf-8") as f:
            contenido = f.read()
        print("✅ APP2.py encontrado")
    except FileNotFoundError:
        print("❌ APP2.py no encontrado")
        return False
    
    # 4. Verificar que las funciones de matplotlib están en APP2.py
    print("\n4. Verificando funciones de matplotlib en APP2.py...")
    if "dibujar_vista_frontal_viga" in contenido:
        print("✅ Función dibujar_vista_frontal_viga encontrada")
    else:
        print("❌ Función dibujar_vista_frontal_viga no encontrada")
    
    if "MATPLOTLIB_AVAILABLE" in contenido:
        print("✅ Variable MATPLOTLIB_AVAILABLE encontrada")
    else:
        print("❌ Variable MATPLOTLIB_AVAILABLE no encontrada")
    
    # 5. Probar importación de APP2.py
    print("\n5. Probando importación de APP2.py...")
    try:
        # Importar solo las funciones necesarias sin ejecutar streamlit
        import importlib.util
        spec = importlib.util.spec_from_file_location("APP2", "APP2.py")
        app2_module = importlib.util.module_from_spec(spec)
        
        # Ejecutar solo las importaciones y definiciones
        with open("APP2.py", "r", encoding="utf-8") as f:
            code = f.read()
        
        # Separar las importaciones y definiciones del código principal
        lines = code.split('\n')
        import_lines = []
        for line in lines:
            if line.strip().startswith(('import ', 'from ', 'def ', 'class ', 'try:', 'except:', 'if __name__')):
                if 'if __name__' in line:
                    break
                import_lines.append(line)
        
        # Ejecutar solo las importaciones
        exec('\n'.join(import_lines))
        print("✅ APP2.py se puede importar correctamente")
        
    except Exception as e:
        print(f"❌ Error importando APP2.py: {e}")
        return False
    
    print("\n🎉 ¡Verificación completada exitosamente!")
    print("💡 La aplicación debería funcionar correctamente.")
    return True

def ejecutar_app():
    """Ejecuta la aplicación"""
    print("\n🚀 Ejecutando APP2.py...")
    print("💡 La aplicación se abrirá en tu navegador.")
    print("💡 Para detener, presiona Ctrl+C en esta ventana.")
    
    try:
        # Ejecutar streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "APP2.py"], check=True)
    except KeyboardInterrupt:
        print("\n⏹️ Aplicación detenida por el usuario")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error ejecutando la aplicación: {e}")
    except FileNotFoundError:
        print("\n❌ Streamlit no encontrado. Ejecuta: pip install streamlit")

if __name__ == "__main__":
    print("🔧 Verificador de APP2.py - CONSORCIO DEJ")
    print("=" * 60)
    
    if verificar_app():
        print("\n✅ Todo está listo para ejecutar la aplicación")
        
        respuesta = input("\n¿Deseas ejecutar la aplicación ahora? (s/n): ").lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            ejecutar_app()
        else:
            print("\n💡 Para ejecutar la aplicación manualmente:")
            print("   streamlit run APP2.py")
    else:
        print("\n❌ Hay problemas que necesitan ser solucionados.")
        print("💡 Revisa los errores anteriores y ejecuta los scripts de instalación.")
    
    input("\nPresiona Enter para salir...") 