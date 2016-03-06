$(document).ready(function() {
    $("nav a").click(function() {
        $("nav a").removeClass("selected");
        $(this).addClass("selected");
    });
});