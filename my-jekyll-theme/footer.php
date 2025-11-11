    </div><!-- #content -->

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <ul class="list-inline text-center">
                        <?php if ( get_option('rss_use') || true ) : ?>
                        <li>
                            <a href="<?php echo esc_url( home_url( '/feed.xml' ) ); ?>">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-circle fa-stack-2x"></i>
                                    <i class="fa fa-rss fa-stack-1x fa-inverse"></i>
                                </span>
                            </a>
                        </li>
                        <?php endif; ?>
                        <!-- Additional social links can be added via menu/widgets or theme options -->
                    </ul>
                    <p class="copyright text-muted">
                        &copy; <?php echo date('Y'); ?> <?php bloginfo('name'); ?>
                        <br>
                        Theme by <a href="http://huangxuan.me">Hux</a>
                    </p>
                </div>
            </div>
        </div>
    </footer>

    <?php // All scripts are enqueued via functions.php and printed by wp_footer() ?>

    <?php wp_footer(); ?>
</body>
</html>
