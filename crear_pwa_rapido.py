#!/usr/bin/env python3
"""
Script Rápido para Crear PWA - CONSORCIO DEJ
Versión simplificada sin dependencias externas
"""

import os
import base64

def crear_icono_simple(tamaño):
    """Crear icono simple en formato SVG"""
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{tamaño}" height="{tamaño}" viewBox="0 0 {tamaño} {tamaño}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{tamaño}" height="{tamaño}" fill="#FFD700"/>
  <rect x="{tamaño//20}" y="{tamaño//20}" width="{tamaño*9//10}" height="{tamaño*9//10}" 
        fill="none" stroke="#FFA500" stroke-width="{tamaño//20}"/>
  <text x="{tamaño//2}" y="{tamaño//2}" font-family="Arial, sans-serif" 
        font-size="{tamaño//4}" font-weight="bold" text-anchor="middle" 
        dominant-baseline="middle" fill="#333">DEJ</text>
</svg>'''
    return svg_content

def generar_iconos_svg():
    """Generar iconos SVG para la PWA"""
    tamaños = [72, 96, 128, 144, 152, 192, 384, 512]
    
    # Crear directorio de iconos si no existe
    if not os.path.exists('icons'):
        os.makedirs('icons')
    
    print("🎨 Generando iconos SVG para la PWA...")
    
    for tamaño in tamaños:
        svg_content = crear_icono_simple(tamaño)
        nombre_archivo = f"icons/icon-{tamaño}x{tamaño}.svg"
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✅ Icono {tamaño}x{tamaño} generado")
    
    print("🎉 Todos los iconos SVG generados correctamente")

def crear_manifest_simple():
    """Crear manifest.json simplificado"""
    manifest = {
        "name": "CONSORCIO DEJ - Análisis Estructural",
        "short_name": "CONSORCIO DEJ",
        "description": "Aplicación profesional de análisis estructural",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#FFD700",
        "theme_color": "#FFD700",
        "orientation": "portrait-primary",
        "scope": "/",
        "lang": "es",
        "icons": [
            {
                "src": "icons/icon-72x72.svg",
                "sizes": "72x72",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-96x96.svg",
                "sizes": "96x96",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-128x128.svg",
                "sizes": "128x128",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-144x144.svg",
                "sizes": "144x144",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-152x152.svg",
                "sizes": "152x152",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-192x192.svg",
                "sizes": "192x192",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-384x384.svg",
                "sizes": "384x384",
                "type": "image/svg+xml",
                "purpose": "any"
            },
            {
                "src": "icons/icon-512x512.svg",
                "sizes": "512x512",
                "type": "image/svg+xml",
                "purpose": "any"
            }
        ]
    }
    
    import json
    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print("✅ Manifest.json creado")

def crear_service_worker_simple():
    """Crear Service Worker simplificado"""
    sw_content = '''// Service Worker Simplificado - CONSORCIO DEJ
const CACHE_NAME = 'consorcio-dej-v1.0.0';

// Instalación
self.addEventListener('install', event => {
  console.log('🔄 Instalando PWA...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('✅ Cache abierto');
        return cache.addAll([
          '/',
          '/manifest.json',
          '/offline.html'
        ]);
      })
      .then(() => self.skipWaiting())
  );
});

// Activación
self.addEventListener('activate', event => {
  console.log('🚀 Activando PWA...');
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            return caches.delete(cacheName);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Interceptar peticiones
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          return response;
        }
        return fetch(event.request)
          .then(response => {
            if (!response || response.status !== 200) {
              return response;
            }
            const responseToCache = response.clone();
            caches.open(CACHE_NAME)
              .then(cache => cache.put(event.request, responseToCache));
            return response;
          })
          .catch(() => {
            if (event.request.headers.get('accept').includes('text/html')) {
              return caches.match('/offline.html');
            }
          });
      })
  );
});

// Notificaciones push
self.addEventListener('push', event => {
  const options = {
    body: 'Nueva actualización disponible en CONSORCIO DEJ',
    icon: '/icons/icon-192x192.svg',
    badge: '/icons/icon-72x72.svg',
    vibrate: [100, 50, 100]
  };
  
  event.waitUntil(
    self.registration.showNotification('CONSORCIO DEJ', options)
  );
});
'''
    
    with open('sw.js', 'w', encoding='utf-8') as f:
        f.write(sw_content)
    
    print("✅ Service Worker creado")

def crear_pagina_offline_simple():
    """Crear página offline simplificada"""
    offline_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CONSORCIO DEJ - Sin Conexión</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            max-width: 400px;
        }
        .icon { font-size: 60px; margin-bottom: 20px; }
        h1 { color: #333; margin-bottom: 15px; }
        p { color: #666; margin-bottom: 20px; }
        button {
            background: #FFD700;
            color: #333;
            border: none;
            padding: 15px 30px;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover { background: #FFA500; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">📡</div>
        <h1>Sin Conexión</h1>
        <p>No tienes conexión a internet. Algunas funciones pueden no estar disponibles.</p>
        <button onclick="window.location.reload()">🔄 Reintentar</button>
        <p style="margin-top: 30px; font-size: 14px; color: #999;">
            <strong>CONSORCIO DEJ</strong><br>
            Análisis Estructural<br>
            Versión 1.0.0
        </p>
    </div>
    <script>
        window.addEventListener('online', () => window.location.reload());
        setInterval(() => {
            if (navigator.onLine) window.location.reload();
        }, 5000);
    </script>
</body>
</html>'''
    
    with open('offline.html', 'w', encoding='utf-8') as f:
        f.write(offline_html)
    
    print("✅ Página offline creada")

def crear_integración_streamlit():
    """Crear integración simple con Streamlit"""
    integracion = """# Integración PWA con Streamlit - CONSORCIO DEJ
import streamlit as st

def configurar_pwa_streamlit():
    """Configurar PWA en Streamlit"""
    
    # Agregar meta tags y manifest
    st.markdown('''
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="theme-color" content="#FFD700">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="default">
        <link rel="manifest" href="/manifest.json">
        <link rel="apple-touch-icon" href="/icons/icon-192x192.svg">
    </head>
    ''', unsafe_allow_html=True)
    
    # Script de instalación PWA
    st.markdown('''
    <script>
        // Registrar Service Worker
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js')
                .then(registration => console.log('✅ PWA registrada'))
                .catch(error => console.log('❌ Error PWA:', error));
        }
        
        // Detectar instalación
        let deferredPrompt;
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            
            // Mostrar botón de instalación
            const installBtn = document.createElement('button');
            installBtn.innerHTML = '📱 Instalar App';
            installBtn.style.cssText = 'position: fixed; top: 20px; right: 20px; background: #FFD700; color: #333; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer; z-index: 1000; font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.2);';
            
            installBtn.onclick = async () => {
                if (deferredPrompt) {
                    deferredPrompt.prompt();
                    const { outcome } = await deferredPrompt.userChoice;
                    console.log('Usuario eligió:', outcome);
                    deferredPrompt = null;
                    installBtn.remove();
                }
            };
            
            document.body.appendChild(installBtn);
        });
        
        // Detectar si está instalada
        window.addEventListener('appinstalled', () => {
            console.log('🎉 PWA instalada correctamente');
        });
    </script>
    ''', unsafe_allow_html=True)

def mostrar_estado_pwa():
    """Mostrar estado de la PWA en el sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.subheader("📱 Estado PWA")
    
    import os
    archivos_pwa = ['manifest.json', 'sw.js', 'offline.html']
    archivos_ok = sum(1 for archivo in archivos_pwa if os.path.exists(archivo))
    
    if archivos_ok == len(archivos_pwa):
        st.sidebar.success("✅ PWA configurada")
    else:
        st.sidebar.warning(f"⚠️ {len(archivos_pwa) - archivos_ok} archivos faltantes")
    
    if os.path.exists('icons'):
        iconos = len([f for f in os.listdir('icons') if f.endswith('.svg')])
        st.sidebar.info(f"🎨 {iconos} iconos generados")
    else:
        st.sidebar.error("❌ Iconos no encontrados")

# Uso en tu app principal:
# configurar_pwa_streamlit()
# mostrar_estado_pwa()
"""
    
    with open('pwa_streamlit_simple.py', 'w', encoding='utf-8') as f:
        f.write(integracion)
    
    print("✅ Integración Streamlit creada")

def crear_instrucciones():
    """Crear archivo de instrucciones"""
    instrucciones = '''# 🚀 PWA RÁPIDA - CONSORCIO DEJ

## 📋 Archivos Creados:
- ✅ manifest.json (configuración PWA)
- ✅ sw.js (Service Worker)
- ✅ offline.html (página sin conexión)
- ✅ icons/ (iconos SVG)
- ✅ pwa_streamlit_simple.py (integración)

## 🔧 Cómo Usar:

### 1. Integrar con Streamlit:
```python
# En tu APP2.py, agrega al inicio:
from pwa_streamlit_simple import configurar_pwa_streamlit, mostrar_estado_pwa

# En la función main():
configurar_pwa_streamlit()
mostrar_estado_pwa()
```

### 2. Subir a servidor:
- Copia todos los archivos a tu servidor web
- Asegúrate de que esté en HTTPS
- Los archivos deben estar en la raíz del sitio

### 3. Probar PWA:
- Abre Chrome DevTools (F12)
- Ve a Application > Manifest
- Verifica que todo esté configurado
- Busca el botón "Install" en la barra de direcciones

## 📱 Características:
- ✅ Instalable como app nativa
- ✅ Funciona offline
- ✅ Iconos personalizados
- ✅ Notificaciones push
- ✅ Carga rápida con cache

## 🎯 Próximos Pasos:
1. Personaliza los colores en manifest.json
2. Agrega tu logo en los iconos
3. Configura notificaciones push
4. Optimiza el cache para tu app

¡Tu PWA está lista para usar! 🎉
'''
    
    with open('INSTRUCCIONES_PWA.md', 'w', encoding='utf-8') as f:
        f.write(instrucciones)
    
    print("✅ Instrucciones creadas")

def main():
    """Función principal"""
    print("=" * 60)
    print("   PWA RÁPIDA - CONSORCIO DEJ")
    print("=" * 60)
    print()
    
    # Generar todos los archivos
    generar_iconos_svg()
    print()
    
    crear_manifest_simple()
    print()
    
    crear_service_worker_simple()
    print()
    
    crear_pagina_offline_simple()
    print()
    
    crear_integración_streamlit()
    print()
    
    crear_instrucciones()
    print()
    
    print("=" * 60)
    print("   🎉 PWA CREADA EXITOSAMENTE")
    print("=" * 60)
    print()
    print("📁 Archivos generados:")
    print("   ✅ manifest.json")
    print("   ✅ sw.js")
    print("   ✅ offline.html")
    print("   ✅ icons/ (8 iconos SVG)")
    print("   ✅ pwa_streamlit_simple.py")
    print("   ✅ INSTRUCCIONES_PWA.md")
    print()
    print("🚀 Para usar:")
    print("   1. Lee INSTRUCCIONES_PWA.md")
    print("   2. Integra con tu APP2.py")
    print("   3. Sube a un servidor HTTPS")
    print()
    print("📱 Los usuarios podrán instalar tu app como nativa!")
    print()
    print("🎯 ¡PWA lista en menos de 5 minutos!")

if __name__ == "__main__":
    main() 