import os
def search_file_in_system(start_path, file_name):
    found_files = []
    for root, dirs, files in os.walk(start_path):
        if file_name in files:
            found_files.append(os.path.join(root, file_name))
            print(f"Fayl topildi: {os.path.join(root, file_name)}")
    return found_files

if __name__ == "__main__":
    search_name = input("Izlash uchun fayl nomini kiriting (masalan: 'example.txt'): ")
    start_directory = "C:\\"  # Barcha tizim bo'ylab qidirish uchun
    print(f"{search_name} faylini qidirishni boshlayapmiz...")
    results = search_file_in_system(start_directory, search_name)

    if results:
        print("\nIzlash yakunlandi. Quyidagi fayllar topildi:")
        for file_path in results:
            print(file_path)
    else:
        print("\nFayl topilmadi.")

    input()
