var count = 0;
var second = 0;
var up_open = 0;
var down_open = 0;
$(".sidebar-dropdown > a").click(function() {
    $(".sidebar-submenu").slideUp(200);

    if ((
            $(this)
            .parent()
            .hasClass("active")
        ) && (count >= 1)) {

        $(".sidebar-dropdown").removeClass("active");
        $(this)
            .parent()
            .removeClass("active");
        second = 0;
        $('#main-wrapper[data-layout=vertical] .left-sidebar[data-sidebarbg=skin6] .sidebar-nav ul .sidebar-item .sidebar-link').css("transform", "translateY(0)")
        $('.sidebar-menu-Admins').css("transform", "translateY(0)")
        if(down_open){
            $(".left-sidebar-add-user").css("transform", "translateY(80px)")
        }else{
            $(".left-sidebar-add-user").css("transform", "translateY(0px)")
        }
    } else {
        second = 1;
        $('#main-wrapper[data-layout=vertical] .left-sidebar[data-sidebarbg=skin6] .sidebar-nav ul .sidebar-item .sidebar-link').css("transform", "translateY(100px)")
        $('.sidebar-menu-Admins').css("transform", "translateY(110px)")
        if (up_open){
            $('.left-sidebar-add-user').css("transform", "translateY(200px)")
        }else{
            $('.left-sidebar-add-user').css("transform", "translateY(120px)")
        }
        $(".sidebar-dropdown").removeClass("active");
        $(this)
            .next(".sidebar-submenu")
            .slideDown(200);
        $(this)
            .parent()
            .addClass("active");
    }
    count = 1
});

// ################################################
var count2 = 0;
$(".sidebar-dropdown-Admins > a").click(function() {
    $(".sidebar-submenu-Admins").slideUp(50);

    if ((
            $(this)
            .parent()
            .hasClass("active")
        ) && (count2 >= 1)) {

        $(".sidebar-dropdown-Admins").removeClass("active");
        $(this)
            .parent()
            .removeClass("active");

        if (second >= 1)
        {
            up_open = 0;
            down_open = 0;
            $(".left-sidebar-add-user").css("transform", "translateY(120px)")
        }
        else{
            up_open = 0;
            down_open = 0;
            $(".left-sidebar-add-user").css("transform", "translateY(0px)")
        }

    }else {
        if (second >= 1){
            up_open = 1;
            down_open = 1;
            $(".left-sidebar-add-user").css("transform", "translateY(200px)")
        }
        else{
            up_open = 1;
            down_open = 1;
            $(".left-sidebar-add-user").css("transform", "translateY(80px)")

        }
        $(".sidebar-dropdown-Admins").removeClass("active");
        $(this)
            .next(".sidebar-submenu-Admins")
            .slideDown(50);
        $(this)
            .parent()
            .addClass("active");
    }
    count2 = 1
});




