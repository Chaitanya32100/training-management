# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data()
	return columns, data


def get_columns():
	columns = [
		{
		'fieldname' : 'name',
		'label': 'Name',
		'fieldtype': 'Data',
		},
		{
		'fieldname' : 'full_name',
		'label': 'Full Name',
		'fieldtype': 'Data',
		},
		{
		'fieldname': 'date',
		'label': ('Date'),
		'fieldtype': 'Date',

		},
		{
		'fieldname':'in_time',
		'label': 'In Time',
		'fieldtype': 'Time',
		},
		{
		'fieldname':'out_time',
		'label': 'Out Time',
		'fieldtype': 'Time',
		},
		{
		'fieldname':'total_working_hours',
		'label': 'Total Working Hours',
		'fieldtype': 'Float',
		}

		]
	
	return columns
	data = []
	# trainee_names = frappe.db.get_all("Trainee",["name","full_name"])
	# print(trainee_names)
	# for trainee in trainee_names:
	# 	print(trainee["full_name"])
	# 	data.append({"name": trainee["name"],
	# 		    "full_name":trainee["full_name"]
	# 			})
	# trainee_date = frappe.db.get_all("Trainee Attendance",["date"])
	# print(trainee_date)
	# for date in trainee_date:
	# 	print()
def get_data():
	data = []
	records = frappe.get_all(
		"Trainee Attendance",
		fields=["trainee_name", "date", "in_time", "out_time", "total_working_hours"],
		order_by="date desc"
	)

	for x in records:
		full_name = frappe.db.get_value("Trainee",x.trainee_name,"full_name")
		print(full_name)
		data.append({
			"name": x.trainee_name,
			"full_name": full_name,
			"date": x.date,
			"in_time": x.in_time,
			"out_time": x.out_time,
			"total_working_hours": x.total_working_hours
		})

	return data