import csv
from csv import writer

data=[]
column_names=[]
with open("E:\\main.csv") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		data.append(row)
#
name = input("Enter: ")

fields = ['SKU','DESCRIPTION','YEAR','CAPACITY','URL','PRICE','SELLER_INFORMATION','OFFER_DESCRIPTION','COUNTRY']

with open('E:\\filteredCountry.csv', 'w',newline='\n') as f_object:
	writer_object = writer(f_object)
	writer_object.writerow(fields)

col = [x[8] for x in data]

if name in col:
	for x in range(0,len(data)):
		if name == data[x][8]:
			with open('E:\\filteredCountry.csv', 'a',newline='\n') as f_object:
				writer_object = writer(f_object)
				writer_object.writerow(data[x])
				f_object.close()
else:
	print("doesn't exit")

data2=[]


with open("E:\\filteredCountry.csv", 'r') as csvfile:
	reader1 = csv.reader(csvfile)
	for r1 in reader1:
		data2.append(r1)


field1 = ['SKU','FIRST_MINIMUM_PRICE','SECOND_MINIMUM_PRICE']
with open('E:\\lowestPrice.csv', 'w',newline='\n') as f1_object:
	writer_object1 = writer(f1_object)
	writer_object1.writerow(field1)