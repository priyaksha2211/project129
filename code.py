import csv

data = []
with open("star_data.csv","r") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        data.append(row)

headers = data[0]
star_data = data[1:]

for data_point in star_data:
    data_point[2] = data_point[2].lower()

star_data.sort(key = lambda star_data : star_data[2])

with open("star_data_sorted.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)

with open("star_data_sorted.csv") as input,open("star_data_sorted1.csv","w",newline = "") as output:
    writer = csv.writer(output)

    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row)