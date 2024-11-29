import os

def search_file_in_system(start_path, file_name):
    for root, _, files in os.walk(start_path):
        if file_name in files:
            print(f"Fayl topildi: {os.path.join(root, file_name)}")

if __name__ == "__main__":
    search_name = input("Izlash uchun fayl nomini kiriting: ")
    print(f"{search_name} faylini qidirishni boshlayapmiz...")
    search_file_in_system("C:\\", search_name)
