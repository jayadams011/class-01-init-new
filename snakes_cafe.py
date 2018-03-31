

print('****************************************')
print('**     Welcome to the Snakes Cafe!    **')
print('**     Please see our menu below.     **')
print('**                                    **')
print('** To quit at any time, type "quit"   **')
print('****************************************')

apps = ['wings', 'sliders', 'clams']
entrees = ['Grilled Steak', 'Salmon', 'Ragu', 'Phad Thai']
desserts = ['Pie', 'Ice Cream', 'Cake']
drinks = ['Water', 'Coffee', 'Tea']

print('Appetizers')
print('-' * 10)
for item in apps:
    print(item)
    print('\n')

print('Entrees')
print('-' * 7)
for item in entrees:
    print(item)
    print('\n')

print('Desserts')
print('-' * 8)
for item in desserts:
    print(item)
    print('\n')

print('Drinks')
print('-' * 6)
for item in drinks:
    print(item)
    print('\n')

print('*************************************')
print('**  What would you like to order?  **')
print('*************************************')

receipt = {

}

while True:
    order = input('=>')
    if order == 'quit':
        exit()
    if order in receipt:
        receipt[order] += 1
        print(f'{receipt[order]} orders of {order} have been added to your order.')
    else:
        receipt[order] = 1
        print(f'one order of {order} has been added to your order.')
