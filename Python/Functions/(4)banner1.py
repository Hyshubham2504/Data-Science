#this function allows different width to be used


# def banner_text(text, screen_width):
def banner_text(text, screen_width=80):  # default parameter value so in this case we dont need to put 2nd argument value each time
    if len(text)>screen_width-4:
        raise ValueError("The width of {0} is greater than screenwidth i.e., {1}".format(text, screen_width))

    if text == '*':
        print("*" * screen_width)
    else:
        print("**{}**".format(text.center(screen_width-4)))

banner_text("*")
banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!",66)
banner_text("And that's to laugh and smile and dance and sing,",66)
banner_text("When you're feeling in the dumps,`",66)
banner_text("Don't be silly chumps,",66)
banner_text("Just purse your lips and whistle -- that's the thing!",66)
banner_text("And... always look on the bright side of life...",66)
banner_text("*",66)
banner_text("*",66)
print(banner_text("And... always look on the bright side of life...",66))
