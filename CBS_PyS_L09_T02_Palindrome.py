def palindrome(text_to_check):
    t = ''.join(text_to_check.lower().split())
    if t[0:len(t) // 2] == t[len(t):len(t) // 2:-1]:
        print(f'Your text is a palindrome')
    else:
        print(f'Your text is not a palindrome')


while True:
    text_to_check = input('Enter text to check if it is a palindrome, \'off\' to exit: ')
    if text_to_check == 'off':
        exit()
    palindrome(text_to_check)
