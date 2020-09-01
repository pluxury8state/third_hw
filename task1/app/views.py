import csv

from django.shortcuts import render

def inflation_view(request):
    template_name = 'inflation.html'
    data = []
    # чтение csv-файла и заполнение контекста
    with open('inflation_russia.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)
        names_of_column = data[0].keys()




    context = {
        'data': data,
        'name_of_column': names_of_column

    }

    return render(request, template_name, context)