/**
 * Created by tristanpotter on 2014-06-07.
 */

$(document).ready(function(){
    "use strict";
    var console = window.console;

    var carouselMain = $('#carousel');
    var carouselInner = $('#carousel-inner');

    var carousel = {
        width: carouselMain.outerWidth(),
        height: carouselMain.outerHeight()
    };


    var on_resize = function(){
        $('.carousel-image').width(carousel.width).height(carousel.height);
        $('.carousel-desc').width(carousel.width);
//        carouselInner.find('li').width(carousel.width).height(carousel.height);
        carouselInner.css('left', -carousel.width);
        carousel = {
            width: carouselMain.outerWidth(),
            height: carouselMain.outerHeight()
        };
    };

    on_resize();

    $( window ).resize(on_resize);

    // When the user clicks button for sliding right:
    $('#prev').on('click', function(){
        var first = carouselInner.find('li:first');
        var last = carouselInner.find('li:last');

        // get the width of an item
        var itemWidth = first.outerWidth();
        console.log("itemWidth: " + itemWidth);

        // new left indent
        var left = parseFloat(carouselInner.css('left')) + itemWidth;

        carouselInner.animate({'left': left}, {queue: false, duration: 500,
            complete: function(){
                carouselInner.css('left', -carousel.width);
                // put the first item
                first.before(last);
            }});
    });

    // When the user clicks the button for sliding left:
    $('#next').on('click', function(){
        var first = carouselInner.find('li:first');
        var last = carouselInner.find('li:last');

        // get the width of an item
        var itemWidth = first.outerWidth();
        console.log("itemWidth: " + itemWidth);

        // new left indent
        var left = parseFloat(carouselInner.css('left')) - itemWidth;

        carouselInner.animate({'left': left}, {queue: false, duration: 500,
            complete: function(){
                carouselInner.css('left', -carousel.width + 'px');
                // put the first item
                last.after(first);
            }});
    });

});
