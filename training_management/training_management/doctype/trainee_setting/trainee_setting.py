# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate, get_datetime


class TraineeSetting(Document):
    pass
@frappe.whitelist()
def mark_all_attendance():
	
	print("python calling")
	logs = frappe.get_all(
		"Trainee Check In",
		filters={
			"log_type": ["in", ["Check In"]],
			
			
		},
		fields=["name","trainee","date","time"]
	)
	print(logs)

	
		
	for x in logs:
		# print(x)
		# trainee  = frappe.db.get_value("Trainee Check In", x["name"], "date")
		# print(trainee)
		trainee_name = x["trainee"]
		check_in_date = getdate(x["date"])
		# print(get_datetime(check_in_date))
		# check_in_datetime = get_datetime(x["date"])
        # check_in_date = check_in_datetime.date()
	


		exists = frappe.db.get_all(
			"Trainee Check In",
			filters = {
				"trainee":trainee_name,
				"log_type":"Check Out",
				"date": check_in_date
				
			},
			fields = ["time","name"]
		)
		print("Check out",exists)
		if exists:
			attendance = frappe.new_doc("Trainee Attendance")
			attendance.trainee_name= trainee_name
			attendance.date = check_in_date
			attendance.in_time = x["time"]
			attendance.check_in  = x["name"]
			attendance.out_time = exists[0]["time"]
			attendance.check_out = exists[0]["name"]
			attendance.insert()
			attendance.save()
			
			
			print(f"Check Out found for {trainee_name} on {check_in_date}")
		else:
			print("No Check Out found")
		
		
		


