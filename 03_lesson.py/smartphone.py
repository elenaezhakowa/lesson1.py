class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number


catalog = [
    Smartphone("Apple", "iPhone 12", "+79876543210"),
    Smartphone("Samsung", "Galaxy S21", "+79876543211"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79876543212"),
    Smartphone("Huawei", "P40 Pro", "+79876543213"),
    Smartphone("Google", "Pixel 5", "+79876543214")
]

for item in catalog:
    print(f"{item.brand} - {item.model}. Номер телефона: {item.phone_number}")
