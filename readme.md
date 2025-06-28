# 🧠 Sistema de Predicción de Contratación con IA

Este proyecto utiliza un modelo de clasificación basado en RandomForest para predecir si un candidato será contratado, considerando variables como edad, experiencia, género, nivel educativo, idiomas y certificaciones.

## ⚙️ Requisitos

- Python 3.8 o superior
- pip

## 🐍 Configuración del entorno virtual (recomendado)

Para evitar conflictos y mantener el entorno limpio:

```bash
    # Crear entorno virtual
    python -m venv venv

    # Activar entorno virtual
    # En Windows:
    venv\Scripts\activate
    # En Linux/Mac:
    source venv/bin/activate

    # Instalar dependencias
    pip install -r requirements.txt

```
# Generar Modelo
```bash
    python modelo.py

```

# Ejecutar la interfaz gráfica
```bash
    python app.py

```

# Generar Gráfico de importancia de Características
```bash
    python importancia.py

```

## 📁 Estructura del proyecto una vez ejecutado venv y generado el modelo
```bash
    .
    ├── app.py                 # Interfaz gráfica Tkinter
    ├── importancia.py         # Gráfico de peso de características
    ├── modelo.py              # Entrenamiento del modelo
    ├── modelo.pkl             # Modelo entrenado (generado)
    ├── requirements.txt       # Dependencias
    ├── .gitignore             # Archivos a excluir del control de versiones
    └── README.md              # Este archivo

```