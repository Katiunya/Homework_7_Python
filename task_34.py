text = 'пара-ра-рам рам-пам-папам па-ра-па-да'
text = text.split()
print(text)
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
count_v = []
for i in text:
    count_v.append(len([x for x in i if x.lower() in vowels]))
if count_v.count(count_v[0]) == len(count_v):
    print('Парам пам-пам')
else:
    print('Пам парам')    