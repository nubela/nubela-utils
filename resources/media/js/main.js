// Generated by IcedCoffeeScript 1.8.0-c
(function() {
  $(document).ready(function() {
    $("#rsvp-yes").on("click", function() {
      $("#rsvp-val").val("y");
      return $("#rsvp-form").submit();
    });
    $("#rsvp-no").on("click", function() {
      $("#rsvp-val").val("n");
      return $("#rsvp-form").submit();
    });
    return $("#rsvp-form").on("keyup keypress", function(e) {
      if (e.keyCode === 13) {
        e.preventDefault();
        return false;
      }
    });
  });

}).call(this);
