language = input('Choose language:\n1. English\n2. Russian\n3. Chinese\n')
while True:
    if (language.lower() == 'english' or language.lower() == 'en' or language == '1' or language == '1.' or
            language.lower() == '1. english'):
        import local_en as loc
        break
    elif (language.lower() == 'russian' or language.lower() == 'ru' or language == '2' or language == '2.' or
            language.lower() == '2. russian'):
        import local_ru as loc
        break
    elif (language.lower() == 'chinese' or language.lower() == 'ch' or language == '3' or language == '3.' or
            language.lower() == '3. chinese'):
        import local_ch as loc
        break
    else:
        language = input('Choose language:\n1. English\n2. Russian\n3. Chinese\n')

term = input(loc.TERM)
while True:
    try:
        term = int(term)
    except ValueError:
        term = input(loc.INPUT_ERROR)
    else:
        break
capital = input(loc.INITIAL_CAPITAL)
while True:
    try:
        capital = float(capital)
    except ValueError:
        capital = input(loc.INPUT_ERROR)
    else:
        break
percents = input(loc.PERCENTAGE)
while True:
    try:
        percents = float(percents)
    except ValueError:
        percents = input(loc.INPUT_ERROR)
    else:
        break
investments = input(loc.INVESTMENT)
while True:
    try:
        investments = float(investments)
    except ValueError:
        investments = input(loc.INPUT_ERROR)
    else:
        break

for year in range(term):
    print(year + 1, loc.YEAR)
    print(loc.BORDER)
    if loc.LANGUAGE == 'chinese':
        print(loc.LINE1)
    else:
        print(loc.LINE1)
        print(loc.LINE2)
    print(loc.BORDER)

    for month in range(12):
        month_percentage = capital * (percents / 100)
        fix_capital = capital
        capital = capital * (percents / 100 + 1)
        print('| {:^5} | {:^13} | {:^13} | {:^13} |'.format(month + 1, round(fix_capital, 2),
              round(month_percentage, 2), (round(capital, 2)))
        )
        capital += investments
    print(loc.BORDER)
