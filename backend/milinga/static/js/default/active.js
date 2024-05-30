(function ($) {
    'use strict';

    var milingaWindow = $(window);

    // :: WOW Active Code
    if (milingaWindow.width() > 480) {
        new WOW().init();
    }

})(jQuery);


