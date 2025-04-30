// Copyright (c) 2025, Chaitanya and contributors
// For license information, please see license.txt

frappe.query_reports["Training Program Allocation"] = {
	"filters": [
		{
			fieldname: 'training_program',
			label: "Training Program",
			fieldtype: 'Link',
			options: 'Training Program'
			
		}

	]
};

