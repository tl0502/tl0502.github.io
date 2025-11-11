<aside id="secondary" class="widget-area">
    <?php if ( is_active_sidebar( 'primary-sidebar' ) ) : ?>
        <?php dynamic_sidebar( 'primary-sidebar' ); ?>
    <?php else : ?>
        <aside id="sidebar" class="widget-area" role="complementary">
            <section class="widget">
                <h3 class="widget-title">About</h3>
                <p>This is a fallback about text. Replace me in Appearance → Widgets.</p>
            </section>
            <section class="widget">
                <h3 class="widget-title">Search</h3>
                <?php get_search_form(); ?>
            </section>
            <section class="widget">
                <h3 class="widget-title">Recent Posts</h3>
                <ul>
                    <?php
                    $recent_posts = wp_get_recent_posts(array('numberposts' => 5));
                    foreach( $recent_posts as $post_item ) : ?>
                        <li><a href="<?php echo get_permalink($post_item['ID']); ?>"><?php echo esc_html($post_item['post_title']); ?></a></li>
                    <?php endforeach; wp_reset_query(); ?>
                </ul>
            </section>
            <section class="widget">
                <h3 class="widget-title">Tags</h3>
                <div class="tag-cloud">
                    <?php wp_tag_cloud(array('smallest' => 12, 'largest' => 18, 'unit' => 'px')); ?>
                </div>
            </section>
        </aside>
    <?php endif; ?>
</aside>
