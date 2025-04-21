# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_hours


class TraineeAttendance(Document):
	def validate(self):
		self.get_attendance()

	def get_attendance(self):
		in_time = self.in_time
		out_time = self.out_time
		self.total_working_hours = time_diff_in_hours(out_time,in_time)
