/* global tinymce */
/** Global admin object **/

$(document).ready(function($) {
    'use strict';
    $('.sortedm2m-items a').click(function(event) {
        event.preventDefault();
        $(this).prev('input').trigger('click');
    });
     
    $('.vTimeField').inputmask({
        mask: '99:99:99',
    });
    $('.vDateField').inputmask({
        mask: '9999-99-99',
    });

    /** datarange filter **/
    (function() {
        $('#changelist-filter input[type="reset"]').click(function(event) {
            event.preventDefault();
            var form = $(this).closest('form');
            form.attr('action', window.location.href);
            form.find('input[type="text"]').val('');
            form.submit();
        });
    }());

    /**
     * begin & end inputs
     */
    (function() {
        var begin = $('#id_begin_0'),
            end = $('#id_end_0');

        if (!begin.length || !end.length) {
            return;
        }

        begin.on('change, blur', function() {
            if (!end.val()) {
                end.val(begin.val());
            }
        });
    }());

    // admin filter select
    (function() {
        $('.admin-filter-select').change(function() {
            window.location.href =  $(this).val();
        });
    }());
});
