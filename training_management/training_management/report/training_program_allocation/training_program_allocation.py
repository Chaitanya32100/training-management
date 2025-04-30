# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	print("Filters are :",filters)
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
	columns = [
	{
	'fieldname' : 'training_program',
	'label': 'Training Program',
	'fieldtype': 'Link',
	'options': 'Training Program',
	},
	{
	'fieldname' : 'trainee',
	'label': 'Trainee',
	'fieldtype': 'Link',
	'options': 'Trainee',
	},
	{
	'fieldname' : 'start_date',
	'label': 'Start Date',
	'fieldtype': 'Date',
	},
	{
	'fieldname' : 'end_date',
	'label': 'End Date',
	'fieldtype': 'Date',
	},

]
	return columns
	
def get_data(filters):
	print("tHI IS SHOWING FROM GET DATA", filters)
	print("**888***",filters.get("training_program"))
	training_program = filters.get("training_program")
	data = frappe.db.sql("""
		SELECT 
			tp.name AS training_program,
			tt.trainee_name AS trainee, 
			tp.start_date,
			tp.end_date
		FROM 
			`tabTraining Program` as tp
		LEFT JOIN 
			`tabTrainee Table` tt  ON parent = tp.name
		WHERE
			tp.name = %s
					
		

	""", (training_program,),as_dict = 1) 

	print(data)
	return data
