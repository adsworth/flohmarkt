django.jQuery(".field-amount").focusout(function () {
  var total = 0;
  django.jQuery('.field-amount >:input[type="number"]').each(function () {
    var _val = django.jQuery(this).val();
    if (_val === "") {
      return;
    }

    var _betrag = parseFloat(django.jQuery(this).val(), 10);
    if (_betrag === NaN) {
      alert("Betrag" + _val + "ist keine Nummer");
    }

    total = total + _betrag;
  });
  var spans_total = django.jQuery('#totalAmount');
  if (spans_total.length === 0) {
    return;
  }
  spans_total[0].innerText = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR' }).format(total);
});