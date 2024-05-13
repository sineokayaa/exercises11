class Item:
    '''
    A class representing an item.

    Attributes:
        code_info (dict): A dictionary containing information
                        about item codes and their corresponding countries.
    '''
    code_info = {}

    def __init__(self, ptr):
        '''
        Initialize the item with its code, name, price, and other details
        '''
        ptr = ptr.split(';')
        self.code = ptr[0]
        self.name = ptr[1]
        self.__price = ptr[2]
        self.amount = 0
        with open('code.txt', 'r', encoding='utf-8') as f:
            for ptr in f:
                Item.code_info[ptr.split(';')[0]] = ptr.split(';')[1][:-1]
        if self.code[0:3] not in Item.code_info.keys():
            self.country = None
        else:
            self.country = Item.code_info[self.code[0:3]]
        self.company_code = self.code[3:7]
        self.item_code = self.code[7:11]
        self.num = self.code[-1]
        self.main_info = (f'Название товара: {self.name}.'
                          f'Цена: {self.__price}.'
                          f'Код: {self.code}.'
                          f'К-во: {self.amount}')
        ShopBasket.lst_items.append(self)

    def __str__(self):
        return (f'Название товара: {self.name}.'
                f'Цена: {self.__price}.'
                f'Код: {self.code}.'
                f'К-во: {self.amount}')

    def __repr__(self):
        return str(f'Название товара: {self.name}.'
                   f'Цена: {self.__price}.'
                   f'Код: {self.code}.'
                   f'К-во: {self.amount}')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        '''Set the price of the item.'''
        if isinstance(new_price, int) or isinstance(new_price, float):
            if new_price > 0:
                self.__price = new_price

    @price.getter
    def price(self):
        '''
        Get the price of the item.
        '''
        return self.__price

    def set_price(self, new_price):
        '''
        Set the price of the item.
        '''
        self.price=new_price


class ShopBasket:
    '''
    A class representing a shopping basket.
    '''
    lst_items = []
    lst_basket = []
    total_basketsumm = 0

    @classmethod
    def add_item(cls):
        '''
        Add an item to the shopping basket.
        '''
        supply = ''
        for i in range(1, len(ShopBasket.lst_items) + 1):
            supply += f'{i}. {ShopBasket.lst_items[i - 1]}{'\n'}'
        print(supply)
        choice = int(input('Введите номер:'))
        while choice not in range(0, len(ShopBasket.lst_items) + 1):
            print(supply)
            print('Такого товара нет в наличии. Выберите заново или нажмите 0, если не выбираете ничего.')
            choice = int(input())
        if choice == 0:
            print('Вы ничего не выбрали.')
        else:
            ShopBasket.lst_items[choice - 1].amount += 1
            ShopBasket.lst_basket.append(ShopBasket.lst_items[choice - 1])
            ShopBasket.total_basketsumm += int(ShopBasket.lst_items[choice - 1].price)

    @classmethod
    def delete_item(cls):
        '''
        Delete an item from the shopping basket.
        '''
        print(ShopBasket.show_basket())
        choice = int(input('Выберите номер товара, который хотите удалить из корзины: '))
        while choice not in range(0, len(ShopBasket.lst_basket) + 1):
            print(ShopBasket.show_basket())
            choice = int(input('Такого товара нет в коризне. Выберите заново или нажмите 0, если не выбираете ничего.'))
        if choice == 0:
            print('Вы ничего не выбрали.')
        else:
            if ShopBasket.lst_basket[choice-1].amount > 1:
                ShopBasket.lst_basket[choice - 1].amount -= 1
                print(ShopBasket.show_basket())
            else:
                ShopBasket.lst_basket.remove(ShopBasket.lst_basket[choice-1])
                print(ShopBasket.show_basket())
            ShopBasket.total_basketsumm -= int(ShopBasket.lst_items[choice - 1].price)

    @classmethod
    def show_basket(cls):
        '''
        Display the contents of the shopping basket.
        '''
        basket = ''
        set_basket = set(ShopBasket.lst_basket)
        lst_set_basket = list(set_basket)
        ShopBasket.lst_basket = lst_set_basket
        for i in range(1, len(lst_set_basket) + 1):
            basket += f'{i}. {lst_set_basket[i - 1]} {'\n'}'
        return f'Корзина: {basket}'


with open('items.txt', 'r', encoding='utf-8') as f:
    for ptr in f:
        Item(ptr[:-1])  # [:-1] чтобы убрать \n


item = ShopBasket.lst_items[2]
print(item)
print(item.price)
item.set_price(43)
print(item.price)
print(item)
print(Item.code_info)
print(ShopBasket.lst_items)
ShopBasket.add_item()
ShopBasket.add_item()
ShopBasket.add_item()
print()
ShopBasket.delete_item()
ShopBasket.delete_item()
ShopBasket.delete_item()
ShopBasket.delete_item()