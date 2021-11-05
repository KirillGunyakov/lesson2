def show_price(items, show_delim=True):
    for price in items:
        price = int(round(price*100))
        rubles = price // 100
        cent = price % 100
        print(f'{rubles:02d} руб {cent:02d} коп', end=',')
    if show_delim:
        print()
price = [45.56, 506.45, 340546.44, 4959.55, 777.56, 30495.22, 23.34, 11.01, 67.55, 123.45]
show_price(price)
price.sort()
show_price(price)
price_desc = sorted(price, reverse=True)
show_price(price_desc)
show_price(price_desc[4::-1], False)