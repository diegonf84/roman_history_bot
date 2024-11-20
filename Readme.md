# Roman History Bot

Bot de conversación especializado en Historia Romana utilizando MLX (Apple Silicon) y el modelo Mistral-7B-Instruct.

## 🚀 Características

- Respuestas en español sobre Historia Romana
- Optimizado para Apple Silicon (M1/M2/M3)
- Procesamiento local (no requiere API externa)
- Sistema de memoria para mantener contexto de conversación
- Modelo cuantizado de 4-bit para eficiencia en memoria

## 📋 Requisitos

- macOS con Apple Silicon (M1/M2/M3)
- Python 3.9+
- Poetry para gestión de dependencias
- Mínimo 16GB RAM recomendado

## 🛠 Instalación

1. Clonar el repositorio:
```bash
git clone <tu-repositorio>
cd roman_history_bot
```

2. Instalar dependencias con Poetry:
```bash
poetry install
```

3. Configurar variables de entorno:
```bash
# Crear archivo .env
HUGGINGFACE_TOKEN=tu_token_aquí
```

## 💻 Uso

1. Activar entorno virtual:
```bash
poetry shell
```

2. Ejecutar el bot interactivo:
```bash
poetry run python tests/test_interactive_memory.py
```

## 🤖 Comandos Disponibles

- `historia`: muestra el historial de conversación
- `salir`: termina la sesión

## 📦 Estructura del Proyecto

```
roman_history_bot/
├── pyproject.toml
├── poetry.lock
├── .env
├── roman_history_bot/
│   ├── bot/
│   │   ├── handlers.py
│   │   └── roman_bot.py
│   └── config/
│       └── settings.py
└── tests/
    └── test_interactive_memory.py
```

## 🔧 Configuración

El bot utiliza las siguientes configuraciones por defecto:
- Modelo: mlx-community/Mistral-7B-Instruct-v0.3-4bit
- Límite de memoria: 3 interacciones
- Formato de respuesta: Español, estilo académico

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de:
1. Hacer fork del proyecto
2. Crear una rama para tu feature
3. Hacer commit de tus cambios
4. Crear un Pull Request

## 📄 Licencia

[Tu licencia aquí]

## ✨ Agradecimientos

- MLX por el framework optimizado para Apple Silicon
- Comunidad MLX por la conversión y optimización del modelo Mistral
- Hugging Face por hosting del modelo