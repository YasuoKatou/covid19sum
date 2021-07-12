/**
 * 日毎の発生データを表示する棒グラフを描画する
 */
 $(window).on('load', function() {
  var data = {
    labels: covid_data.labels,
    datasets: [
    {
      label: covid_data.area.title,
      backgroundColor: 'rgb(54, 162, 235)',
      data: covid_data.area.data,
    },{
      label: covid_data.area_jp.title,
      data: covid_data.area_jp.data,
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      hidden: true,
    }]
  };

  var ctx = $('#chart01');
  var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
      plugins: {
        title: {
          display: true,
          text: covid_data.graph_title,
        },
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true
        }
      }
    }
  });
});