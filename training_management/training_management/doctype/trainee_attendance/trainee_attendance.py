# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_hours


class TraineeAttendance(Document):
	def validate(self):
		self.get_attendance()
		self.get_overtime()
		

	def get_attendance(self):
		in_time = self.in_time
		out_time = self.out_time
		self.total_working_hours = time_diff_in_hours(out_time,in_time)

	def get_overtime(self):
		working_hours = frappe.db.get_single_value("Trainee Setting", "working_hours")

		
		if working_hours and self.total_working_hours:
			self.standard_hours = working_hours  

		
		if self.total_working_hours > working_hours:
			self.over_time = self.total_working_hours - working_hours
		else:
			self.over_time = 0
		# if working_hours and self.total_working_hours:
		# 	
		# 	if self.total_working_hours > working_hours:
		# 		self.over_time = self.total_working_hours - working_hours

		# 	else:
		# 		self.over_time = 0
	


	




		
