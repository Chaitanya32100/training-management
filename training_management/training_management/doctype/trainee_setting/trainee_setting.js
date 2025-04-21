// Copyright (c) 2025, Chaitanya and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Trainee Setting", {
 	mark_attendance(frm) {
        
            frappe.call({
                       method:"training_management.training_management.doctype.trainee_setting.trainee_setting.mark_all_attendance",
                       callback : function(r){
                            console.log(r)
                       }
               })
           

 	},
 });
