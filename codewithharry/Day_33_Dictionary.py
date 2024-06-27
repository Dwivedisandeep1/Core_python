info = {
    'name' : 'Sandeep',
    'age' : 21,
    'eligible' : True

}
# print(info['name'])
# print(info.get('name'))
# print(info.keys())
#
# for key in info.keys():
#     print(f'The value corresponding to the key {key}'
#           f' is {info[key]}')

print(info.items())

for key , value in info.items():
    print(f'The value corresponding to the key {key}'
            f' is {value}')