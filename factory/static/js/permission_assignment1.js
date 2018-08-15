var count=1
$('#increase').click(function () {
    $('#box').show();
    $('#cover').show();
})//单击“新增”时打开弹出框1


$("#cancel").click(function () {
    $('#box').hide();
    $('#cover').hide();
})//单击“取消”时关闭弹出框1

$("#cancel1").click(function () {
    $('#box1').hide();
    $('#cover').hide();
})//单击“取消”时关闭弹出框2


$(".editor").click(function () {
    $('#box').show();
    $('#cover').show();
})//单击“编辑”时打开弹出框1

function addList() {
    count += 1;
    var userName = document.getElementById("userName").value;
    var options = $("#permission option:selected").val();
    var description = $("#permission1 option:selected").val();
    var oId = document.getElementById('idIput').value;
    
    var oTr = document.createElement('tr');
    var oTd1 = document.createElement('td');
    var oInput = document.createElement('input');
    oTd1.appendChild(oInput);
    oInput.setAttribute('type', 'checkbox');
    oInput.setAttribute('name', 'item');
    
    var oTd2 = document.createElement('td');
    oTd2.innerHTML = oId;
    var oTd3 = document.createElement('td');
    oTd3.innerHTML = userName;
    var oTd4 = document.createElement('td');
    oTd4.innerHTML = options;
    var oTd5 = document.createElement('td');
    oTd5.innerHTML = description;
    var oTd7 = document.createElement('td');
    var oInput2 = document.createElement('input');
    var oInput3 = document.createElement('input');
    oInput2.setAttribute('type', 'button');
    oInput2.setAttribute('value', '删除');
    oInput2.setAttribute('onclick', 'confirm_del(this)');
    oInput2.className = 'am-btn am-btn-default am-btn-xs am-text-danger';
    
    oInput3.setAttribute('type', 'button');
    oInput3.setAttribute('value', '修改');
    oInput3.setAttribute('onclick', 'modify(this)');
    oInput3.className = 'am-btn am-btn-default am-btn-xs am-text-secondary';
    oTd7.appendChild(oInput2);
    oTd7.appendChild(oInput3);
    oTr.appendChild(oTd1);
    oTr.appendChild(oTd2);
    oTr.appendChild(oTd3);
    oTr.appendChild(oTd4);
    oTr.appendChild(oTd5);
    oTr.appendChild(oTd7);
    var olistTable = document.getElementById('listTable');
    olistTable.appendChild(oTr);
    $('#box').hide();
    $('#cover').hide();
    var hang = $("#listTable").find("tr").length;
    $("#arrLength").html(hang);
    $('#update').attr("disabled", true);
}


function del(obj) {
    var oParentnode = obj.parentNode.parentNode;
    var olistTable = document.getElementById('listTable');
    olistTable.removeChild(oParentnode);
    var hang = $("#listTable").find("tr").length;
    $("#arrLength").html(hang);
}







function checkAll(c) {
    var status = c.checked;
    var oItems = document.getElementsByName('item');
    for (var i = 0; i < oItems.length; i++) {
        oItems[i].checked = status;
    }
}
//delAll功能
function delAll() {
    var olistTable = document.getElementById('listTable');
    var items = document.getElementsByName("item");
    for (var j = 0; j < items.length; j++) {
        if (items[j].checked) //如果item被选中
        {
            var oParentnode = items[j].parentNode.parentNode;
            olistTable.removeChild(oParentnode);
            j--;
        }
    }
    var hang = $("#listTable").find("tr").length;

    $("#arrLength").html(hang)
}

// 修改功能
function modify(obj) {
    var oUser = document.getElementById('userName');
    var oPermission = document.getElementById('permission');
    var oDescription = document.getElementById('permission1');
    var oTr = obj.parentNode.parentNode;
    var aTd = oTr.getElementsByTagName('td');
    rowIndex = obj.parentNode.parentNode.rowIndex;
    oUser.value = aTd[1].innerHTML;
    oPermission.value = aTd[2].innerHTML;
    oDescription.value = aTd[3].innerHTML;
    $('#box').show();
    $('#cover').show();
    $('#confirm').attr("disabled", false);
}

//删除功能（确认删除提示框）
function confirm_del(obj) {
    $('#box1').show();
    $('#cover').show();
    var ouser=document.getElementById("get_username");
    var oTr = obj.parentNode.parentNode;
    var aTd = oTr.getElementsByTagName('td');
    ouser.innerHTML = aTd[1].innerHTML;
    get_username1=document.getElementById("get_username1");
    get_username1.href='/delete_user?username='+aTd[1].innerHTML;
}



更新功能
function update(obj) {
    var oUser = document.getElementById('userName');
    var oPermission = document.getElementById('permission');
    get_username2=document.getElementById("get_username2");
    get_username2.href='/update_user?username='+oUser.value+'&power='+oPermission.value;
    $('#box').hide();
    $('#cover').hide();
}

// select二级联动
$('#permission').change(function(){
    var sValue = $("#permission").val()
    switch(sValue){
        case "1" : $("#permission1").html("<option selected='selected'>至高无上的权利1</option>").show();break;
        case "2" : $("#permission1").html("<option selected='selected'>至高无上的权利2</option>").show();break;
        case "3" : $("#permission1").html("<option selected='selected'>至高无上的权利3</option>").show();break;
        default : alert("erro");
    };
});
