// Copyright (c) 2025, Chaitanya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Trainee", {
 	refresh(frm) {
        frm.add_custom_button("Check In", () => {
            frappe.call({
                method: "training_management.training_management.doctype.trainee.trainee.create_check_in",
                args:{
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
    
    frappe.ui.form.on("Trainee",{
        dob: function(frm){
            if(frm.doc.dob){
                frappe.call({
                    method:"training_management.training_management.doctype.trainee.trainee.calculate_age",
                    args:{
                        "dob":frm.doc.dob
                    },
                    callback: function(r){
                        console.log(r.message)
                        frm.set_value('age',r.message["age"])
    
                    }
                })
                
            }


        },

    });


 
    //     validate: function(frm){
    //     if(frm.doc.dob){
    //         let dob = new Date(frm.doc.dob);
    //         let today = new Date();

    //         let age = today.getFullYear() - dob.getFullYear();
    //         const month_diff = today.getMonth() - dob.getMonth();    

    //     }
    //    }       
