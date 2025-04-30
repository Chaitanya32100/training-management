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

//  frappe.ui.form.on("Trainee Setting", {
//      get_trainee(frm) {
       
//            frappe.call({
//                       method:"training_management.training_management.doctype.trainee_setting.trainee_setting.get_trainee",
//                       args: {
//                          docname: frm.doc.name
//                      },
//                       callback : function(r){
//                            console.log(r)
//                       }
//               })
          

//      },
// });

 frappe.ui.form.on("Trainee Setting", {
     get_trainee(frm) {
          frm.clear_table("trainee_table");
           frappe.db.get_list('Trainee',{
               fields:['name']
          
               
          }).then(trainees => {
          console.log("traine",trainees)
               trainees.forEach(trainee => {
               let r = frm.add_child('trainee_table',{
               "trainee_name":trainee.name
               }); 
               console.log("Added trainee:", trainee.name);
          });
          
          
          });
          frm.refresh_field("trainee_table")
          frappe.msgprint("Trainees added succesfully")

     }
 });
