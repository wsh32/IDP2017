var chart = null;


function add_data()	{
	var data = [];
	for (var i = 1950; i <= 2010; i += 5) {
		point = 3.9E136*Math.pow(2.71828,-0.154*i);
		console.log(point);
		data.push([i, point]);
	}

	var options = {
		pointStart: 10,
		name: "Cases of Measles",
		data: data,
		animation: {
			duration: 2000
		},
	};

	chart.addSeries(options);
}

$(document).ready(function() {
	var options = {
		chart: {
			renderTo: 'graph',
			marginRight: 20,
			zoomType: 'xy',
		},
		xAxis: {
			type: 'linear',
			title: {
				text: 'Year',
			},
			softMin: 1950,
			softMax: 2010,
		},
		yAxis: {
			title: {
				text: 'Number of cases',
			},
			floor: 0,
			min: 0,
			max: 1500000,
		},
		credits: {
			enabled: false,
		},
		title: {
			text: 'Cases of Measles in the United States',
		},
		tooltip: {
			headerFormat: '<span style="font-size: 10px">{point.key} Cases</span><br/>',
			valueDecimals: 0,
			valueSuffix: ' cases',
		},
		plotOptions: {
			line: {
				marker: {
					enabled: false
				}
			}
		},
	}

	chart = new Highcharts.Chart(options);

	$('.show').hide();

	$('#data').on('click', function()	{
		add_data();
		$('.show').show();
		$('#data').hide();
	});
});