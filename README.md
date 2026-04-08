# LocalPDF 📄🚫☁️

**LocalPDF** is a simple, private Python tool for working with PDF files directly on your computer. It is designed for two common tasks: **extracting pages from a PDF** and **merging multiple PDFs into a single file**. Unlike online services such as *iLovePDF*, your documents never leave your machine, which helps protect the privacy of sensitive, personal, or legal files.

**LocalPDF** es una herramienta sencilla y privada desarrollada en Python para trabajar con archivos PDF directamente en tu computadora. Está pensada para dos tareas comunes: **extraer páginas de un PDF** y **unir varios PDFs en un solo archivo**. A diferencia de servicios en línea como *iLovePDF*, tus documentos nunca salen de tu máquina, lo que ayuda a proteger la privacidad de archivos sensibles, personales o legales.

---

## English

### ✨ Features

- **Page extraction:** Extract selected pages from a PDF using human-friendly inputs such as `1-5`, `1,3,10`, or mixed patterns like `2-4,7,9-11`.
- **PDF merging:** Combine multiple PDF files into a single document in the exact order you choose.
- **Interactive terminal workflow:** Run the script and follow simple prompts without needing a graphical interface.
- **Drag & drop support:** You can drag PDF files directly into the terminal instead of manually typing long file paths.
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

When you launch the program, you can choose between:

- **1) Extract pages from a PDF**
- **2) Merge multiple PDFs into one**

The script will then guide you step by step in the terminal.

### 📌 Extracting pages

If you choose extraction mode, you will:

- drag or paste the input PDF path,
- enter the pages you want to extract, or press `Enter` to keep all pages,
- choose an output filename,
- choose an output folder.

#### Example page inputs

- `1-5` → extracts pages 1 through 5
- `1,3,10` → extracts pages 1, 3, and 10
- `2-4,7,9-11` → extracts multiple ranges and individual pages

### 📎 Merging PDFs

If you choose merge mode, you will:

- drag the PDF files **one by one** into the terminal in the desired order,
- press `Enter` on an empty line when you are done,
- choose an output filename,
- choose an output folder.

#### Example merge workflow

```text
What do you want to do?
1) Extract pages from a PDF
2) Merge multiple PDFs
Choose [1/2]: 2

PDF #1: [drag first file here]
PDF #2: [drag second file here]
PDF #3: [drag third file here]
PDF #4: [press Enter if finished]
```

### 🔒 Privacy

LocalPDF is designed for fully local use. Your files are processed entirely on your computer, without being uploaded to external servers.

### 📜 License

MIT License

---

## Español

### ✨ Características

- **Extracción de páginas:** Extrae páginas seleccionadas de un PDF usando entradas amigables como `1-5`, `1,3,10` o combinaciones como `2-4,7,9-11`.
- **Unión de PDFs:** Combina varios archivos PDF en un solo documento en el orden exacto que elijas.
- **Flujo interactivo en terminal:** Ejecuta el script y sigue instrucciones simples sin necesidad de una interfaz gráfica.
- **Soporte para arrastrar y soltar:** Puedes arrastrar archivos PDF directamente a la terminal en lugar de escribir rutas largas manualmente.
- **Privacidad por diseño:** Todo funciona localmente en tu equipo.

### 🚀 Instalación rápida (Windows)

1. **Clona el repositorio**
   ```powershell
   git clone https://github.com/jrconstain/LocalPDF.git
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

Cuando inicies el programa, podrás elegir entre:

- **1) Extraer páginas de un PDF**
- **2) Unir varios PDFs en uno**

Luego el script te irá guiando paso a paso en la terminal.

### 📌 Extraer páginas

Si eliges el modo de extracción, podrás:

- arrastrar o pegar la ruta del PDF de entrada,
- escribir las páginas que quieres extraer, o presionar `Enter` para conservar todas,
- elegir el nombre del archivo de salida,
- elegir la carpeta de destino.

#### Ejemplos de entrada de páginas

- `1-5` → extrae de la página 1 a la 5
- `1,3,10` → extrae las páginas 1, 3 y 10
- `2-4,7,9-11` → extrae múltiples rangos y páginas individuales

### 📎 Unir PDFs

Si eliges el modo de unión, podrás:

- arrastrar los archivos PDF **uno por uno** a la terminal en el orden deseado,
- presionar `Enter` en una línea vacía cuando hayas terminado,
- elegir el nombre del archivo de salida,
- elegir la carpeta de destino.

#### Ejemplo de flujo para unir PDFs

```text
¿Qué quieres hacer?
1) Extraer páginas de un PDF
2) Unir varios PDFs
Elige [1/2]: 2

PDF #1: [arrastra aquí el primer archivo]
PDF #2: [arrastra aquí el segundo archivo]
PDF #3: [arrastra aquí el tercer archivo]
PDF #4: [presiona Enter si terminaste]
```

### 🔒 Privacidad

LocalPDF está diseñado para uso completamente local. Tus archivos se procesan enteramente en tu computadora, sin subirse a servidores externos.

### 📜 Licencia

Licencia MIT