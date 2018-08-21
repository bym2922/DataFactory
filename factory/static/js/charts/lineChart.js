var myChart, option;
$(function () {
    myChart = echarts.init(document.getElementById('main'));
    option = {
        title: {
            text: '工厂销售情况',
            subtext: ''
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: []
        },
        toolbox: {
            show: true,
            feature: {
                mark: {
                    show: true
                },
                dataView: {
                    show: true,
                    readOnly: true
                },
                magicType: {
                    show: true,
                    type: ['line', 'bar', 'stack', 'tiled']
                },
                restore: {
                    show: true
                },
                saveAsImage: {
                    show: true
                }
            }
        },
        optionToContent: function (opt) {
            var axisData = opt.xAxis[0].data;
            var series = opt.series;
            var table =
                '<table style="width:100%;text-align:center" cellspacing="0" cellpadding="0" class="table_Qushi"><tbody><tr>' +
                '<td>时间</td>' +
                '<td>' + series[0].name + '</td>' +
                '<td>' + series[1].name + '</td>' +
                '<td>' + series[2].name + '</td>' +
                '<td>' + series[3].name + '</td>' +
                '<td>' + series[4].name + '</td>' +
                '</tr>';
            for (var i = 0, l = axisData.length; i < l; i++) {
                table += '<tr>' +
                    '<td>' + axisData[i] + '</td>' +
                    '<td>' + series[0].data[i] + '</td>' +
                    '<td>' + series[1].data[i] + '</td>' +
                    '<td>' + series[2].data[i] + '</td>' +
                    '<td>' + series[3].data[i] + '</td>' +
                    '<td>' + series[4].data[i] + '</td>' +
                    '</tr>';
            }
            table += '</tbody></table>';
            return table;
        },
        dataZoom: {
            id: 'dataZoomX',
            show: true, 
            backgroundColor: "rgba(47,69,84,0)", 
            type: 'slider',
            fillerColor: "rgba(167,183,204,0.4)", 
            borderColor: "#ddd", 
            filterMode: 'filter', 
            start: 0, 
            end: 100,
            startValue: 10,
            endValue: 100,
            orient: "horizontal", 
            zoomLock: false, 
            throttle: 100, 
            zoomOnMouseWheel: true,
            moveOnMouseMove: true, 
            left: "center", 
            top: "bottom", 
            right: "auto",
            bottom: "auto",
        },
        xAxis: [{
            type: 'category',
            boundaryGap: false,
            data: [],
            axisLabel: {
                interval: 0, //横轴信息全部显示
                rotate: 30, //60度角倾斜显示
                formatter: function (val) {
                    //                                        return val.split("").join("\n"); //横轴信息文字竖直显示
                    return val;
                },
                textStyle: {
                    color: '#000',
                    align: 'center',
                    fontWeight: 'bold'
                }
            }
        }],
        yAxis: [],
        series: []
        //                myChart = require('echarts').init(document.getElementById('main'));
    };
    myChart.showLoading({
        //                    text : '数据获取中',
        effect: 'whirling'
    });
    getData();
});
//请求json
var fields,
    itemsMap,
    seriesItem,
    yAxis_arr = [];

function getData() {
    $.ajax({
        // url: 'http://192.168.1.177:8000/data/?fname=%E4%B9%A6%E6%AC%BE%E4%BF%A1%E6%81%AF.xls',
        url: 'http://192.168.1.177:8000/data/'+window.location.search,
        dataType: 'json',
        async: false,
        type: 'get',
        success: function (json) {
            //console.log(json.data);  
            fields = json.name;
            itemsMap = json.data;

            createEcharts(); //动态创建曲线图
            myChart.hideLoading();
            myChart.setOption(option);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {

            if (textStatus == 'parsererror') {

                alert('数据为空或者SQL语句错误！');
            }
            console.log(errorThrown);
        }
    });
}
/*
 * 动态创建曲线图
 */
function createEcharts() {
    //    series                
    for (var i = 1; i < fields.length; i++) {
        if (i == 1) {
            itemStyle = {
                normal: {
                    areaStyle: {
                        type: 'default'
                    }
                }
            };
        } else {
            itemStyle = {
                normal: {


                }
            };
        }
        option.legend.data.push(fields[i])
        //    legend
        seriesItem = {};
        seriesItem.name = fields[i];
        seriesItem.type = 'line';
        seriesItem.smooth = false;
        seriesItem.yAxisIndex = i - 1;
        seriesItem.itemStyle = itemStyle;
        seriesItem.data = [];
        for (var key in itemsMap) {
            seriesItem.data.push(itemsMap[key][i]);

        }



        //        填充默认显示曲线的数据
        option.series.push(seriesItem);
        //        option.series[0].type      = 'line';
        //        option.series[1].type      = 'bar';
        // yAxis    
        var yAxis_obj = {};
        yAxis_obj.type = 'value';
        // yAxis_obj.name = fields[i];
        yAxis_obj.show = true;
        yAxis_arr.push(yAxis_obj);
    }
    for (var j in itemsMap) {
        option.xAxis[0].data.push(itemsMap[j][0]);
    }
    option.yAxis = yAxis_arr;
}