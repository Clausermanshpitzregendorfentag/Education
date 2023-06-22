##price = 100
#discount = 50
def discounted(price,discount): 
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount

product = {'name':'Samsung Gal', 'stock': 8, 'price': 50000.0, 'discount': 50}
product['with_discount'] = discounted(product['price'], product['discount'])
print(product)