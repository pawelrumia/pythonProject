def standardoweWywolanie(argument):
    print(argument)


standardoweWywolanie(10)
standardoweWywolanie(argument=10)


def wywolaniePrzezPozycje(argument, /):
    print(argument)


wywolaniePrzezPozycje(15)


# wywolaniePrzezPozycje(argument=10) blad

def wywolaniePrzezKeyword(*, argument):
    print(argument)


wywolaniePrzezKeyword(argument=20)


# wywolaniePrzezKeyword(20) blad

def wywolanieMieszane(normalny, position, /, *, keyword):
    print(normalny, position, keyword)

wywolanieMieszane(30, 40, keyword=50)

def wymienPlanety(*planety, sep='/'):
    join = sep.join(planety)
    print(join)
    return join


wymienPlanety('merkury', 'wenus', 'ziemia', 'mars', 'jowisz', 'saturn', 'uran')