
var tweets = null;
var container = null;

function new_tweets() {
    var this_url = document.URL;
    $.ajax({
        type: "GET",
        url: this_url + '&ajax=true',
        success: function(html) {
            $('.container').replaceWith($(html));

        }
    });
}


$(document).ready(function() {
    //$('.container').empty();
    var count = 0;
    grams = $('.grams');
    function changeQuote() {
        setInterval(function(){
            new_tweets();
        }, 10000);
    }
    changeQuote();
});