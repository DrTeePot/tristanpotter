/**
 * Created by tristanpotter on 2014-06-07.
 */

$(document).ready(function(){
    "use strict";
    var console = window.console;

    var carouselMain = $('#carousel');
    var carousel = {
        width: carouselMain.outerWidth(),
        height: carouselMain.outerHeight()
    };
    var carouselInner = $('#carousel-inner');

    var carouselItems = carouselInner.find('li');

    $('.carousel-image').width(carousel.width).height(carousel.height);
    carouselInner.css('left', -carousel.width);

    // First we need to move the last item to before the first item

    // When the user clicks button for sliding right:
    $('#prev').on('click', function(){
        var first = carouselInner.find('li:first');
        var last = carouselInner.find('li:last');

        // get the width of an item
        var itemWidth = first.outerWidth();
        console.log("itemWidth: " + itemWidth);

        // new left indent
        var left = parseFloat(carouselInner.css('left')) - itemWidth;

        carouselInner.animate({'left': left}, {queue: false, duration: 500},
            function(){
                carouselInner.css('left', -carousel.width);
            });

        // put the first item
        first.before(last);
        console.log('prev');
    });

    // When the user clicks the button for sliding left:
    $('#next').on('click', function(){
        var first = carouselInner.find('li:first');
        var last = carouselInner.find('li:last');

        // get the width of an item
        var itemWidth = first.outerWidth();
        console.log("itemWidth: " + itemWidth);

        // new left indent
        var left = parseInt(carouselInner.css('left')) - itemWidth;

        carouselInner.animate({'left': left}, {queue: false, duration: 500},
            function(){
                first.before(last);
                carouselInner.css('left', -carousel.width);
            });

        // put the first item
        first.before(last);
        console.log('next');
    });

});
