/**
 * Created by jesuscc29 on 19/07/15.
 */

showErrorAlert = function (title, message) {
    var $error = $("#errorModal");
    $error.find(".modal-title").text(title);
    $error.find(".modal-body").find("p").text(message);
    $error.modal("show");
};

showConfirmAlert = function (title, message) {
    var $error = $("#confirmModal");
    $error.find(".modal-title").text(title);
    $error.find(".modal-body").find("p").text(message);
    $error.modal("show");
};
