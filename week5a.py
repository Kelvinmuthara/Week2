
class Device:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")


class Smartphone(Device):
    def __init__(self, brand, model, battery_life, os, storage):
        super().__init__(brand, model, battery_life)
        self.os = os  # Operating System (e.g., Android, iOS)
        self.storage = storage  # Storage in GB
    
    def display_info(self):
        super().display_info()  # Call the parent class method
        print(f"OS: {self.os}")
        print(f"Storage: {self.storage}GB")
    
    def call(self, number):
        print(f"Calling {number}...")

    def take_picture(self):
        print("Taking a picture...")


my_phone = Smartphone("Apple", "iPhone 14", 20, "iOS", 128)
my_phone.display_info()
my_phone.call("123-456-7890")
my_phone.take_picture()
