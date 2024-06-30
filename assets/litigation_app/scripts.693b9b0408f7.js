if (!$) {
    $ = django.jQuery;
}


$(function (){



   const origin = $('#id_origin');
        origin.hide();

    $('#id_residual_surface').attr("readonly", true);

   $("input").keyup(function(){
          const residualText = $('#residual-text');
       const val1 = +$("#id_surface_directly_concerned").val();
       const val2 = +$("#id_occupied_area").val();
       const result = $("#id_residual_surface").val(val1 - val2);

       if (result.val() < 0){
              result.addClass('is-invalid');
              residualText.text('Occupied Area can\'t be bigger than Concerned Area');
              residualText.removeClass('text-muted');
              residualText.addClass('text-danger');

          } else {
              result.removeClass('is-invalid');
              residualText.text('Residual Area');
              residualText.removeClass('text-danger');
              residualText.addClass('text-muted');
          }

    });

   $("body").on( "keyup",
            "#id_initial_estimation_value, #id_target_value, #id_total_cost, #id_final_value, #id_revenue, #id_enrollment_amount",
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

        $('#id_initial_estimation_value, #id_target_value, #id_total_cost, #id_final_value, #id_revenue,#id_surface_directly_concerned, #id_occupied_area').bind("cut copy paste",function(e) {
            e.preventDefault();
            });

        $("#id_surface_directly_concerned, #id_occupied_area").keypress(function (e){
             var charCode = (e.which) ? e.which : e.keyCode;
                if (charCode > 31 && (charCode < 48 || charCode > 57)) {
                return false;
  }
});


        $(document).ready(function() {
            const selectField = $('#id_registration_type'),
                agricultural_export = $('.reg-1'),
                exp_resi_industrial_building = $('.reg-2'),
                esp_fabb_residenziale = $('.reg-3');

            function checkRegistrationType(registration_type) {
                console.log(registration_type);

                if (registration_type === 'Esproprio Residenziale Libera' || registration_type === 'Esproprio Industriale Libera') {
                    exp_resi_industrial_building.show();
                    esp_fabb_residenziale.hide();
                    agricultural_export.hide();
                } else if (registration_type === 'Esproprio Agricolo') {
                    agricultural_export.show();
                    exp_resi_industrial_building.hide();
                    esp_fabb_residenziale.hide();
                } else if (registration_type === 'Esproprio Fabbricato Residenziale' || registration_type === 'Esproprio Fabbricato Industriale') {
                    exp_resi_industrial_building.hide();
                    agricultural_export.hide();
                    esp_fabb_residenziale.show();
                } else {
                    exp_resi_industrial_building.hide();
                    esp_fabb_residenziale.hide();
                    agricultural_export.hide();
                }
            }

            // Trigger the check on change
            selectField.on('change', function() {
                checkRegistrationType($(this).val());
            });

            // Initial check on page load
            checkRegistrationType(selectField.val());
        });





   $("#id_date_receipt_act, #id_contract_date").datepicker({
       dateFormat: "dd-mm-yy"
   });


   var partialDemolition = $('#field-partial_demolition');
    partialDemolition.hide();
    $('input:radio[name="total_demolition"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            partialDemolition.hide();
        } else {
            partialDemolition.show();
        }
    });


    var mc_residui = $('#field-mc_residui');
    mc_residui.hide();
    $('input:radio[name="residual_airspace"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            mc_residui.show();
        } else {
            mc_residui.hide();
        }
    });


    var contract_fields = $('#contract-fields');
    contract_fields.show();
    $('input:radio[name="lease_agreement"]').change(
    function(){
        if (this.checked && this.value === 'Yes') {
            contract_fields.show();
        } else {
            contract_fields.hide();
        }
    });





});



$(document).ready(function(){
    $('select').formSelect();
  });



















