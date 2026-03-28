text = input('Input: ')

no_vowel_text = ''.join(c for c in text if c not in 'aeiouAEIOU')

print(f'Output: {no_vowel_text}')
