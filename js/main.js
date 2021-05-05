    var fileButton = document.getElementById("fileButton");
    fileButton.addEventListener('change', function(e){
            var file = e.target.files[0];
            var storageRef = firebase.storage().ref(file.name);
            storageRef.put(file);
    });  
    // Your web app's Firebase configuration
    var firebaseConfig = {
        apiKey: "AIzaSyDC7HlzvfpCi1IBFcuzqVQkcvmSF84JHRw",
        authDomain: "hacksummit-8dbf3.firebaseapp.com",
        databaseURL: "https://hacksummit-8dbf3.firebaseio.com",
        projectId: "hacksummit-8dbf3",
        storageBucket: "",
        messagingSenderId: "630484404533",
        appId: "1:630484404533:web:f23d56efe383b8f8"
    };
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);

(function ($) {
    "use strict";

    /*==================================================================
    [ Validate after type ]*/
    $('.validate-input .input100').each(function(){
        $(this).on('blur', function(){
            if(validate(this) == false){
                showValidate(this);
            }
            else {
                $(this).parent().addClass('true-validate');
            }
        })    
    })
  
  
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
           $(this).parent().removeClass('true-validate');
        });
    });

     function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');

        $(thisAlert).append('<span class="btn-hide-validate">&#xf136;</span>')
        $('.btn-hide-validate').each(function(){
            $(this).on('click',function(){
               hideValidate(this);
            });
        });
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
        $(thisAlert).find('.btn-hide-validate').remove();
    }
    

})(jQuery);