name = 'ivan'
print(len(name))

for i in name:
    print(i, end=' ')#za da mi se printira na edin red

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(name.find('ov')) #tyrsim string v string; ako e nameren stringa
                       # dava poziciqta na koqto enameren, ako ne -1
print(name.index('iv')) #ako idex ne nameri ne6to vry6ta gre6ka
#startswith -vry6ta true or false
