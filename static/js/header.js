(function($) {
  "use strict"; // Start of use strict

  // Start midnight
  $(document).ready(function() {
    // Change this to the correct selector for your nav.
    $('.nav-toggler').midnight();
  });

  $(".hamburger").click(function(e) {
    e.preventDefault();
    $(".hamburger").toggleClass("is-active");
    $(".nav-menu").toggleClass("show");
    $("body").toggleClass("nav-open");
    // Other Stuff
  });

})(jQuery); // End of use strict