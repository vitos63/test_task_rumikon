from datetime import datetime


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class FoodProduct(Product):
    def __init__(self, name:str, price:int|float, count:int, 
                 protein:int, fat:int, carbohydrate:int, calories:int) -> None:
        Product.__init__(self, name, price, count)
        self.protein = protein
        self.fat = fat
        self.carbohydrate = carbohydrate
        self.calories = calories


class PerishableProduct(Product):
    def __init__(self, name:str, price:int|float, count:int, 
                 created_at:datetime, expiration_date:datetime) -> None:
        Product.__init__(self, name, price, count)
        self.created_at = created_at
        self.expiration_date = expiration_date


class Vitamin(Product):
    def __init__(self, name:str, price:int|float, count:int, 
                 available_without_prescription:bool=False) -> None:
        Product.__init__(self, name, price, count)
        self.available_without_prescription = available_without_prescription


class FoodPerishableProduct(FoodProduct, PerishableProduct):
    def __init__(self, name: str, price: int | float, count: int, 
                 protein: int, fat: int, carbohydrate: int, calories: int, 
                 created_at: datetime, expiration_date: datetime) -> None:
        FoodProduct.__init__(self, name, price, count, protein, fat,carbohydrate, calories)
        PerishableProduct.__init__(self, name, price, count, created_at, expiration_date)
