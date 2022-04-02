from pprint import pprint


def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as file:
        cook_book = {}
        while True:
            key = file.readline().strip().strip()
            if not key:
                break
            cook_book[key] = []
            ingredient_count = int(file.readline().strip())
            for line in range(ingredient_count):
                ingredient = file.readline().strip().split(" | ")
                cook_book[key] += [
                    {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}]
            file.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    cook_book = get_cook_book()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                key = ingredient['ingredient_name']
                if key in shop_list_by_dishes:
                    quantity = int(shop_list_by_dishes[key]['quantity']) + int(ingredient['quantity'])
                else:
                    quantity = ingredient['quantity']
                value = {'measure': ingredient['measure'], 'quantity': quantity}
                shop_list_by_dishes[key] = value
    for key in shop_list_by_dishes:
        shop_list_by_dishes[key]['quantity'] *= int(person_count)
    return shop_list_by_dishes

shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(shop_list)

