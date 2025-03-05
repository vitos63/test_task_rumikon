from unittest import TestCase
from datetime import datetime
from products import FoodProduct, PerishableProduct, Vitamin, FoodPerishableProduct
from user_cart import UserCart
from storage_management import Storage


class TestProduct(TestCase):
    def test_create_food_product(self):
        product = FoodProduct(name="banana", price=20, count=5,
                              protein=4, fat=1, carbohydrate=50,
                              calories=150)
        self.assertTrue(product.name, "banana")
        self.assertTrue(product.price, 20)
        self.assertTrue(product.count, 5)
        self.assertTrue(product.protein, 4)
        self.assertTrue(product.fat, 1)
        self.assertTrue(product.carbohydrate, 50)
        self.assertTrue(product.calories, 150)

    def test_create_perishable_product(self):
        product = PerishableProduct(name="milk", price=20, count=5,
            created_at=datetime(2024, 5, 5), expiration_date=datetime(2024, 6, 5),)
        self.assertTrue(product.name, "milk")
        self.assertTrue(product.price, 20)
        self.assertTrue(product.count, 5)
        self.assertTrue(product.created_at, datetime(2024, 5, 5))
        self.assertTrue(product.expiration_date, datetime(2024, 6, 5))

    def test_create_vitamin(self):
        product = Vitamin(name="C", price=20, count=5,
                           available_without_prescription=True)
        self.assertTrue(product.name, "C")
        self.assertTrue(product.price, 20)
        self.assertTrue(product.count, 5)
        self.assertTrue(product.available_without_prescription, True)

    def test_create_food_perishable_product(self):
        product = FoodPerishableProduct(name="banana",price=20,count=5,
                                        protein=4, fat=1, carbohydrate=50,
                                        calories=150, created_at=datetime(2024, 5, 5),
                                        expiration_date=datetime(2024, 6, 5))
        self.assertTrue(product.name, "C")
        self.assertTrue(product.price, 20)
        self.assertTrue(product.count, 5)
        self.assertTrue(product.protein, 4)
        self.assertTrue(product.fat, 1)
        self.assertTrue(product.carbohydrate, 50)
        self.assertTrue(product.calories, 150)
        self.assertTrue(product.created_at, datetime(2024, 5, 5))
        self.assertTrue(product.expiration_date, datetime(2024, 6, 5))


class TestUserCart(TestCase):

    def setUp(self):
        self.test_cart = UserCart(protein_limit=150, fat_limit=50, 
                                  carbohydrate_limit=500, calories_limit=3000)
        self.food_product = FoodProduct(name="banana", price=20, count=5,
                                        protein=4, fat=1, carbohydrate=50,
                                        calories=150)
        self.perishable_product = PerishableProduct(name="milk", price=20, count=5,
                                                    created_at=datetime(2024, 5, 5),
                                                    expiration_date=datetime(2025, 6, 5))
        self.vitamin = Vitamin(name="C", price=20, count=5, 
                               available_without_prescription=True)
        self.food_perishable_product = FoodPerishableProduct(name="banana", price=20, count=5,
                                                             protein=4, fat=1, carbohydrate=50,
                                                             calories=150, created_at=datetime(2024, 5, 5),
                                                             expiration_date=datetime(2025, 6, 5))

    def test_add_food_product_success(self):
        response = self.test_cart.add_product(self.food_product)
        self.assertEqual(response, "Товар успешно добавлен, лимиты БЖУ и калорий не превышены")
        self.assertIn(self.food_product, self.test_cart.products)

    def test_add_perishable_product_success(self):
        response = self.test_cart.add_product(self.perishable_product)
        self.assertEqual(response, "Товар успешно добавлен, лимиты БЖУ и калорий не превышены")
        self.assertIn(self.perishable_product, self.test_cart.products)

    def test_add_vitamin_product_success(self):
        response = self.test_cart.add_product(self.vitamin)
        self.assertEqual(response, "Товар успешно добавлен, лимиты БЖУ и калорий не превышены")
        self.assertIn(self.vitamin, self.test_cart.products)

    def test_add_food_perishable_product_success(self):
        response = self.test_cart.add_product(self.food_perishable_product)
        self.assertEqual(response, "Товар успешно добавлен, лимиты БЖУ и калорий не превышены")
        self.assertIn(self.food_perishable_product, self.test_cart.products)

    def test_add_ended_product(self):
        self.food_perishable_product.count = 0
        response = self.test_cart.add_product(self.food_perishable_product)
        self.assertEqual(response, "Данный товар отсутсвует на складе")
        self.assertNotIn(self.food_perishable_product, self.test_cart.products)

    def test_add_expired_product(self):
        self.food_perishable_product.expiration_date = datetime.now()
        response = self.test_cart.add_product(self.food_perishable_product)
        self.assertEqual(response, "У данного товара скоро истечет, либо уже истек срок годности")
        self.assertNotIn(self.food_perishable_product, self.test_cart.products)

    def test_add_not_available_without_prescription_vitamin(self):
        self.vitamin.available_without_prescription = False
        response = self.test_cart.add_product(self.vitamin)
        self.assertEqual(response, "Данный витами не продается без рецепта")
        self.assertIn(self.vitamin, self.test_cart.products)

    def test_over_limit_protein(self):
        self.food_product.protein = 160
        response = self.test_cart.add_product(self.food_product)
        self.assertEqual(response, "Превышена норма белка")
        self.assertIn(self.food_product, self.test_cart.products)

    def test_over_limit_fat(self):
        self.food_product.fat = 60
        response = self.test_cart.add_product(self.food_product)
        self.assertEqual(response, "Превышена норма жира")
        self.assertIn(self.food_product, self.test_cart.products)

    def test_over_limit_carbohydrate(self):
        self.food_product.carbohydrate = 660
        response = self.test_cart.add_product(self.food_product)
        self.assertEqual(response, "Превышена норма углеводов")
        self.assertIn(self.food_product, self.test_cart.products)

    def test_over_limit_calories(self):
        self.food_product.calories = 3660
        response = self.test_cart.add_product(self.food_product)
        self.assertEqual(response, "Превышена норма калорий")
        self.assertIn(self.food_product, self.test_cart.products)

    def test_over_multiply_lmit(self):
        self.food_product.calories = 3660
        self.food_product.fat = 60
        self.food_product.protein = 160
        response = self.test_cart.add_product(self.food_product)
        self.assertEqual(response,"Превышена норма белка, Превышена норма жира, Превышена норма калорий")
        self.assertIn(self.food_product, self.test_cart.products)

    def test_delete_unknown_product(self):
        response = self.test_cart.delete_product(self.food_product)
        self.assertEqual(response, "Данного товара нет в корзине")

    def test_delete_product_success(self):
        self.test_cart.add_product(self.food_product)
        response = self.test_cart.delete_product(self.food_product)
        self.assertEqual(response, "Товар успешно удален из корзины")

    def test_total_cost(self):
        self.test_cart.add_product(self.food_product)
        self.test_cart.add_product(self.food_product)
        self.assertEqual(self.test_cart.total_cost(), 'Общая стоимость товаров в корзине 40')
        self.test_cart.add_product(self.vitamin)
        self.assertEqual(self.test_cart.total_cost(), 'Общая стоимость товаров в корзине 60')


class TestStorageManagement(TestCase):
    def setUp(self):
        self.food_product = FoodProduct(name="banana", price=20, count=5,
                                        protein=4, fat=1, carbohydrate=50,
                                        calories=150)
        self.perishable_product = PerishableProduct(name="milk", price=20, count=5,
                                                    created_at=datetime(2024, 5, 5),
                                                    expiration_date=datetime(2025, 6, 5))
        self.vitamin = Vitamin(name="C", price=20, count=5, available_without_prescription=True)
        self.food_perishable_product = FoodPerishableProduct(name="banana", price=20, count=5,
                                                             protein=4, fat=1, carbohydrate=50,
                                                             calories=150, created_at=datetime(2024, 5, 5),
                                                             expiration_date=datetime(2025, 6, 5))
        self.test_storage = Storage(
            {self.food_product: 3,
             self.perishable_product: 2,
             self.vitamin: 10,
             self.food_perishable_product: 8}
             )

    def test_add_product(self):
        response = self.test_storage.add_products(self.vitamin, 5)
        self.assertEqual(self.test_storage.products[self.vitamin], 15)
        self.assertEqual(response, "Товары успешно добавлены")

    def test_delete_unknown_product(self):
        self.unknown_food = FoodProduct(name="unknown", price=20, count=5,
                                        protein=4, fat=1, carbohydrate=50,
                                        calories=150)
        response = self.test_storage.delete_products(self.unknown_food)
        self.assertEqual(response, "Данного товара нет на складе")

    def test_delete_some_products(self):
        response = self.test_storage.delete_products(self.food_product, 2)
        self.assertEqual(response, f"Удалено 2 штук товара {self.food_product.name}")
        self.assertEqual(self.test_storage.products[self.food_product], 1)

    def test_delete_more_then_have_products(self):
        response = self.test_storage.delete_products(self.food_product, 4)
        self.assertEqual(response, f"Удалено 3 штук товара {self.food_product.name}")
        self.assertEqual(self.test_storage.products[self.food_product], 0)

    def test_delete_all_products(self):
        response = self.test_storage.delete_products(self.food_product, all=True)
        self.assertEqual(response, f"Удалено 3 штук товара {self.food_product.name}")
        self.assertEqual(self.test_storage.products[self.food_product], 0)

    def test_list_of_products_for_purchase(self):
        response = self.test_storage.list_of_products_for_purchase()
        correct_response = list(filter(lambda x: x.count < 5, self.test_storage.products))
        self.assertEqual(response, correct_response)

    def test_list_of_products_for_recycling(self):
        response = self.test_storage.list_of_products_for_purchase()
        correct_response = list(
            filter(lambda x: isinstance(x, PerishableProduct | FoodPerishableProduct)
                and (x.expiration_date - datetime.now()).days <= 0,
                self.test_storage.products)
                )
        self.assertEqual(response, correct_response)
