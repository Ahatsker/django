from decimal import Decimal
from django.conf import settings
from shop.models import Shop


class Cart(object):
    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем пустую корзину, если не было предыдущей сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем их из базы данных
        """
        product_ids = self.cart.keys()
        products = Shop.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        :return: Количетсво товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        # Сохраняем товар
        self.session.modified = True

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавляем товар в корзину и обновляем его количество
        :param product:
        :param quantity:
        :param update_quantity:
        :return:
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            # TODO # Сделать проверку строк на двузначное/трехзначное значение айди при поиске
            self.cart[product_id] = {'quantity': 0, "price": str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """
        Удаление товара
        :param product:
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        # получаем общую сумму
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем сессию
        del self.session[settings.CART_SESSION_ID]
        self.save()