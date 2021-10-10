# Week 40 Assignment
"""Task 1—Convert multiple lists to list of records"""
data = {'name': ['Joe', 'Pia', 'Even', 'Abdul'],
        'age': [22, 24, 21, 23],
        'phone': ['12345678', '23456789', '34567890', '45678901']}
data1 = {'name': ['Joe', 'Pia', 'Even', 'Abdul'],
        'age': [22, 24, 21 ],
        'phone': ['12345678', '23456789', '34567890', '45678901']}

# def to_records(dt):
#     new_key = list(dt.keys())
#     new_value = list(dt.values())
#
#     flat_value = sum(new_value, [])
#     total_len = len(flat_value)
#     value_len = len(new_value[0])
#     # value_len_list = list(map(len, new_value))
#     B = [flat_value[i:total_len:value_len] for i in range(value_len)]
#     l = []
#     for i in B:
#         dic = dict(zip(new_key, i))
#         l.append(dic)
#     return l

def to_records(dt):
    new_key = list(dt.keys())
    new_value = list(dt.values())
    flat_value = sum(new_value, [])
    total_len = len(flat_value)
    value_len = len(new_value[0])
    value_len_list = list(map(len, new_value))

    if min(value_len_list) == value_len:
        l = []
        B = [flat_value[i:total_len:value_len] for i in range(value_len)]
        for i in B:
            dic = dict(zip(new_key, i))
            l.append(dic)
        return l
    else:
        print('Error')
        print([])

print(to_records(data))
print(to_records(data1))
