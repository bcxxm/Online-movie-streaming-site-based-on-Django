$(function(){
    $("#item li a").each(function(){
    if($($(this))[0].href==String(window.location))
        $(this).addClass('active')
	})
    // $("#item li").each(function (i) {
    //       $(this).eq(i).click(function () {
    //           $(this).addClass("active")
    //       })
    //     }
    //
    // )
});
