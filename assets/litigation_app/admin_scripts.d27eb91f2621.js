
if (!$) {
    $ = django.jQuery;
}


$(function () {

    $('#id_EBIT, #id_EBIt_percentage, #id_residual_surface').attr("readonly", true);


    const origin = $('.field-origin'),
        date = $('.field-date'),
        descriptionField = $('.field-description'),
        mc_residui = $('.fieldBox.field-MC_residui');

    origin.hide();
    date.hide();
    descriptionField.hide();
    mc_residui.hide();

    $('input:radio[name="batch_disfiguration"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            descriptionField.show();
        } else {
            descriptionField.hide();
        }
    });

    $('input:radio[name="residual_airspace"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            mc_residui.show();
        } else {
            mc_residui.hide();
        }
    });

    var partialDemolition = $('.fieldBox.field-partial_demolition');
    partialDemolition.hide();
    $('input:radio[name="total_demolition"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            partialDemolition.hide();
        } else {
            partialDemolition.show();
        }
    });

    var contract_duration = $('.fieldBox.field-contract_duration');
    contract_duration.show();
    $('input:radio[name="lease_agreement"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            contract_duration.show();
        } else {
            contract_duration.hide();
        }
    });

    var reclamation_intervention_type = $('.fieldBox.field-reclamation_intervention_type');
    reclamation_intervention_type.hide();
    $('input:radio[name="reclamation_activities"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            reclamation_intervention_type.show();
        } else {
            reclamation_intervention_type.hide();
        }
    });



    $("body").on( "keyup",
            "#id_initial_estimation_value, #id_target_value, #id_total_cost, #id_final_value, #id_revenue," +
        "#id_surface_directly_concerned, #id_occupied_area, #id_epoch_construction, #id_contract_fee, #id_residual_rent, #id_above_ground_quantification",
            function( event ) {

			// When user select text in the document, also abort.
                const selection = window.getSelection().toString();
                if ( selection !== '' ) {
				return;
			}

			// When the arrow keys are pressed, abort.
			if ( $.inArray( event.keyCode, [38,40,37,39] ) !== -1 ) {
				return;
			}


                const $this = $(this);

                // Get the value.
                let input = $this.val();

                input = input.replace(/[\D\s_\-]+/g, "");
					input = input ? parseInt( input, 10 ) : 0;

					$this.val( function() {
						return ( input === 0 ) ? "" : input.toLocaleString( "en-US" );
					} );
		} );




        $("input").keyup(function(){

            const val1 = +$("#id_revenue").val().split(",").join("");
            const val2 = +$("#id_total_cost").val().split(",").join("");


            $("#id_EBIT").val(val1-val2);
            $('#id_EBIt_percentage').val((val1 - val2) / 100);



             const res_val1 = +$("#id_surface_directly_concerned").val();
             const res_val2 = +$("#id_occupied_area").val();
             $("#id_residual_surface").val(res_val1 - res_val2);

    });


   $('#id_fruit_pendants > div:nth-child(1)').hide();
   $('#id_batch_disfiguration > div:nth-child(1)').hide();
   $('#id_reception_act > div:nth-child(1)').hide();
   $('#id_purchase_contract > div:nth-child(1)').hide();
   $('#id_social_economic_reform > div:nth-child(1)').hide();
   $('#id_total_demolition > div:nth-child(1)').hide();
   $('#id_residual_airspace > div:nth-child(1)').hide();
   $('#id_storage_state > div:nth-child(1)').hide();
   $('#id_lease_agreement > div:nth-child(1)').hide();
   $('#id_productive_activities > div:nth-child(1)').hide();
   $('#id_need_transfer_user > div:nth-child(1)').hide();
   $('#id_reclamation_activities > div:nth-child(1)').hide();




   $('.form-row.field-surface_directly_concerned, .form-row.field-occupied_area, .form-row.field-residual_surface').append('<span class="meters"> m<sup>2</sup></span>')


});


