# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Assessment(Document):
	def validate(self):
		self.calculate_result()

	def calculate_result(self):
		if (self.marks_obtained/self.total_marks * 100) >= 35:
			self.result = "Pass"
		else:
			self.result = "Fail"

