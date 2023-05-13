import csv

with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    records = []
    for row in csv_reader:
        records.append(row)

    sum = 0
    count = 0
    for i in records[1:]:
        date = i[1].split('/')
        if date[2] == "2006":
            value = i[4].replace(',', '')
            sum = sum + int(value)
            count += 1
        print(i)
    print("Trung binh hoa don nam 2006:")
    print(round(sum/count, 2))
