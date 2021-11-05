msg = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_msg = []
for el in msg:
    if el.isdigit():
        el =f'{int(el):02}'
        new_msg.append('"')
        new_msg.append(el)
        new_msg.append('"')
    elif el.strip('+-').isdigit():
        new_msg.append('"')
        el = el[0] + f'{int(el):02d}'
        new_msg.append(el)
        new_msg.append('"')
    else:
        new_msg.append(el)
print(' '.join(new_msg))