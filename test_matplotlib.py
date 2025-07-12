#!/usr/bin/env python3
"""
Script de prueba para verificar que matplotlib funciona correctamente
"""

def test_matplotlib():
    """Prueba la instalación y funcionamiento de matplotlib"""
    print("🔍 Probando matplotlib...")
    
    try:
        # Importar matplotlib
        import matplotlib
        print("✅ matplotlib importado correctamente")
        
        # Configurar backend
        matplotlib.use('Agg')
        print("✅ Backend configurado correctamente")
        
        # Importar pyplot
        import matplotlib.pyplot as plt
        print("✅ pyplot importado correctamente")
        
        # Importar patches
        from matplotlib.patches import Rectangle, Polygon, Patch
        print("✅ patches importado correctamente")
        
        # Crear una figura simple
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_title("Prueba de Matplotlib")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        
        # Guardar la figura
        fig.savefig("test_matplotlib.png", dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        print("✅ Figura creada y guardada correctamente")
        print("✅ Matplotlib funciona perfectamente")
        return True
        
    except ImportError as e:
        print(f"❌ Error importando matplotlib: {e}")
        return False
    except Exception as e:
        print(f"❌ Error usando matplotlib: {e}")
        return False

if __name__ == "__main__":
    success = test_matplotlib()
    if success:
        print("\n🎉 ¡Matplotlib está funcionando correctamente!")
        print("💡 La aplicación debería mostrar gráficos sin problemas.")
    else:
        print("\n⚠️ Matplotlib tiene problemas.")
        print("💡 Ejecuta: pip install matplotlib")
        print("💡 O ejecuta: python instalar_dependencias.py") 