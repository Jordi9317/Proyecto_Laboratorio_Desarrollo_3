# 🖼️ Restauración Facial Rápida con GFPGAN

Aplicación web local para restaurar y mejorar rostros en imágenes degradadas usando modelos de IA. Combina restauración facial con GFPGAN para un procesamiento rápido y eficiente.

## ✨ Características

- **Restauración Facial**: Mejora automática de rostros usando GFPGAN
- **Interfaz Web**: Streamlit intuitiva y responsive
- **Procesamiento Local**: Todo se ejecuta en tu máquina
- **Comparación Visual**: Vista paralela de imagen original y restaurada
- **Datos de Comparación**: Dimensiones y tamaño de archivos
- **Descarga**: Exportación de imágenes procesadas en PNG
- **Rápido**: Optimizado para CPU, procesamiento en segundos

## 🚀 Instalación Rápida

### 1. Clonar o descargar el proyecto

```bash
cd c:\Proyecto\Laboratorio 3.0
```

### 2. Crear y activar entorno virtual

```cmd
# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar aplicación

```bash
streamlit run app.py
```

¡La aplicación se abrirá en `http://localhost:8501`!

## 📋 Requisitos del Sistema

### Mínimos
- **Python**: 3.8+
- **RAM**: 4GB
- **Almacenamiento**: 2GB libres (para modelo)

### Recomendados
- **Python**: 3.9+
- **RAM**: 8GB
- **Almacenamiento**: 5GB libres

## 🎯 Uso de la Aplicación

### 1. Carga de Imágenes
- Arrastra y suelta imágenes o haz clic para seleccionar
- Formatos soportados: JPG, PNG, JPEG
- Tamaño máximo recomendado: 2048px lado

### 2. Procesamiento
- Haz clic en "Restaurar Rostros"
- Espera el procesamiento (5-15 segundos)
- Visualiza comparación paralela

### 3. Comparación
- Imagen original vs restaurada lado a lado
- Datos: Dimensiones (ancho x alto), Tamaño en bytes

### 4. Exportación
- Descarga la imagen restaurada en PNG
- Mantiene calidad alta

## 🏗️ Arquitectura

```
image_restoration_app/
├── app.py                 # Interfaz principal Streamlit
├── requirements.txt       # Dependencias Python
├── README.md              # Documentación
└── venv/                  # Entorno virtual (creado por usuario)
```

## 🔧 Configuración

### Variables de Entorno (opcional)

```bash
# Para personalizar, crear .env
MODEL_URL=https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth
```

### Optimizaciones de Rendimiento

- Modelo GFPGAN sin upscale para mayor rapidez
- Procesamiento en CPU
- Caché del modelo para sesiones múltiples

## 🧪 Testing

### Ejecutar Localmente
```bash
# Activar entorno
venv\Scripts\activate

# Ejecutar
streamlit run app.py
```

### Verificar Instalación
```bash
venv\Scripts\activate && pip list | findstr gfpgan
```

## 📊 Rendimiento

### Tiempos Aproximados (CPU i5/i7)

| Operación | Tiempo | Memoria |
|-----------|--------|---------|
| Carga Modelo | 10-20s (primera vez) | ~500MB |
| Restauración Facial | 5-15s | ~1-2GB |

## 🐛 Solución de Problemas

### Problema: "ModuleNotFoundError: No module named 'gfpgan'"
```bash
# Asegurar entorno activado
venv\Scripts\activate

# Reinstalar
pip install gfpgan
```

### Problema: Modelo no descarga
```bash
# Verificar conexión a internet
# Intentar con VPN si es necesario
```

### Problema: Aplicación no inicia
```bash
# Verificar puerto 8501 libre
streamlit run app.py --server.port 8502
```

## 🤝 Contribución

### Desarrollo Local
```bash
# Instalar dependencias de desarrollo (si aplica)
pip install streamlit --upgrade
```

### Mejoras Sugeridas
- Soporte para GPU
- Batch processing
- Más formatos de salida

## 📄 Licencias

### Código
- **MIT License**: Código fuente de la aplicación

### Modelos
- **GFPGAN**: MIT License

**Importante**: Revisar términos de uso para aplicaciones comerciales.

## 🙏 Agradecimientos

- **GFPGAN**: Para restauración facial de alta calidad
- **Streamlit**: Por el framework web
- **PyTorch**: Por el backend de IA

---

**⭐ Si te gusta el proyecto, ¡dale una estrella en GitHub!**

*Creado con ❤️ para la comunidad de procesamiento de imágenes*