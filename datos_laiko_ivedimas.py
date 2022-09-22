import datetime

ivesta_data_laikas = input("įveskite datą ir laiką YYYY-MM-DD hh:mm:ss formatu:")
suformatuotas_laikas = datetime.datetime.strptime(ivesta_data_laikas, "%Y-%m-%d %H:%M:%S")
skirtumas = datetime.datetime.now() - suformatuotas_laikas
print(skirtumas)
