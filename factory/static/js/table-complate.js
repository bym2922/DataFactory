$(function() {
    $("#selectAll").click(function() {
        $(":checkbox[name='ids']").prop("checked", this.checked); // this指代的你当前选择的这个元素的JS对象
    });
});