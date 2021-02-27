#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with and
#inserted before the last item. For example, passing the previous spam list to
#the function would return 'apples, bananas, tofu, and cats'. But your function
#should be able to work with any list value passed to it.

spam = ['apple', 'bananas', 'tofu', 'cats']

def comma(spam):
    spam.insert(len(spam)-1, 'and')
    for i in range(len(spam)-2):
        print(spam[i] + ', ', end='')
    print(spam[len(spam)-2] + ' ' + spam[len(spam)-1])

comma(spam)
