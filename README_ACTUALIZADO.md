# 🏗️ CONSORCIO DEJ - Análisis Estructural Avanzado

## 📋 Descripción

Aplicación web completa para análisis estructural con diseño de elementos de concreto armado, gráficos interactivos, y funcionalidades PWA. Basada en las normas ACI 318, Norma E.060 y metodologías de Arthur H. Nilson y Jack C. McCormac.

## ✨ Nuevas Funcionalidades Agregadas

### 🔧 Diseño de Zapatas (Cimentaciones)
- **Cálculos completos** según ACI 318 y Norma E.060
- **Verificaciones de punzonamiento y flexión**
- **Gráficos de cortantes y momentos** según McCormac
- **Dibujo automático de la zapata** con dimensiones y refuerzo
- **Análisis de capacidad portante del suelo**

### 🔧 Diseño de Vigas
- **Diseño por flexión y corte** con verificaciones completas
- **Cálculo de área de acero** y espaciamiento de estribos
- **Diagramas de cortantes y momentos** según McCormac
- **Dibujo de la viga** con acero longitudinal y estribos
- **Verificaciones de cuantías** mínimas y máximas

### 🏢 Diseño de Columnas
- **Diseño por compresión y flexión** combinada
- **Cálculo de acero longitudinal** y estribos
- **Diagramas de cortantes y momentos** para columnas
- **Dibujo de la columna** con distribución de acero
- **Verificaciones de esbeltez** y capacidad

### ✂️ Ejercicio Básico de Corte
- **Cálculos de corte** según fórmulas del PDF
- **Verificación de zonas críticas**
- **Espaciamiento de estribos** automático
- **Diagramas de cortantes y momentos** según McCormac
- **Dibujo del elemento** con refuerzo de corte

## 📊 Gráficos y Visualizaciones

### Diagramas de Cortantes y Momentos (McCormac)
- **Vigas simplemente apoyadas**
- **Vigas empotradas**
- **Vigas continuas**
- **Cargas distribuidas y puntuales**
- **Valores máximos** de cortantes y momentos

### Dibujos de Elementos Estructurales
- **Vigas** con acero longitudinal y estribos
- **Columnas** con distribución de acero
- **Zapatas** con dimensiones y refuerzo
- **Escalas automáticas** para visualización
- **Anotaciones** con propiedades del material

### Gráficos Interactivos (Plotly)
- **Barras comparativas** de propiedades
- **Gráficos de pastel** para verificaciones
- **Comparaciones** con valores típicos
- **Análisis de factores de seguridad**

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación Automática
```bash
# Opción 1: Script automático
python instalar_dependencias.py

# Opción 2: Requirements.txt
pip install -r requirements.txt
```

### Dependencias Principales
- **Streamlit** >= 1.28.0 - Framework web
- **NumPy** >= 1.24.0 - Cálculos numéricos
- **Pandas** >= 2.0.0 - Manipulación de datos
- **Matplotlib** >= 3.7.0 - Gráficos básicos
- **Plotly** >= 5.15.0 - Gráficos interactivos
- **ReportLab** >= 4.0.0 - Generación de PDFs
- **Stripe** >= 6.0.0 - Sistema de pagos

## 🎯 Ejecución de la Aplicación

### Ejecución Básica
```bash
streamlit run APP2.py
```

### Ejecución con Configuración Específica
```bash
# Puerto personalizado
streamlit run APP2.py --server.port 8501

# Configuración de desarrollo
streamlit run APP2.py --server.headless true
```

## 📱 Funcionalidades PWA

### Características PWA
- **Instalación como app** en dispositivos móviles
- **Funcionamiento offline** con cache
- **Iconos personalizados** para la aplicación
- **Manifest.json** para configuración
- **Service Worker** para funcionalidad offline

### Generación de PWA
```bash
python generar_pwa.py
```

## 💳 Sistema de Planes

### Plan Gratuito
- ✅ Cálculos básicos
- ✅ Resultados simples
- ✅ Gráficos básicos
- ⚠️ Funciones limitadas

### Plan Premium
- ✅ Diseño completo de elementos
- ✅ Verificaciones detalladas
- ✅ Gráficos interactivos
- ✅ Generación de PDFs
- ✅ Dibujos de elementos
- ✅ Diagramas de cortantes y momentos

## 📚 Metodologías Implementadas

### Arthur H. Nilson
- **Diseño de Estructuras de Concreto**
- **Cálculos de cortantes y momentos**
- **Verificaciones de capacidad**

### Jack C. McCormac
- **Diseño de Concreto Reforzado**
- **Diagramas de cortantes y momentos**
- **Metodologías de diseño**

### Normas Técnicas
- **ACI 318** - Código de Construcción
- **Norma E.060** - Concreto Armado
- **Normas peruanas** de diseño sísmico

## 🔧 Funciones Técnicas

### Cálculos Estructurales
- **Predimensionamiento** de elementos
- **Diseño por flexión** y corte
- **Verificaciones de capacidad**
- **Análisis sísmico** básico
- **Cálculo de propiedades** de materiales

### Verificaciones
- **Cuantías mínimas** y máximas
- **Esfuerzos permisibles**
- **Factores de seguridad**
- **Longitudes de desarrollo**
- **Espaciamientos mínimos**

## 📊 Reportes y Exportación

### Generación de PDFs
- **Reportes técnicos** completos
- **Gráficos incluidos** en PDF
- **Tablas de resultados**
- **Especificaciones** de diseño

### Exportación de Datos
- **Excel** (.xlsx)
- **CSV** para análisis
- **JSON** para integración

## 🛠️ Solución de Problemas

### Errores Comunes
1. **ModuleNotFoundError**: Ejecutar `python instalar_dependencias.py`
2. **Puerto ocupado**: Usar `--server.port 8502`
3. **Gráficos no aparecen**: Verificar instalación de matplotlib/plotly

### Verificación de Instalación
```bash
python VERIFICAR_SOLUCION.py
```

## 📞 Soporte y Contacto

### Información del Proyecto
- **Desarrollador**: CONSORCIO DEJ
- **Versión**: 2.0 (Actualizada)
- **Fecha**: 2024
- **Licencia**: Uso educativo y profesional

### Características Técnicas
- **Framework**: Streamlit
- **Lenguaje**: Python 3.8+
- **Base de datos**: Sesiones locales
- **Autenticación**: Sistema propio
- **Pagos**: Integración Stripe

## 🎉 Novedades de la Versión 2.0

### Nuevas Secciones
- ✅ Diseño de Zapatas completo
- ✅ Diseño de Vigas detallado
- ✅ Diseño de Columnas avanzado
- ✅ Ejercicio Básico de Corte
- ✅ Diagramas de Cortantes y Momentos (McCormac)
- ✅ Dibujos automáticos de elementos
- ✅ Gráficos interactivos mejorados

### Mejoras Técnicas
- ✅ Manejo robusto de dependencias
- ✅ Verificaciones de disponibilidad
- ✅ Gráficos con fallback
- ✅ Código optimizado
- ✅ Documentación completa

---

**¡Disfruta usando CONSORCIO DEJ para tus análisis estructurales! 🏗️✨** 