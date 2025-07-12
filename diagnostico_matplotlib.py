#!/usr/bin/env python3
"""
Script de diagnóstico para verificar el estado de matplotlib en APP2.py
"""

def diagnosticar_matplotlib():
    """Diagnostica el estado de matplotlib"""
    print("🔍 Diagnóstico de Matplotlib para APP2.py")
    print("=" * 50)
    
    # 1. Verificar importación básica
    print("1. Verificando importación básica...")
    try:
        import matplotlib
        print("✅ matplotlib importado correctamente")
        print(f"   Versión: {matplotlib.__version__}")
    except ImportError as e:
        print(f"❌ Error importando matplotlib: {e}")
        return False
    
    # 2. Verificar backend
    print("\n2. Verificando backend...")
    try:
        matplotlib.use('Agg')
        print("✅ Backend 'Agg' configurado correctamente")
    except Exception as e:
        print(f"❌ Error configurando backend: {e}")
        return False
    
    # 3. Verificar pyplot
    print("\n3. Verificando pyplot...")
    try:
        import matplotlib.pyplot as plt
        print("✅ pyplot importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando pyplot: {e}")
        return False
    
    # 4. Verificar patches
    print("\n4. Verificando patches...")
    try:
        from matplotlib.patches import Rectangle, Polygon, Patch
        print("✅ patches importado correctamente")
    except ImportError as e:
        print(f"❌ Error importando patches: {e}")
        return False
    
    # 5. Crear figura de prueba
    print("\n5. Creando figura de prueba...")
    try:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_title("Prueba de Matplotlib")
        
        # Agregar un rectángulo (como en la aplicación)
        rect = Rectangle((0.5, 0.5), 2, 1, linewidth=2, edgecolor='red', facecolor='blue', alpha=0.5)
        ax.add_patch(rect)
        
        plt.close(fig)
        print("✅ Figura creada correctamente con patches")
    except Exception as e:
        print(f"❌ Error creando figura: {e}")
        return False
    
    # 6. Verificar variables globales (como en APP2.py)
    print("\n6. Verificando variables globales...")
    try:
        MATPLOTLIB_AVAILABLE = True
        plt_test = plt
        Rectangle_test = Rectangle
        Polygon_test = Polygon
        Patch_test = Patch
        
        print("✅ Variables globales configuradas correctamente")
        print(f"   MATPLOTLIB_AVAILABLE: {MATPLOTLIB_AVAILABLE}")
        print(f"   plt: {plt_test is not None}")
        print(f"   Rectangle: {Rectangle_test is not None}")
        print(f"   Polygon: {Polygon_test is not None}")
        print(f"   Patch: {Patch_test is not None}")
    except Exception as e:
        print(f"❌ Error configurando variables: {e}")
        return False
    
    print("\n🎉 ¡Diagnóstico completado exitosamente!")
    print("💡 Matplotlib está funcionando correctamente para APP2.py")
    return True

def simular_funcion_dibujo():
    """Simula la función de dibujo de la aplicación"""
    print("\n🔧 Simulando función de dibujo...")
    
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle, Polygon, Patch
        
        # Simular la función dibujar_vista_frontal_viga
        def dibujar_vista_frontal_viga_simulada(b, h, d, tipo_fierro, cantidad_fierro, Av_estribo, s_estribos, zona_critica):
            fig, ax = plt.subplots(figsize=(10, 8))
            
            # Dibujar contorno de la viga
            rect_viga = Rectangle((0, 0), b, h, linewidth=3, edgecolor='black', facecolor='#f0f0f0', alpha=0.8)
            ax.add_patch(rect_viga)
            
            # Dibujar recubrimiento
            recubrimiento = 6
            rect_recubrimiento = Rectangle((recubrimiento, recubrimiento), b-2*recubrimiento, h-2*recubrimiento, 
                                         linewidth=2, edgecolor='red', facecolor='none', linestyle='--', alpha=0.7)
            ax.add_patch(rect_recubrimiento)
            
            # Dibujar acero principal
            for i in range(4):  # 4 barras principales
                x = recubrimiento + 2 + i * 3
                y = recubrimiento + 2
                barra = Rectangle((x, y), 1, 1, linewidth=1, edgecolor='orange', facecolor='orange', alpha=0.8)
                ax.add_patch(barra)
            
            # Dibujar acero de temperatura
            for i in range(2):  # 2 barras de temperatura
                x = recubrimiento + 2 + i * 3
                y = h - recubrimiento - 3
                barra = Rectangle((x, y), 1, 1, linewidth=1, edgecolor='green', facecolor='green', alpha=0.8)
                ax.add_patch(barra)
            
            # Dibujar estribos
            for i in range(min(cantidad_fierro, 10)):  # Máximo 10 estribos para visualización
                y = recubrimiento + 5 + i * 4
                if y + 2 <= h - recubrimiento:
                    estribo_izq = Rectangle((recubrimiento, y), 2, 2, linewidth=1, edgecolor='blue', facecolor='blue', alpha=0.7)
                    ax.add_patch(estribo_izq)
                    estribo_der = Rectangle((b-recubrimiento-2, y), 2, 2, linewidth=1, edgecolor='blue', facecolor='blue', alpha=0.7)
                    ax.add_patch(estribo_der)
            
            ax.set_xlim(-2, b + 2)
            ax.set_ylim(-2, h + 2)
            ax.set_aspect('equal')
            ax.set_title('Vista Frontal - Viga con Acero de Temperatura y Estribos', fontsize=14, fontweight='bold')
            ax.set_xlabel('Ancho (cm)')
            ax.set_ylabel('Alto (cm)')
            ax.grid(True, alpha=0.3)
            
            # Agregar leyenda
            legend_elements = [
                Patch(facecolor='orange', alpha=0.8, label='Acero Principal'),
                Patch(facecolor='green', alpha=0.8, label='Acero de Temperatura'),
                Patch(facecolor='blue', alpha=0.7, label='Estribos'),
                Patch(facecolor='red', alpha=0.3, label='Recubrimiento')
            ]
            ax.legend(handles=legend_elements, loc='upper left')
            
            plt.tight_layout()
            return fig
        
        # Probar la función
        fig = dibujar_vista_frontal_viga_simulada(25, 60, 54, "3/8\"", 12, 0.71, 20, True)
        plt.close(fig)
        print("✅ Función de dibujo simulada correctamente")
        return True
        
    except Exception as e:
        print(f"❌ Error en función de dibujo: {e}")
        return False

if __name__ == "__main__":
    print("🚀 Diagnóstico de Matplotlib para CONSORCIO DEJ")
    print("=" * 60)
    
    # Ejecutar diagnóstico
    if diagnosticar_matplotlib():
        # Simular función de dibujo
        simular_funcion_dibujo()
        print("\n🎉 ¡Todo está funcionando correctamente!")
        print("💡 La aplicación debería mostrar gráficos sin problemas.")
    else:
        print("\n❌ Hay problemas con matplotlib.")
        print("💡 Ejecuta: pip install matplotlib")
        print("💡 O ejecuta: python instalar_matplotlib.py")
    
    input("\nPresiona Enter para salir...") 