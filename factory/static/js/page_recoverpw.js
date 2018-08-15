<!--向后台通过ajax发送手机号码数据-->
$('#forcode').click(function () {
    $.ajax({
        cache:false,
        type:"POST",
        url:"{% url 'user:forcode' %}",
        data:{
           csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val(),
           mobile:$("#mobile").val()
        },
        async:true,
        success:function (data) {
            alert(data)
        }
    })
})

// 发送按钮倒计时代码
var countdown=60;
function settime(obj) {
    if (countdown == 0) {
        obj.removeAttribute("disabled");
        obj.value="免费获取验证码";
        countdown = 60;
        return;
    } else {
        obj.setAttribute("disabled", true);
        obj.value="重新发送(" + countdown + ")";
        countdown--;
    }
setTimeout(function() {
    settime(obj) }
    ,1000)
}