a = {'name': 'ivan', 'age': 18}
a['name'] = 'marijka'
a['phone'] = '555-666' # ne tr da izpolzvame floating-poins
print(a['name'], a["age"])  # obry6ta me se kym klw4a
# nqma dva ednakvi klw4a

if 'name' in a:
    print('true')

del a['name']

for key , val  in a.items(): # vry6ta tuple
    print(key, '----', val)  # i = key
    
print(a.get('kk', 'nema'))