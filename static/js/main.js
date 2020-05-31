$(function() {
    $(document).scroll(function() {
        var $nav = $("#homeNav");
        $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
    });
});