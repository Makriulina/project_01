def quarter_of(month):
    if month in [1,2,3]:
        return '1 квартал'
    elif month in [4,5,6]:
        return '2 квартал'
    elif month in [7,8,9]:
        return '3 квартал'
    elif month in [10,11,12]:
        return '4 квартал'

month = int(input("Введите номер месяца: "))
print(quarter_of(month))