$(document).ready(function() {
    $('.copy').click(function() {

        let id = '#' + 'quote' + $(this).attr('id').slice(4);

        let temp = document.createElement('input');
        temp.setAttribute('value', $(id).find($('.quote')).text());
        document.body.appendChild(temp);
        temp.select();

        document.execCommand("copy");

        document.body.removeChild(temp);

    });
});