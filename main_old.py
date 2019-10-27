import local_ru as loc

term = int(input(loc.TERM))
capital = float(input(loc.INITIAL_CAPITAL))
percents = float(input(loc.PERCENTAGE))
investments = float(input(loc.INVESTMENT))

for year in range(term):
    print(year + 1, loc.YEAR)
    print(loc.border)
    print(loc.upper_line)
    print(loc.lower_line)
    print(loc.border)

    for month in range(12):
        month_percentage = capital * (percents / 100)
        fix_capital = capital
        capital = capital * (percents / 100 + 1)
        capital += investments
        print(
            '| {:^5} | {:^13} | {:^13} | {:^13} |'.format(month + 1, round(fix_capital, 2), round(month_percentage, 2),
                                                          (round(capital, 2))))
    print(loc.border)
