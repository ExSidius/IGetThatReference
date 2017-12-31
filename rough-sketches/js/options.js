$(document).ready(function() {
    $('.copy').click(function() {

        // console.log("banana");
        let id = '#' + $(this).attr('id').slice(0, -5);
        // console.log(id);

        let temp = document.createElement('input');
        temp.setAttribute('value', $(id).find($('.quote')).text());
        document.body.appendChild(temp);
        temp.select();

        document.execCommand("copy");

        document.body.removeChild(temp);

    });
});