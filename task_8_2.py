def palindrom(word):
    if word == word[::-1]:
        print(word, ' - слово палиндром')
words = input()
new_list = words.split()
for i in new_list:
    palindrom(i)
