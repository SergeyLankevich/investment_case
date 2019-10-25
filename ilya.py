import local_ch as loc

def month_format(number):
    """

    :param number: formatting month number
    :return: formatted string with month number
    """
    l = len(str(number))
    return ' '*(5 - l) + str(number) + ' '*4


def table_format(number):
    """

    :param number: formatting number for table cell
    :return: formatted string with number
    """
    t = type(number)
    if type(number) is float:
        number = round(number, 2)
    l = len(str(number))
    return ' '*(12-l) + str(number)


def table_row(col1, col2, col3, col4):
    """

    :param col1: string for first column of table
    :param col2: string for second column of table
    :param col3: string for third column of table
    :param col4: string for fourth column of table
    :return: formatted table row as string
    """
    return '|' + month_format(col1) + '|' + table_format(col2) + '|' + table_format(col3) + '|' + table_format(col4) + '|'


def table(col2, col3, col4):
    """

    :param col2: list with values of first column of table
    :param col3: list with values of second column of table
    :param col4: list with values of third column of table
    :return: print table
    """
    print('-' * 50)
    if loc.LANGUAGE == 'chinese':
        print('|', loc.ROW2_1, '|', loc.ROW2_2, '|', loc.ROW2_3, '|', loc.ROW2_4, '|', sep='')
    else:
        print('|', ' ' * 9, '|', loc.ROW1_1, '|', loc.ROW1_2, '|', ' ' * 12, '|', sep='')
        print('|', loc.ROW2_1, '|', loc.ROW2_2, '|', loc.ROW2_3, '|', loc.ROW2_4, '|', sep='')
    print('-' * 50)
    for i in range(len(col2)):
        print(table_row(i, col2[i], col3[i], col4[i]))
    print('-' * 50)


col2 = [3, 1325, 12512, 12.345, 0.1]
col3 = [32532, 3, 54, 12.32, 121]
col4 = [1, 12, 123, 1234, 12345]

table(col2, col3, col4)