$('body').scrollspy({ target: '.sidebar' });
$('ul.nav li a').bind('click', function(e) {
  e.preventDefault();
  $('html,body').animate({scrollTop: $(this.hash).offset().top});
});