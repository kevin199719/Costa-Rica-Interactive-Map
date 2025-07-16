# 🗺️ Costa Rica Interactive Map

Este proyecto es un mapa interactivo de Costa Rica que muestra la ubicación de volcanes, aeropuertos y aeródromos. Fue desarrollado con [Folium](https://python-visualization.github.io/folium/) y datos estructurados en JSON. El mapa detecta automáticamente el idioma del sistema y muestra la información en inglés o español.

---

## 🌍 Descripción

Visualización de:
- 🌋 Volcanes activos de Costa Rica
- ✈️ Aeropuertos internacionales y regionales
- 🛩️ Aeródromos públicos y privados

El mapa permite alternar capas (LayerControl) y visualizar información adicional mediante popups con enlaces oficiales.

---

## 📁 Estructura del Proyecto
```bash
Costa-Rica-Interactive-Map/
│
├── data/
│   ├── data.json                
│
├── icons/
│   ├── volcan_icon.png      
│   └── airport.png           
│
├── output/
│   └── map.html              
│
├── LICENSE
├── mapping.py              
└── README.md  
```
## ⚙️ Requisitos

- Python 3.7+
- Recomendado usar un entorno virtual

Instalar dependencias:

```bash
pip install folium
```
Cómo ejecutar: 
- Abre la terminal en tu proyecto
- Ejecuta "python mapping.py"

El archivo map.html se generará en la carpeta output/. Abrilo en tu navegador para visualizar el mapa interactivo.

## 🌐 Internationalization
a aplicación detecta automáticamente el idioma del sistema y muestra la información en:

🇪🇸 Español

🇬🇧 Inglés

Si la configuración regional de tu sistema comienza con es, se mostrará el contenido en español. En cualquier otro caso, se mostrará en inglés por defecto.

## 📚 Fuentes de datos
Sistema Nacional de Áreas de Conservación: https://www.sinac.go.cr

Wikipedia (para algunos volcanes)

Datos obtenidos manualmente y mediante geolocalización de códigos Plus/Google Maps

## 🤝 Contribuciones
¡Toda ayuda es bienvenida! Puedes:

Agregar nuevos volcanes o aeropuertos

Corregir coordenadas o nombres

Mejorar el estilo visual del mapa

## 🧑‍💻 Autor
Desarrollado por Kevin Arce

## 📄 Licencia
Este proyecto está bajo la licencia MIT.









