$(function() {
  // Create the chart
  $('#WeatherPi').highcharts({
    chart: {
      type: 'line'
    },
    title: {
      text: 'Temperature & Humidity'
    },

    yAxis: {
      title: {
        text: ''
      },
      labels: {
        formatter: function() {
          return this.value
        }
      }
    },
    xAxis: {
      title: {
        text: 'Time'
      }
    },

    tooltip: {
      crosshairs: true,
      shared: true
    },

    legend: {},

    data: {
      googleSpreadsheetKey: '1OAp-5DWuWQ2_r6OJcZVBapAF2mAg0BQ3TXlCFpwIXZ0',
      startColumn: 0,
      endColumn: 2
    },
    series: [
      {
        type: 'line',
        marker: {
          symbol: 'circle'
        },
        color: '#56ccf2',
        tooltip: {
          valueSuffix: ' °F'
        }
      },
      {
        name: 'Humidity',
        type: 'line',
        color: '#B81324',
        marker: {
          symbol: 'circle'
        },
        tooltip: {
          valueSuffix: ' %'
        }
      }
    ]
  })
})
