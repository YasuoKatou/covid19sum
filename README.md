# Djangoで作るWebアプリケーション

## リリースするアプリケーション  

* 新型コロナウイルスの感染者数をグラフ化（[サンプルサイト](https://yk2021.pythonanywhere.com/covid19sum/)）

## 変更履歴  
* グラフの表示間隔を日毎と週間(期間は日毎の３倍)から選択可能にした（2021/7/16)  
* 最新のデータ日付から遡ってグラフ出力する（2021/7/14)  
* 日毎の感染者数を棒グラフで表示する場合、全国の表示を非表示にする（2021/7/12)  
* python-dateutilの利用を止める。pythonanywhereでimportエラーとなるため（2021/7/11)

## 参照データベース  

新型コロナウィルスのデータは、[covid19Data](https://github.com/YasuoKatou/covid19Data)プロジェクトを使用して登録する（このプロジェクトにDBは含まれていません）。


### グラフツール
[Chart.js](https://www.chartjs.org/)

