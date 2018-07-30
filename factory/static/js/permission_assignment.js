
$('#increase').click(function () {
    $('#box').show();
    $('#cover').show();
})


$("#cancel").click(function () {
    $('#box').hide();
    $('#cover').hide();
})


$(".editor").click(function () {
    $('#box').show();
    $('#cover').show();
})


function addList() {
    var userName = document.getElementById("userName").value;
    var options = $("#permission option:selected").val();
    var description = document.getElementById("text_description").value;
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
    oInput2.setAttribute('onclick', 'del(this)');
    oInput2.className = 'am-btn am-btn-default am-btn-xs am-text-danger';
    oInput3.setAttribute('type', 'button');
    oInput3.setAttribute('value', '修改');
    oInput3.setAttribute('onclick', 'modify_New(this)');
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


function dell(obj) {
    var oParentnode = obj.parentNode.parentNode.parentNode.parentNode;
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
    var oId = document.getElementById('idIput');
    var oUser = document.getElementById('userName');
    var oPermission = document.getElementById('permission');
    var oDescription = document.getElementById('text_description');
    var oTr = obj.parentNode.parentNode.parentNode.parentNode;
    var aTd = oTr.getElementsByTagName('td');
    rowIndex = obj.parentNode.parentNode.parentNode.parentNode.rowIndex;
    oId.value = aTd[1].innerHTML;
    oUser.value = aTd[2].innerHTML;
    oPermission.value = aTd[3].innerHTML;
    oDescription.value = aTd[4].innerHTML;
    //alert(i);
    $('#box').show();
    $('#cover').show();
    $('#confirm').attr("disabled", true);
}


//更新功能
function update() {
    var oId = document.getElementById('idIput');
    var oUser = document.getElementById('userName');
    var oPermission = document.getElementById('permission');
    var oDescription = document.getElementById('text_description');
    var oMytable = document.getElementById('mytable');
    //alert(rowIndex);
    //var aTd = rowIndex.cells;
    console.log(oMytable.rows[rowIndex].cells)
    oMytable.rows[rowIndex].cells[1].innerHTML = oId.value;
    oMytable.rows[rowIndex].cells[2].innerHTML = oUser.value;
    oMytable.rows[rowIndex].cells[3].innerHTML = oPermission.value;
    oMytable.rows[rowIndex].cells[4].innerHTML = oDescription.value;
    $('#box').hide();
    $('#cover').hide();
}

//新增按钮修改功能
function modify_New(obj) {
    var oId = document.getElementById('idIput');
    var oUser = document.getElementById('userName');
    var oPermission = document.getElementById('permission');
    var oDescription = document.getElementById('text_description');
    var oTr = obj.parentNode.parentNode;
    var aTd = oTr.getElementsByTagName('td');
    rowIndex = obj.parentNode.parentNode.rowIndex;
    oId.value = aTd[1].innerHTML;
    oUser.value = aTd[2].innerHTML;
    oPermission.value = aTd[3].innerHTML;
    oDescription.value = aTd[4].innerHTML;
    //alert(i);
    $('#box').show();
    $('#cover').show();

}