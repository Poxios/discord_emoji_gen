string = input('')
for i in string:
    if i == ' ':
        print(' ', end=' ')
    else:
        print(":regional_indicator_" + i + ":", end=' ')
