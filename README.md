# LocalPDF 📄🚫☁️

**LocalPDF** is a simple, private Python tool for manipulating PDF files directly on your computer. Unlike online services such as *iLovePDF*, your documents never leave your machine, which helps protect the privacy of sensitive, personal, or legal files.

**LocalPDF** es una herramienta sencilla y privada desarrollada en Python para manipular archivos PDF directamente en tu computadora. A diferencia de servicios en línea como *iLovePDF*, tus documentos nunca salen de tu máquina, lo que ayuda a proteger la privacidad de archivos sensibles, personales o legales.

---

## English

### ✨ Features

- **Page extraction:** Select page ranges such as `1-5` or individual pages such as `1, 3, 10`.
- **Human-friendly indexing:** Pages start at `1`, just like in a PDF reader.
- **Smart path handling:** Supports drag and drop paths from the terminal, including PowerShell-formatted paths.
- **Automatic fallbacks:** If you do not provide an output name or folder, the script suggests smart defaults based on the original file.
- **Private by design:** Everything runs locally on your machine.

### 🚀 Quick Setup (Windows)

1. **Clone the repository**
   ```powershell
   git clone https://github.com/jrconstain/LocalPDF.git
   cd LocalPDF
   ```

2. **Create and activate a virtual environment**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

### 🛠️ Usage

Run the script interactively:

```powershell
python mpdf.py
```

Then follow the prompts in the terminal to:

- choose the input PDF,
- define the pages you want to extract,
- set the output name and location, or use the suggested defaults.

### 📌 Example page inputs

- `1-5` → extracts pages 1 through 5
- `1,3,10` → extracts pages 1, 3, and 10
- `2-4,7,9-11` → extracts multiple ranges and individual pages

### 🔒 Privacy

LocalPDF is designed for local use only. Your files are processed entirely on your computer, without uploading them to external servers.

### 📜 License

MIT License

---

## Español

### ✨ Características

- **Extracción de páginas:** Selecciona rangos como `1-5` o páginas individuales como `1, 3, 10`.
- **Interfaz pensada para humanos:** Las páginas empiezan en `1`, tal como las ves en tu lector de PDF.
- **Manejo inteligente de rutas:** Soporta rutas copiadas o arrastradas desde la terminal, incluyendo formatos complejos de PowerShell.
- **Fallbacks automáticos:** Si no especificas nombre o carpeta de salida, el script sugiere opciones inteligentes basadas en el archivo original.
- **Privacidad por diseño:** Todo funciona localmente en tu equipo.

### 🚀 Instalación rápida (Windows)

1. **Clona el repositorio**
   ```powershell
   git clone https://github.com/YOUR_USER/LocalPDF.git
   cd LocalPDF
   ```

2. **Crea y activa un entorno virtual**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```

3. **Instala las dependencias**
   ```powershell
   pip install -r requirements.txt
   ```

### 🛠️ Uso

Ejecuta el script de forma interactiva:

```powershell
python mpdf.py
```

Luego sigue las instrucciones en la terminal para:

- elegir el PDF de entrada,
- definir las páginas que quieres extraer,
- indicar el nombre y la ubicación de salida, o usar las opciones sugeridas.

### 📌 Ejemplos de entrada de páginas

- `1-5` → extrae de la página 1 a la 5
- `1,3,10` → extrae las páginas 1, 3 y 10
- `2-4,7,9-11` → extrae múltiples rangos y páginas individuales

### 🔒 Privacidad

LocalPDF está diseñado para uso completamente local. Tus archivos se procesan enteramente en tu computadora, sin subirse a servidores externos.

### 📜 Licencia

Licencia MIT
