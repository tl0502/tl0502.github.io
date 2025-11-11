<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="<?php echo esc_url( get_template_directory_uri() . '/img/favicon.ico' ); ?>" />

    <?php if ( is_singular() && get_post_meta( get_queried_object_id(), '_yoast_wpseo_desc', true ) ) : ?>
        <meta name="description" content="<?php echo esc_attr( get_post_meta( get_queried_object_id(), '_yoast_wpseo_desc', true ) ); ?>">
    <?php else : ?>
        <meta name="description" content="<?php echo esc_attr( get_bloginfo( 'description' ) ); ?>">
    <?php endif; ?>

    <?php if ( is_singular() ) : ?>
        <link rel="canonical" href="<?php echo esc_url( get_permalink() ); ?>" />
    <?php else : ?>
        <link rel="canonical" href="<?php echo esc_url( home_url( add_query_arg( array(), $wp->request ) ) ); ?>" />
    <?php endif; ?>

    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?> ontouchstart="">

<?php get_template_part( 'nav' ); ?>

<div id="content" class="site-content">
