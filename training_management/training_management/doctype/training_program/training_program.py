# Copyright (c) 2025, Chaitanya and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import date_diff, getdate
from frappe.model.document import Document


class TrainingProgram(Document):
	def validate(self):
		return
		self.calculate_duration()

		

	def calculate_duration(self):
		start_date = getdate(self.start_date)
		end_date = getdate(self.end_date)
		if self.end_date < self.start_date:
			frappe.throw("End date cannot be less than start date")
		else:
			self.duration = date_diff(self.end_date,self.start_date)

	def validate(self):
		    
			# new_start = getdate(self.start_date)
			# new_end = getdate(self.end_date)

			for trainee in self.trainee_table:
				print("Trainee Name", trainee.trainee_name)
				trainee_id = trainee.trainee_name
				
				existing_programs = frappe.db.get_all(
					"Trainee Table",
					filters = {
						"parenttype" : "Training Program",
						"trainee_name": trainee.trainee_name
					
					},
					fields = ['trainee_name']
					

				)
			print(existing_programs)   

			for row in existing_programs:
				if row.trainee_name == trainee_id:
					frappe.throw(
						f"Trainee '{trainee_id}' is already enrolled in a program "
					)
				
	def validate(self):
		existing = frappe.db.exists(
			"Training Program",
			{
				"trainer": self.trainer,
				
			},
		)
		print(existing)
		if existing:
			frappe.throw(f"Trainer {self.trainer} is already assigned to another Training Program ({existing}). Please select a different trainer.")

			





		
		
		
			

		
			
		
 