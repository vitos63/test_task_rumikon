from typing import Dict, List
from datetime import datetime
from products import (
    FoodProduct,
    PerishableProduct,
    Vitamin,
    FoodPerishableProduct,
)


class Storage:
    def __init__(self,
                 products: Dict[FoodProduct | PerishableProduct | Vitamin | FoodPerishableProduct, int]) -> None:
        self.products = products

    def add_products(self,
                     product: FoodProduct | PerishableProduct | Vitamin | FoodPerishableProduct,count: int) -> str:
        """Данный метод добавляет товары на склад"""
        self.products[product] = self.products.get(product, 0) + count
        return "Товары успешно добавлены"

    def delete_products(self,
                        product: FoodProduct | PerishableProduct | Vitamin | FoodPerishableProduct,
                        count: int = 0, all: bool = False) -> str:
        """Данный метод удаляет товары со склада"""

        if product not in self.products or self.products[product]==0:
            return "Данного товара нет на складе"

        if all:
            count = self.products[product]
            self.products[product] = 0

        else:
            if count>self.products[product]:
                count = self.products[product]
            self.products[product] = self.products.get(product, 0) - count

        return f'Удалено {count} штук товара {product.name}'

    def list_of_products_for_purchase(self) -> List[FoodProduct | PerishableProduct | Vitamin | FoodPerishableProduct]:
        """Данный метод формирует список товаров для закупки"""
        products_for_purchase = []
        for product in self.products:
            if product.count < 5:
                products_for_purchase.append(product)

        return products_for_purchase

    def list_of_products_for_recycling(self) -> List[PerishableProduct | FoodPerishableProduct]:
        """Данный метод формирует список товаров для утилизации"""
        products_for_recycling = []
        for product in self.products:
            if not isinstance(product, PerishableProduct | FoodPerishableProduct):
                continue

            if product.expiration_date - datetime.now() <= 0:
                products_for_recycling.append(product)

        return products_for_recycling
