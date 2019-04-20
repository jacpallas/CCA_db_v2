$(function() {
  $inp = $("#prependedcheckbox");
  $cb = $("#checkbox_01");
  $inp.prop('disabled', true);

  $cb.on('change', function() {
    if ($cb.is(':checked')) {
      $inp.prop('disabled', false);
    } else {
      $inp.prop('disabled', true);
      $('input:text').val('');
    }
  });

});