# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt
import frappe
from datetime import date
from frappe.model.document import Document
from frappe.utils import getdate, now


class Trainee(Document):
	def validate(self):
		if self.dob:
			today = date.today()
			dob = getdate(self.dob)
			print("today",today,type(today))
			print("self.dob",self.dob,type(getdate(self.dob)))
			age = today.year - dob.year - (
				(today.month, today.day) < (dob.month, dob.day)
			)
			self.age = age

@frappe.whitelist()
def create_check_in(trainee_name):
		doc = frappe.new_doc("Trainee Check In")
		doc.log_type = "Check In"
		doc.date = now()
		doc.time = now()
		doc.trainee = trainee_name
		doc.insert()
		return frappe.msgprint("Checked In")
@frappe.whitelist()
def create_check_out(trainee_name):
		doc = frappe.new_doc("Trainee Check In")
		doc.log_type = "Check Out"
		doc.date = now()
		doc.time = now()
		doc.trainee = trainee_name
		doc.insert()
		return frappe.msgprint("Checked Out")

