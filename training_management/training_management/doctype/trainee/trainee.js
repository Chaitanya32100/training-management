// Copyright (c) 2025, Chaitanya and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Trainee", {
 	refresh(frm) {
        frm.add_custom_button("Check In", () => {
            frappe.call({
                method: "training_management.training_management.doctype.trainee.trainee.create_check_in",
                args: {
                 "trainee_name":frm.doc.name
                },
                callback : function(r){

                }
        })
    });
        frm.add_custom_button("Check Out", () => {
            frappe.call({
                method: "training_management.training_management.doctype.trainee.trainee.create_check_out",
                args: {
                    "trainee_name":frm.doc.name
                },
                callback: function(r){

                }
            })
        });
                

 	},
 });
