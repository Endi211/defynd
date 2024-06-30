if (!$) {
    $ = django.jQuery;
}


$(function (){
    const selectField = $('#id_customer_type'),
        company_name_field = $('.field-company_name'),
        vat_number_field = $('.field-vat_number'),
        fiscal_code_field = $('.field-fiscal_code'),
        birth_place_field = $('.field-birth_place'),
        birthday_field = $('.field-birthday'),
        gender_field = $('.field-gender'),
        origin = $('.field-origin');
        origin.hide();

    $('.field-gender div div:first-child').hide();

    function checkCustomerType(customer_type) {
    console.log(customer_type);


    if (customer_type === 'individual') {
        birthday_field.show();
        birth_place_field.show();
        gender_field.show();
        company_name_field.hide();
        vat_number_field.hide();
        fiscal_code_field.hide();

    }

    if (customer_type === 'company') {
        company_name_field.show();
        vat_number_field.show();
        fiscal_code_field.show();
        birthday_field.hide();
        birth_place_field.hide();
        gender_field.hide();

    }
}

checkCustomerType(selectField.val());
selectField.change(function() {
            checkCustomerType($(this).val());
        });
});



