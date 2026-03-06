# ==========================================
# SOAL NOMOR 1: Membuat Kelas Restaurant
# ==========================================

print("--- Soal Nomor 1: Buat kelas bernama Restaurant ---")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # Menyimpan dua atribut (state)
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        # Mencetak kedua informasi
        print(f"Nama Restoran: {self.restaurant_name}")
        print(f"Jenis Masakan: {self.cuisine_type}")
        
    def open_restaurant(self):
        # Mencetak pesan restoran buka
        print(f"Restoran {self.restaurant_name} sekarang sudah buka!\n")

# Membuat instance bernama 'restaurant'
restaurant = Restaurant("Ajo Awak", "Padang")

# Mencetak kedua atribut secara terpisah
print("--- Atribut Terpisah ---")
print() #Biar Rapi
print(f"Atribut Nama: {restaurant.restaurant_name}")
print(f"Atribut Masakan: {restaurant.cuisine_type}")
print() #Biar Rapi
print("------------------------")
print() #Biar Rapi

# Memanggil kedua metode
restaurant.describe_restaurant()
restaurant.open_restaurant()


# ==========================================
# SOAL NOMOR 2: Tiga Instance Berbeda
# ==========================================
print("--- Soal Nomor 2: Tiga Instance Berbeda ---")

# Membuat 3 instance berbeda dari kelas Restaurant
resto1 = Restaurant("Baklava", "Makanan Manis Turki")
resto2 = Restaurant("KFC", "Cepat Saji")
resto3 = Restaurant("Ayam bumbu", "Indonesia")

# Memanggil describe_restaurant() untuk setiap instance
resto1.describe_restaurant()
print() # baris kosong agar rapi
resto2.describe_restaurant()
print()
resto3.describe_restaurant()
print("\n")


# ==========================================
# SOAL NOMOR 3: Membuat Kelas User
# ==========================================

class User:
    def __init__(self, first_name, last_name, age, location, job):
        # Atribut wajib dan atribut profil tambahan
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.job = job
        
    def describe_user(self):
        # Mencetak ringkasan informasi pengguna
        print(f"Ringkasan Profil: {self.first_name} {self.last_name}")
        print(f"Umur    : {self.age} tahun")
        print(f"Lokasi  : {self.location}")
        print(f"Pekerjaan: {self.job}")
        
    def greet_user(self):
        # Mencetak salam pribadi
        print(f"Halo, {self.first_name}! Selamat datang kembali.\n")

# Membuat beberapa instance yang mewakili user berbeda
user1 = User("Rafli", "Aswiansyah", 19, "Pekanbaru", "Programmer")
user2 = User("Reski", "Putra", 19, "Medan", "Desainer Grafis")
user3 = User("Aldi", "Dewo", 20, "Tembilahan", "Mahasiswa Ilmu Hukum")

# Memanggil kedua metode untuk setiap user
print("--- Soal Nomor 3: Profil User ---")
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
