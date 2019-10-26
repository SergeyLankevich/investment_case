import ru_local

term = int(input(ru_local.term))
capital = float(input(ru_local.initial_capital))
percents = float(input(ru_local.percentage))
investments = float(input(ru_local.investment))

for year in range(term):
    print(year + 1, ru_local.year)
    print(ru_local.border)
    print(ru_local.upper_line)
    print(ru_local.lower_line)
    print(ru_local.border)

    for month in range(12):
        month_percentage = capital * (percents / 100)
        fix_capital = capital
        capital = capital * (percents / 100 + 1)
        capital += investments
        print(
            '| {:^5} | {:^13} | {:^13} | {:^13} |'.format(month + 1, round(fix_capital, 2), round(month_percentage, 2),
                                                          (round(capital, 2))))
    print(ru_local.border)
