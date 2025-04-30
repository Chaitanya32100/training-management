// Copyright (c) 2025, Chaitanya and contributors
// For license information, please see license.txt


frappe.ui.form.on('Training Program', {
   
    refresh: function(frm) {
        
    }
});

frappe.ui.form.on('Trainee Table', {
    
    amount: function(frm, cdt, cdn) {
        calculate_grand_total(frm);
    },

    
  
});


function calculate_grand_total(frm) {
    let total = 0;
    frm.doc.trainee_table.forEach(row => {
        total += row.amount;
    });
    frm.set_value('grand_total', total);
}




// frappe.ui.form.on("Trainee Table", {
// 	amount: function(frm,cdt,cdn) {
//         calculate_grand_total(frm);
// 	},



// });
// function calculate_grand_total(frm){
//     let total = 0;
//     frm.doc.trainees.forEach (row => {
//         total+= row.amount;
//     });
//     frm.set_value('grand_total',total);
// }
