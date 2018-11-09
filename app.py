from database import DatabaseConnection

db = DatabaseConnection()
parcels = db.get_all_parcel()
print(parcels)

for parcel in parcels:
	print('######')
	item = ''
	item += ' ' +  parcel['name']
	item += ' ' +  parcel['source']
	item += ' ' +  parcel['destination']
	item += ' ' +  str(parcel['price'])
	item += ' ' +  str(parcel['delivery_date'])
	item += ' ' +  str(parcel['delivered'])
	print(item)



# rowcount = db.create_parcel('mac pro', 'kiwatule', 'ntinda', 999000, '2018-07-21', False)
# print(rowcount)