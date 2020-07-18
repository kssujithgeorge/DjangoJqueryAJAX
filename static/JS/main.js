 /*
        On submiting the form, send the POST ajax
        request to server and after successfull submission
        display the object.
    */
   const form = document.getElementById('post-form');

$("#initial-form").submit(function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: 'appendData',
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#initial-form").trigger('reset');
                // 2. focus to nickname input
                $("#id_drop_down_1").focus();
        //        form.reset();

                // display the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];
                $("#dis-table tbody").prepend(
                    `<tr>
                    <td>${fields["form_id"]||""}</td>
                    <td>${fields["drop_down_1"]||""}</td>
                    <td>${fields["drop_down_2"]||""}</td>
                    <td>${fields["check_box_1"]||""}</td>
                    <td>${fields["Integer_box"]||""}</td>
                    <td>${fields["text_box"]||""}</td>
                    <td>${fields["dob"]||""}</td>
                    <td>${fields["new_check_box_1"]||""}</td>
                    <td>${fields["new_check_box_2"]||""}</td>
                    <td>${fields["new_check_box_A"]||""}</td>
                    <td>${fields["new_check_box_B"]||""}</td>
                    <td>${fields["new_check_box_C"]||""}</td>
                    <td>${fields["new_check_box_D"]||""}</td>
                    <td>${fields["integerbox_A"]||""}</td>
                    <td>${fields["integerbox_B"]||""}</td>
                    <td>${fields["integerbox_C"]||""}</td>
                    <td>${fields["integerbox_D"]||""}</td>
                    </tr>`
                )
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
})
//$("#id_form_id").focusout(function (e) {
//        e.preventDefault();
//        // get the nickname
//        var form_id = $(this).val();
//        // GET AJAX request
//        $.ajax({
//            type: 'GET',
//            url: 'validate_formid',
//            data: form_id,
//            success: function (response) {
//                // if not valid user, alert the user
//                if(!response["valid"]){
//                    alert("You cannot create a friend with same nick name");
//                    var formid = $("#id_form_id");
//                    formid.val("")
//                    formid.focus()
//                }
//            },
//            error: function (response) {
//                console.log(response)
//            }
//        })
//})
$("#fin-submit").click(function(event){
    event.preventDefault();
    $("#main-container").css("display", "none");
    $("#dis-container").css("display", "block");

});
$("#confirm").click(function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        console.log("Entered in savedata");
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: 'saveData',
            data: serializedData,
            success: function successFunction(msg) {
                if (msg.message === 'success'){
                alert ('form is submitted, Success!!');
                form.reset()
                }
            }
        });
});