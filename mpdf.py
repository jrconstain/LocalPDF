import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter
import re

def clean_path(path_str):
    """Limpia basura de PowerShell como el '&' y comillas extras"""
    return path_str.strip().lstrip('&').strip().strip("'").strip('"')

def parse_paths(raw_paths):
    """
    Soporta varios formatos típicos al arrastrar múltiples PDFs en PowerShell, por ejemplo:
    & 'C:\\a.pdf'& 'C:\\b.pdf'
    "C:\\a.pdf", "C:\\b.pdf"
    'C:\\a.pdf', 'C:\\b.pdf'
    """
    raw_paths = raw_paths.strip()

    # 1) Intentar extraer todas las rutas entre comillas simples o dobles
    quoted_paths = re.findall(r"'([^']+\.pdf)'|\"([^\"]+\.pdf)\"", raw_paths, flags=re.IGNORECASE)
    paths = [Path(p1 or p2) for p1, p2 in quoted_paths if (p1 or p2)]

    if paths:
        return paths

    # 2) Fallback: separar por comas
    parts = [p.strip() for p in raw_paths.split(",") if p.strip()]
    return [Path(clean_path(p)) for p in parts]

def parse_range(range_str):
    """Convierte '1-3, 5' (entrada humana) en [0, 1, 2, 4] (índice Python)"""
    pages = set()
    for part in range_str.split(','):
        part = part.strip()
        if not part: continue
        
        if '-' in part:
            start, end = map(int, part.split('-'))
            # Restamos 1 al inicio y mantenemos el fin para el range() de Python
            # range(1-1, 3) -> range(0, 3) -> genera 0, 1, 2
            pages.update(range(start - 1, end))
        else:
            pages.add(int(part) - 1)
    return sorted(list(pages))

def collect_pdf_paths():
    """Pide PDFs uno por uno hasta que el usuario dé Enter vacío"""
    pdf_paths = []

    print("\n📚 Arrastra los PDFs UNO POR UNO en el orden deseado.")
    print("↩️ Cuando termines, simplemente presiona Enter en blanco.\n")

    while True:
        raw = input(f"PDF #{len(pdf_paths) + 1}: ").strip()

        if not raw:
            break

        pdf_path = Path(clean_path(raw))

        if not pdf_path.exists():
            print(f"❌ No existe: {pdf_path}")
            continue

        if pdf_path.suffix.lower() != ".pdf":
            print(f"❌ No es un PDF: {pdf_path}")
            continue

        pdf_paths.append(pdf_path)
        print(f"✅ Añadido: {pdf_path.name}")

    return pdf_paths

def merge_pdfs(input_paths, output_path):
    """Une varios PDFs en el orden dado y guarda un solo archivo"""
    writer = PdfWriter()

    for pdf_path in input_paths:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"\n✅ ¡Merge listo! Guardado en: {output_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Ruta al PDF")
    parser.add_argument("-p", "--pages", help="Páginas (ej: 1-3,5)")
    args = parser.parse_args()

    mode = input(
        "¿Qué quieres hacer?\n"
        "1) Extraer páginas de un PDF\n"
        "2) Unir varios PDFs\n"
        "Elige [1/2]: "
    ).strip() or "1"

    if mode == "2":
        input_paths = collect_pdf_paths()

        if len(input_paths) < 2:
            print("❌ Debes añadir al menos 2 PDFs para hacer merge.")
            return

        print("\n📑 Orden final del merge:")
        for i, p in enumerate(input_paths, start=1):
            print(f"   {i}. {p.name}")

        default_name = f"MERGED_{input_paths[0].stem}.pdf"
        user_output = input(f"\n💾 Nombre del archivo [{default_name}]: ").strip()
        final_name = user_output if user_output else default_name
        if not final_name.endswith(".pdf"):
            final_name += ".pdf"

        default_folder = input_paths[0].parent
        user_folder = input(f"📂 Carpeta de destino [{default_folder}]: ").strip()
        final_folder = Path(clean_path(user_folder)) if user_folder else default_folder

        final_output_path = final_folder / final_name
        merge_pdfs(input_paths, final_output_path)
        return

    # 1. Obtener Archivo de Entrada
    raw_input = args.input or input("📄 Arrastra el PDF aquí: ")
    input_path = Path(clean_path(raw_input))

    if not input_path.exists():
        print(f"❌ No existe: {input_path}")
        return

    # 2. Obtener Páginas
    pages_raw = args.pages or input("🔢 Páginas (ej: 0-2, 5) [Enter para todas]: ")
    
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    
    if not pages_raw.strip():
        page_list = list(range(total_pages))
    else:
        page_list = parse_range(pages_raw)

    # 3. Preguntar NOMBRE y DESTINO con Fallbacks
    default_name = f"RECORTADO_{input_path.name}"
    user_output = input(f"💾 Nombre del archivo [{default_name}]: ").strip()
    
    # Si dio Enter, usamos el nombre por defecto
    final_name = user_output if user_output else default_name
    if not final_name.endswith(".pdf"):
        final_name += ".pdf"

    default_folder = input_path.parent
    user_folder = input(f"📂 Carpeta de destino [{default_folder}]: ").strip()
    
    # Si dio Enter, usamos la carpeta original. Si no, limpiamos la ruta que pegue.
    final_folder = Path(clean_path(user_folder)) if user_folder else default_folder

    # Ruta final completa
    final_output_path = final_folder / final_name

    # 4. Procesar y Guardar
    writer = PdfWriter()
    for p in page_list:
        if 0 <= p < total_pages:
            writer.add_page(reader.pages[p])
            
    with open(final_output_path, "wb") as f:
        writer.write(f)
    
    print(f"\n✅ ¡Listo! Guardado en: {final_output_path}")

if __name__ == "__main__":
    main()