$(document).ready(function() {
    $('#latest-copy').click(function() {

        let temp = document.createElement('input');
        temp.setAttribute('value', $('#latest-quote').text());
        document.body.appendChild(temp);
        temp.select();

        document.execCommand("copy");

        document.body.removeChild(temp);
    });
});