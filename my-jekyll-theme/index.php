<?php get_header(); ?>

<div class="container">
    <div class="row">
        <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">

            <?php if ( have_posts() ) : while ( have_posts() ) : the_post(); ?>
                <div class="post-preview">
                    <a href="<?php the_permalink(); ?>">
                        <h2 class="post-title"><?php the_title(); ?></h2>
                        <div class="post-content-preview"><?php the_excerpt(); ?></div>
                    </a>
                    <p class="post-meta">Posted by <?php the_author_posts_link(); ?> on <?php the_date(); ?></p>
                </div>
                <hr />
            <?php endwhile; ?>

            <div class="pager">
                <?php
                echo paginate_links( array(
                    'prev_text' => '&larr; Newer Posts',
                    'next_text' => 'Older Posts &rarr;'
                ) );
                ?>
            </div>

            <?php else : ?>
                <p><?php _e( 'Sorry, no posts matched your criteria.', 'my-jekyll-theme' ); ?></p>
            <?php endif; ?>

        </div>
        <div class="col-md-4">
            <?php get_sidebar(); ?>
        </div>
    </div>
</div>

<?php get_footer(); ?>
