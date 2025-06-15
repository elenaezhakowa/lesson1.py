from smartphone1 import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 14 Pro Max", "+79876543210"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79123456789"),
    Smartphone("Xiaomi", "Redmi Note 11", "+79876543211"),
    Smartphone("Huawei", "P50 Pro", "+79123456788"),
    Smartphone("Google", "Pixel 7 Pro", "+79876543212")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
