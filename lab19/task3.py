


library = []
with open('C:\\Users\\User\Desktop\\folder python\\lab19\\library.txt', encoding='utf-8', mode='r') as fd:
        for line in fd:
            inner_list = [elt.strip() for elt in line.split(',')]
            # in alternative, if you need to use the file content as numbers
            # inner_list = [int(elt.strip()) for elt in line.split(',')]
            library.append(inner_list)

instances = [x for x in library if x[3] == 'філософська притча']
print(library)
print(instances)
