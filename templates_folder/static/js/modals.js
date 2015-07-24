/**
 * Created by jesuscc29 on 19/07/15.
 */

showErrorAlert = function (title, message) {
    var $error = $("#error-modal");
    $error.find(".modal-title").text(title);
    $error.find(".modal-body").find("p").text(message);
    $error.modal("show");
};

showConfirmAlert = function (title, message) {
    var $error = $("#confirm-modal");
    $error.find(".modal-title").text(title);
    $error.find(".modal-body").find("p").text(message);
    $error.modal("show");
};
