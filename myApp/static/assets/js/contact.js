jQuery(document).ready(function () {
    jQuery('#contact-form').on('submit', function (e) {
        e.preventDefault(); // Prevent default form submission

        // AJAX request to Django endpoint
        jQuery.ajax({
            url: '/contact/', // Correct endpoint
            type: 'POST',
            data: jQuery(this).serialize(),
            headers: {
                'X-CSRFToken': jQuery('[name=csrfmiddlewaretoken]').val(), // CSRF token
            },
            success: function (data) {
                swal({
                    title: "Thank You!",
                    text: "Your request has been submitted successfully.",
                    icon: "success",
                    timer: 3000,
                    buttons: false,
                }).then(function () {
                    jQuery('#contact-form')[0].reset(); // Reset form
                });
            },
            error: function () {
                swal({
                    title: "Oops...",
                    text: "Something went wrong. Please try again.",
                    icon: "error",
                    timer: 3000,
                    buttons: false,
                });
            },
        });
    });
});
