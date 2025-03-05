from datetime import datetime
from products import (
    FoodProduct,
    PerishableProduct,
    Vitamin,
    FoodPerishableProduct,
)


class UserCart:
    def __init__(self, protein_limit: int, fat_limit: int, 
                 carbohydrate_limit: int, calories_limit: int) -> None:
        self.protein_limit = protein_limit
        self.fat_limit = fat_limit
        self.carbohydrate_limit = carbohydrate_limit
        self.calories_limit = calories_limit
        self.current_protein = 0
        self.current_fat = 0
        self.current_carbohydrate = 0
        self.current_calories = 0
        self.products = {}

    def add_product(self,
                    product: FoodProduct | PerishableProduct | Vitamin | FoodPerishableProduct) -> str:
        """Данный метод добавляет товар в корзину, если он не отсутсвует на складе и если не истекает срок годности
        Так же предупреждает пользователя о превышении норм БЖУ и добавлении витаминов, который продаются только по рецепту
        """
        if product.count == 0:
            return "Данный товар отсутсвует на складе"

        if (isinstance(product, FoodPerishableProduct | PerishableProduct)
            and (product.expiration_date - datetime.now()).days <= 0
        ):
            return "У данного товара скоро истечет, либо уже истек срок годности"

        self.products[product] = self.products.get(product, 0) + 1

        warnings = []
        if isinstance(product, Vitamin) and not product.available_without_prescription:
            warnings.append("Данный витами не продается без рецепта")

        if isinstance(product, FoodProduct | FoodPerishableProduct):
            self.current_protein += product.protein
            self.current_fat += product.fat
            self.current_carbohydrate += product.carbohydrate
            self.current_calories += product.calories

        if self.current_protein > self.protein_limit:
            warnings.append("Превышена норма белка")

        if self.current_fat > self.fat_limit:
            warnings.append("Превышена норма жира")

        if self.current_carbohydrate > self.carbohydrate_limit:
            warnings.append("Превышена норма углеводов")

        if self.current_calories > self.calories_limit:
            warnings.append("Превышена норма калорий")

        return ", ".join(warnings) if warnings else "Товар успешно добавлен, лимиты БЖУ и калорий не превышены"

    def delete_product(self,
                        product: FoodProduct | PerishableProduct | Vitamin | FoodPerishableProduct) -> str:
        """Данный метод удаляет товар из корзины пользователя"""
        if not product in self.products:
            return "Данного товара нет в корзине"

        self.products[product] -= 1
        if self.products[product] == 0:
            del self.products[product]

        return "Товар успешно удален из корзины"

    def total_cost(self) -> str:
        """Данный метод рассчитывает суммарную стоимость товаров в корзине"""
        cost = 0
        for product in self.products:
            cost += product.price * self.products[product]

        return f'Общая стоимость товаров в корзине {cost}'
