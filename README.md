# Script de Python para obtener el ID de un grupo de Telegram

Este repositorio contiene un script en Python llamado `get_group_id.py` que permite obtener el ID de un grupo específico en Telegram. A continuación, se detallan los pasos necesarios para configurar y ejecutar este script.

## Requisitos

Asegúrate de tener instalados los siguientes componentes:

- **Python 3.x**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- **Bibliotecas adicionales**: El script requiere la biblioteca `requests`.

## Pasos de Configuración

### 1. Crear el Bot
- Habla con [@BotFather](https://telegram.me/BotFather) en Telegram para crear un nuevo bot.
- Guarda el token que te proporciona BotFather.

### 2. Configurar el Bot
- Asegúrate de que el bot tenga habilitada la opción de unirse a grupos.
- Configura los permisos del bot para que pueda leer mensajes de grupo.

### 3. Añadir el Bot al Grupo
- Invita al bot al grupo donde quieres obtener el ID.
- Dale permisos de administrador al bot en el grupo.

### 4. Generar Actividad
- Envía algunos mensajes en el grupo después de añadir el bot.

### 5. Preparar el Script
- Asegúrate de tener Python instalado en tu sistema.
- Instala la librería 'requests':
   ```bash
   pip3 install requests
   ```
- Copia el código del script en un archivo `.py`.
- Reemplaza `'YOUR_BOT_TOKEN'` en el script con el token real de tu bot.

## Instalación

**Clone the repository**:
   ```bash
   git clone https://github.com/Hector711/get-telegram-group-id.git
   cd your-repository+
   ```
