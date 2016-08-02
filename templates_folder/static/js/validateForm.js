var validateForm = function ($form) {
    var is_valid = false;
    $form.find("input.required, select.required").each(function () {
        if ($(this).val() == "" || $(this).val() == 0) {
            $(this).parent().parent().addClass("has-error");
            is_valid = false;
        } else {
            $(this).parent().parent().removeClass("has-error");
            is_valid = true;
        }
    });
    return is_valid;
};