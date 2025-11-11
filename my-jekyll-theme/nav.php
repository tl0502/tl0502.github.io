<!-- Navigation (converted from _includes/nav.html) -->
<nav class="navbar navbar-default navbar-custom navbar-fixed-top">
    <div class="container-fluid">
        <div class="navbar-header page-scroll">
            <button type="button" class="navbar-toggle"> 
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php bloginfo('name'); ?></a>
        </div>

        <div id="huxblog_navbar">
            <div class="navbar-collapse">
                <?php
                // Primary menu (fall back to pages if no menu)
                if ( has_nav_menu( 'primary' ) ) {
                    wp_nav_menu( array(
                        'theme_location' => 'primary',
                        'container' => false,
                        'menu_class' => 'nav navbar-nav navbar-right'
                    ) );
                } else {
                    wp_page_menu( array( 'menu_class' => 'nav navbar-nav navbar-right' ) );
                }
                ?>
            </div>
        </div>
    </div>
</nav>

<script>
    // Minimal port of navigation toggle from original theme
    (function(){
        var $toggle = document.querySelector('.navbar-toggle');
        var $navbar = document.querySelector('#huxblog_navbar');
        var $collapse = document.querySelector('.navbar-collapse');
        if(!$toggle) return;
        $toggle.addEventListener('click', function(){
            if ($navbar.className.indexOf('in') > 0) {
                $navbar.className = " ";
                setTimeout(function(){
                    if($navbar.className.indexOf('in') < 0) {
                        $collapse.style.height = "0px";
                    }
                },400)
            } else {
                $collapse.style.height = "auto";
                $navbar.className += " in";
            }
        });
    })();
</script>
