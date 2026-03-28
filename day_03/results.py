results = ['Mario', 'Luigi']

results.append('Princess')
results.append('Yoshi')
results.append('Koopa Troopa')
results.append('Toad')

results.append(['Bowser', 'Donkey Kong Jr.'])
results.remove(['Bowser', 'Donkey Kong Jr.'])
results.extend(['Bowser', 'Donkey Kong Jr.'])

new_results = ['Mario', 'Luigi', 'Princess', 'Yoshi', 'Koopa Troopa', 'Toad', 'Bowser', 'Donkey Kong Jr.']

new_results.remove('Bowser')
new_results.insert(0, 'Bowser')
new_results.reverse()

print(results)
print(new_results)
