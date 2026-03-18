import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter

def clean_path(path_str):
    """Limpia basura de PowerShell como el '&' y comillas extras"""
    return path_str.strip().lstrip('&').strip().strip("'").strip('"')

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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Ruta al PDF")
    parser.add_argument("-p", "--pages", help="Páginas (0-2,5)")
    args = parser.parse_args()

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