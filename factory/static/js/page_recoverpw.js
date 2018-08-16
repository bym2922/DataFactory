<!--向后台通过ajax发送手机号码数据-->
$('#forcode').click(function () {
    $.ajax({
        cache:false,
        type:"POST",
        url:"http://192.168.1.177:8000/forcode/",
        data:{
           "mobile":$("#mobile").val(),
        },
        dataType:"json",
        async:true,
        success:function (data) {
            alert(data)
        },
        error:function (error) {
            console.log(error)
        }
    })
})


// 发送按钮倒计时代码
var countdown=60;
function settime(obj) {
    if (countdown == 0) {
        obj.removeAttribute("disabled");
        obj.value="获取验证码";
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