if (!$) {
    $ = django.jQuery;
}

$(function (){
    const selectField = $('#id_customer_type'),
        company_fields = $('.company-atr'),
        individual_fields = $('.individual-atr'),
        origin = $('#id_origin');
        origin.hide();


    function checkCustomerType(customer_type) {
    console.log(customer_type);


    if (customer_type === 'individual') {
        company_fields.hide();
        individual_fields.show();
    }

    if (customer_type === 'company') {
        company_fields.show();
        individual_fields.hide();
    }
}

checkCustomerType(selectField.val());
selectField.change(function() {
            checkCustomerType($(this).val());
        });




})


$(document).ready(function(){
    $('select').formSelect();
  });
