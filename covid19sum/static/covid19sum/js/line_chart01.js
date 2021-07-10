/**
 * 累計データを表示する線グラフを描画する
 */
$(window).on('load', function() {
  var data = {
    labels: covid_data.labels,
    datasets: [
    {
      label: covid_data.area_jp.title,
      data: covid_data.area_jp.data,
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      yAxisID: 'y',
    },{
      label: covid_data.area.title,
      data: covid_data.area.data,
      borderColor: 'rgb(54, 162, 235)',
      backgroundColor: 'rgb(54, 162, 235, 0.5)',
      yAxisID: 'y2',
    }]
  };

  var ctx = $('#chart01');
  var myLineChart = new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: covid_data.graph_title,
        }
      },
      scales: {
        y: {
          type: 'linear',   // linear固定 
          position: 'left',
          //beginAtZero: true,
          //max: 1000000,
          ticks: {
            color: 'rgb(255, 99, 132)',
          },
        },
        y2: {
          type: 'linear', 
          position: 'right',
          //beginAtZero: true,
          //max: 50000,
          grid: {
            display: false
          },
          ticks: {
            color: 'rgb(54, 162, 235)',
          },
        },
      }
    },
  });
});