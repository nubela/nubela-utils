$(document).ready ->
    $("#rsvp-yes").on "click", ->
        $("#rsvp-val").val("y")
        $("#rsvp-form").submit()

    $("#rsvp-no").on "click", ->
        $("#rsvp-val").val("n")
        $("#rsvp-form").submit()

    $("#rsvp-form").on "keyup keypress", (e) ->
        if e.keyCode == 13
            e.preventDefault()
            return false

