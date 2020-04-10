$(function(){
    loadPersons();
});


function loadPersons(){
    $.getJSON("http://localhost:5000/", function(data) {
        var items = [];
        var count = 0;
        $.each( data, function( key, val ) {
            count ++;
            items.push(`<li class="list-group-item d-flex justify-content-between lh-condensed" onclick="editPerson('` + val.email + `')">
                <div>
                    <h6 class="my-0">` + val.name + `</h6>
                    <small class="text-muted">` + val.email + `</small>

                </div>
                <span class="text-muted">` + val.phone + `</span>
                <span class="glyphicon glyphicon-trash trash-pointer" aria-hidden="true" onclick="removePerson('` + val.email  + `')"></span>
            </li>`);
        });

        $('#persons').html(items.join(""));
        $('#total').text(count);
    });
}

$("form").submit(function(event){
    event.preventDefault();
    var person = {
        email: $("#email").val(),
        name: $("#name").val(),
        phone: $("#phone").val()
    };



    $.ajax({
        type: 'POST',
        url: 'http://localhost:5000/persons',
        contentType: 'application/json',
        data: JSON.stringify(person),
        dataType: 'json',
        success:  function(){
            loadPersons();
        }
    });

});

function removePerson(email){
    var removePersonUrl = 'http://localhost:5000/persons' + '/' + email;
    $.ajax({
        type: 'DELETE',
        url: removePersonUrl,
        contentType: 'application/json',
        dataType: 'json',
        success:  function(){
            loadPersons();
        }
    });
}

function editPerson(email){
    var emailPersonURL = 'http://localhost:5000/persons' + '/' + email;
    $.ajax({
        type: 'GET',
        url: emailPersonURL,
        contentType: 'application/json',
        dataType: 'json',
        success:  function(data){
           $("#name").val(data.name);
           $("#email").val(data.email);
           $("#phone").val(data.phone);
        }
    });
}