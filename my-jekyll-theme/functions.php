<?php
/**
 * Theme functions for My Jekyll Theme
 */

if ( ! function_exists( 'mjt_setup' ) ) :
    function mjt_setup() {
        add_theme_support( 'title-tag' );
        add_theme_support( 'post-thumbnails' );
        add_theme_support( 'automatic-feed-links' );
        add_theme_support( 'html5', array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption' ) );
        register_nav_menus( array(
            'primary' => __( 'Primary Menu', 'my-jekyll-theme' ),
        ) );
    }
endif;
add_action( 'after_setup_theme', 'mjt_setup' );

function mjt_enqueue_scripts() {
    // These files are expected to be copied into the theme's css/ and js/ folders.
    wp_enqueue_style( 'mjt-bootstrap', get_template_directory_uri() . '/css/bootstrap.min.css', array(), '3.3.7' );
    wp_enqueue_style( 'mjt-hux', get_template_directory_uri() . '/css/hux-blog.min.css', array('mjt-bootstrap'), filemtime( get_template_directory() . '/css/hux-blog.min.css' ) );
    wp_enqueue_style( 'mjt-syntax', get_template_directory_uri() . '/css/syntax.css', array('mjt-hux'), filemtime( get_template_directory() . '/css/syntax.css' ) );

    // use WP built-in jQuery
    wp_enqueue_script( 'jquery' );
    wp_enqueue_script( 'mjt-bootstrap-js', get_template_directory_uri() . '/js/bootstrap.min.js', array('jquery'), null, true );
    wp_enqueue_script( 'mjt-hux-js', get_template_directory_uri() . '/js/hux-blog.min.js', array('jquery','mjt-bootstrap-js'), null, true );
}
add_action( 'wp_enqueue_scripts', 'mjt_enqueue_scripts' );

// Register sidebar
function mjt_widgets_init() {
    register_sidebar( array(
        'name'          => __( 'Primary Sidebar', 'my-jekyll-theme' ),
        'id'            => 'primary-sidebar',
        'description'   => __( 'Main sidebar that appears on posts and pages.', 'my-jekyll-theme' ),
        'before_widget' => '<div id="%1$s" class="widget %2$s">',
        'after_widget'  => '</div>',
        'before_title'  => '<h3 class="widget-title">',
        'after_title'   => '</h3>',
    ) );
}
add_action( 'widgets_init', 'mjt_widgets_init' );

?>

<?php
// Open Graph meta for social sharing (basic)
function mjt_print_og_tags() {
    if ( is_singular() ) {
        global $post;
        $title = get_the_title( $post );
        $desc = has_excerpt( $post ) ? get_the_excerpt( $post ) : get_bloginfo( 'description' );
        $url = get_permalink( $post );
        $image = '';
        if ( has_post_thumbnail( $post ) ) {
            $image = get_the_post_thumbnail_url( $post, 'full' );
        }
        echo "<meta property=\"og:site_name\" content=\"" . esc_attr( get_bloginfo( 'name' ) ) . "\" />\n";
        echo "<meta property=\"og:title\" content=\"" . esc_attr( $title ) . "\" />\n";
        echo "<meta property=\"og:description\" content=\"" . esc_attr( wp_strip_all_tags( $desc ) ) . "\" />\n";
        echo "<meta property=\"og:url\" content=\"" . esc_url( $url ) . "\" />\n";
        echo "<meta property=\"og:type\" content=\"article\" />\n";
        if ( $image ) {
            echo "<meta property=\"og:image\" content=\"" . esc_url( $image ) . "\" />\n";
        }
    } else {
        echo "<meta property=\"og:site_name\" content=\"" . esc_attr( get_bloginfo( 'name' ) ) . "\" />\n";
        echo "<meta property=\"og:title\" content=\"" . esc_attr( get_bloginfo( 'name' ) ) . "\" />\n";
        echo "<meta property=\"og:description\" content=\"" . esc_attr( get_bloginfo( 'description' ) ) . "\" />\n";
        echo "<meta property=\"og:type\" content=\"website\" />\n";
        echo "<meta property=\"og:url\" content=\"" . esc_url( home_url() ) . "\" />\n";
    }
}
add_action( 'wp_head', 'mjt_print_og_tags', 5 );
