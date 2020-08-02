var $objHead = $( 'head' );

// define a function to disable zooming
var zoomDisable = function() {
    $objHead.find( 'meta[name=viewport]' ).remove();
    $objHead.prepend( '<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0" />' );
};

// ... and another to re-enable it
var zoomEnable = function() {
    $objHead.find( 'meta[name=viewport]' ).remove();
    $objHead.prepend( '<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=1" />');
};

// if the device is an iProduct, apply the fix whenever the users touches an input
if( navigator.userAgent.length && /iPhone|iPad|iPod/i.test( navigator.userAgent ) ) {
    // define as many target fields as your like
    $( ".search-form input, .contact-form input" )
        .on( { 'touchstart' : function() { zoomDisable() } } )
        .on( { 'touchend' : function() { setTimeout( zoomEnable , 500 ) } } );
}