/*----------------------饼状图-----------------------*/
//环形图


(function () {

    function loadOneColumn() { 
        var pie1 = echarts.init(document.getElementById("pie1"));
        pie1.setOption({
            title: {
                text: "环形图",
                x: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                x: 'left',
                data: []
            },
            series: [{
                name: '访问来源',
                type: 'pie',
                radius: ['50%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    normal: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        show: true,
                        textStyle: {
                            fontSize: '30',
                            fontWeight: 'bold'
                        }
                    }
                },
                labelLine: {
                    normal: {
                        show: false
                    }
                },
                data: []
            }]
        });
        pie1.showLoading();
        var names = [];
        var brower = [];
        $.ajax({
            type: 'get',
            // url: 'http://192.168.1.177:8000/pie_data/?fname=%E4%B9%A6%E6%AC%BE%E4%BF%A1%E6%81%AF.xls', //请求数据的地址
            url:'http://192.168.1.177:8000/pie_data/'+window.location.search,
            dataType: "json", //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象
                $.each(result.list, function (index, item) {
                    names.push(item.Name); //挨个取出类别并填入类别数组 
                    brower.push({
                        name: item.Name,
                        value: item.Data
                    });
                });
                pie1.hideLoading(); //隐藏加载动画
                pie1.setOption({ //加载数据图表                
                    legend: {
                        data: names
                    },
                    series: [{
                        data: brower
                    }]
                });
            },
            error: function (errorMsg) {
                //请求失败时执行该函数
                alert("图表请求数据失败!");
                pie1.hideLoading();
            }
        });
    
     };
     loadOneColumn();

})();




(function () {
    function loadTwoColumn() {
        var pie2 = echarts.init(document.getElementById('pie2'));
        // 显示标题，图例和空的坐标轴
        pie2.setOption({
            title: {
                text: '销量',
                x: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                x: 'left',
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
                        readOnly: false
                    },
                    magicType: {
                        show: true,
                        type: ['pie', 'funnel'],
                        option: {
                            funnel: {
                                x: '25%',
                                width: '50%',
                                funnelAlign: 'left',
                                max: 1548
                            }
                        }
                    },
                    restore: {
                        show: true
                    },
                    saveAsImage: {
                        show: true
                    }
                }
            },
            series: [{
                name: '销量',
                type: 'pie',
                radius: '55%',
                center: ['50%', '60%'],
                data: []
            }]
        });
        pie2.showLoading(); //数据加载完之前先显示一段简单的loading动画
        var names = []; //类别数组（用于存放饼图的类别）
        var brower = [];
        $.ajax({
            type: 'get',
            // url: 'http://192.168.1.177:8000/pie_data/?fname=%E4%B9%A6%E6%AC%BE%E4%BF%A1%E6%81%AF.xls', //请求数据的地址
            url:'http://192.168.1.177:8000/pie_data/'+window.location.search,
            dataType: "json", //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象
                $.each(result.list, function (index, item) {
                    names.push(item.Name); //挨个取出类别并填入类别数组 
                    brower.push({
                        name: item.Name,
                        value: item.Data
                    });
                });
                pie2.hideLoading(); //隐藏加载动画
                pie2.setOption({ //加载数据图表                
                    legend: {
                        data: names
                    },
                    series: [{
                        data: brower
                    }]
                });
            },
            error: function (errorMsg) {
                //请求失败时执行该函数
                alert("图表请求数据失败!");
                pie2.hideLoading();
            }
        });
    };
    loadTwoColumn();
})()