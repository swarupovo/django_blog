// Class definition

var KTFormControls = function () {
    // Private functions
    
    var demo1 = function () {
        $( "#kt_form_1" ).validate({
            // define validation rules
            rules: {
                first_name:{
                    required: true,
                    minlength:2,
                },
                last_name:{
                    required: true,
                    minlength: 2,
                },
                email: {
                    required: true,
                    email: true,
//                    minlength: 10 ,
                },
                url: {
                    required: true ,

                },
                skype: {
                    required: true,
//                    minlength:4,

                },
                dob: {
                    required:true,
                    minlength:6

                },
                country: {
                    required:true,
                    minlength:3
                },
                city:{
                    required:true,
                    minlength:3
                },
                language :{
                    required:true,
                    minlength:3
                },
                image :{
                    image:true,
//                    required:true,

                },
                description:{
                    required:true,
                    minlength:4
                },
                position_limit:{
                    required:true,
                    number:true,
                },
                digits: {
                    required: true,
                    digits: true
                },
                creditcard: {
                    required: true,
                    creditcard: true 
                },
                phone_no: {
                    required: true,
//                    phoneUS: true,
//                    maxlength:11,
                    digits: true
                },
//                min_bid: {
//                    required: true,
//                    digits: true
//                },

                option: {
                    required: true
                },
                options: {
                    required: true,
                    minlength: 2,
                    maxlength: 4
                },
                memo: {
                    required: true,
                    minlength: 10,
                    maxlength: 100
                },

                checkbox: {
                    required: true
                },
                checkboxes: {
                    required: true,
                    minlength: 1,
                    maxlength: 2
                },
                radio: {
                    required: true
                },
                //addpositions validator
                name:{
                    required: true,
                    minlength:2,
                },
                author:{
                    required:true,
                    minlength:4,
                },
                description:{
                    required:true,
                    minlength:4
                },
                size:{
                    required:true,
                    minlength:1
                },
                //price validation
                price:{
                    required:true,
                    number:true,
                    minlength: 1
                },
                //auction validation add
                start_price:{
                    required:true,
                    number:true,
                    minlength:1
                },
                min_bid:{
                    required:true,
                    minlength:1,
                    digits: true
                },
                //category_add validation


            },
            
            //display error alert on form submit  
            invalidHandler: function(event, validator) {     
                var alert = $('#kt_form_1_msg');
                alert.removeClass('kt--hide').show();
                KTUtil.scrollTop();
            },

            submitHandler: function (form) {
                form[0].submit(); // submit the form
            }
        });       
    }

    var demo2 = function () {
        $( "#kt_form_2" ).validate({
            // define validation rules
            rules: {
                //= Client Information(step 3)
                // Billing Information
                billing_card_name: {
                    required: true
                },
                billing_card_number: {
                    required: true,
                    creditcard: true
                },
                billing_card_exp_month: {
                    required: true
                },
                billing_card_exp_year: {
                    required: true
                },
                billing_card_cvv: {
                    required: true,
                    minlength: 2,
                    maxlength: 3
                },

                // Billing Address
                billing_address_1: {
                    required: true
                },
                billing_address_2: {
                    
                },
                billing_city: {
                    required: true
                },
                billing_state: {
                    required: true
                },
                billing_zip: {
                    required: true,
                    number: true
                },

                billing_delivery: {
                    required: true
                }
            },
            
            //display error alert on form submit  
            invalidHandler: function(event, validator) {
                swal.fire({
                    "title": "", 
                    "text": "There are some errors in your submission. Please correct them.", 
                    "type": "error",
                    "confirmButtonClass": "btn btn-secondary",
                    "onClose": function(e) {
                        console.log('on close event fired!');
                    }
                });

                event.preventDefault();
            },

            submitHandler: function (form) {
                //form[0].submit(); // submit the form
                swal.fire({
                    "title": "", 
                    "text": "Form validation passed. All good!", 
                    "type": "success",
                    "confirmButtonClass": "btn btn-secondary"
                });

                return false;
            }
        });       
    }

    return {
        // public functions
        init: function() {
            demo1(); 
            demo2();
        }
    };
}();

jQuery(document).ready(function() {    
    KTFormControls.init();
});