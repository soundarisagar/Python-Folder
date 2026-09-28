s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print(s3,"\n")


list1 = [1, 2, 3]
list2 = [4, 5, 6]

for x, y in zip(list1, list2):
    print(x, y)


stocks = ['reliance', 'tata', 'infosys']
prices = [1000, 2000, 3000]

new_dict = dict(zip(stocks, prices))
print('\n{}'.format(new_dict))