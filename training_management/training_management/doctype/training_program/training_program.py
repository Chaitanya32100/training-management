# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import date_diff, getdate
from frappe.model.document import Document


class TrainingProgram(Document):
	def validate(self):
		self.calculate_duration()

	def calculate_duration(self):
		start_date = getdate(self.start_date)
		end_date = getdate(self.end_date)
		if self.end_date < self.start_date:
			frappe.throw("End date cannot be less than start date")
		else:
			self.duration = date_diff(self.end_date,self.start_date)
		
		
		
			

		
			
		
 