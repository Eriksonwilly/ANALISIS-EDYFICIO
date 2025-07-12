#!/usr/bin/env python3
"""
Script para verificar que todas las dependencias están instaladas correctamente
"""

def verificar_modulo(nombre, import_name=None):
    """Verifica si un módulo está disponible"""
    if import_name is None:
        import_name = nombre
    
    try:
        __import__(import_name)
        print(f"✅ {nombre} - OK")
        return True
    except ImportError as e:
        print(f"❌ {nombre} - ERROR: {e}")
        return False

def main():
    print("🔍 Verificador de Dependencias para APP2.py")
    print("=" * 50)
    
    # Lista de módulos críticos
    modulos = [
        ("Streamlit", "streamlit"),
        ("NumPy", "numpy"),
        ("Pandas", "pandas"),
        ("Matplotlib", "matplotlib"),
        ("Plotly", "plotly"),
        ("ReportLab", "reportlab"),
        ("Pillow", "PIL"),
        ("SciPy", "scipy")
    ]
    
    exitos = 0
    total = len(modulos)
    
    for nombre, import_name in modulos:
        if verificar_modulo(nombre, import_name):
            exitos += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Resumen: {exitos}/{total} módulos disponibles")
    
    if exitos == total:
        print("🎉 ¡Todas las dependencias están instaladas correctamente!")
        print("🚀 La aplicación debería funcionar sin problemas.")
        
        # Verificación adicional de matplotlib
        try:
            import matplotlib
            import matplotlib.pyplot as plt
            from matplotlib.patches import Rectangle, Polygon, Patch
            print("✅ Matplotlib está configurado correctamente para gráficos")
        except Exception as e:
            print(f"⚠️ Matplotlib tiene problemas: {e}")
    else:
        print("⚠️ Algunas dependencias faltan.")
        print("💡 Ejecuta: pip install -r requirements.txt")
        print("💡 O ejecuta: python instalar_dependencias.py")

if __name__ == "__main__":
    main() 