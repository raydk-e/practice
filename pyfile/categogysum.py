def categorysum(l):
    dic = { }
    for i in l:
        category = i['category']
        dic[category] = dic.get(category,0) + i['spend']
    return dic
l1 = [{'category': 'Tech', 'spend': 100}, {'category': 'Food', 'spend': 50}, {'category': 'Tech', 'spend': 200}]
p = categorysum(l1)
print(p)
