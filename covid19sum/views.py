import datetime
import json
#from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from .models import DaillyPatients
from covid19sum.const.area import getAreaName, getAreaGroup

_DEFAULT_GRAPH_TYPE = 'line'
_DEFAULT_AREA_CODE = '400009'   # Fukuoka

def _getResponseBase(areaCode):
    return {'labels': [],
            'area_jp': {'title': '全国','data' : []},
            'area':    {'title': getAreaName(areaCode),'data' : []},
            'area_code': areaCode,
           }

def _getCovid19DataA(areaCode):
    v = _getResponseBase(areaCode)

    #データ取得期間
    d2 = DaillyPatients.getLastTargetDate()
    s2 = d2.strftime('%Y-%m-%d')
    #d1 = d2 - relativedelta(months=6)   # from (-6 month)
    d1 = d2 - datetime.timedelta(days=180)   # from (-6 month)
    s1 = d1.strftime('%Y-%m-%d')
    #全国データの取得
    gd1 = None
    gd2 = None
    data = []
    r  = DaillyPatients.objects.filter(Q(target_date__gt=s1) & Q(target_date__lte=s2) & Q(area_code='JP')).order_by('target_date')
    for d in r:
        if d.target_date.day == 1:
            v['labels'].append('%d/%d' % (d.target_date.month, d.target_date.day))
        else:
            v['labels'].append(str(d.target_date.day))
        data.append(d.patients)
        if not gd1:
            gd1 = d.target_date.strftime('%Y/%m/%d')
    v['area_jp']['data'] = data
    gd2 = list(r)[-1].target_date.strftime('%Y/%m/%d')
    v['graph_title'] = '累計感染者数 (%s - %s)' % (gd1, gd2, )
    #都道府県データの取得
    r  = DaillyPatients.objects.filter(Q(target_date__gt=s1) & Q(target_date__lte=s2) & Q(area_code=areaCode)).order_by('target_date')
    data = []
    for d in r:
        data.append(d.patients)
    v['area']['data'] = data

    return v

def _getCovid19DataB(areaCode):
    v = _getResponseBase(areaCode)

    #データ取得期間
    d2 = DaillyPatients.getLastTargetDate()
    s2 = d2.strftime('%Y-%m-%d')
    #d1 = d2 - relativedelta(months=3)   # from (-3 month)
    d1 = d2 - datetime.timedelta(days=90)   # from (-3 month)
    s1 = d1.strftime('%Y-%m-%d')
    #全国データの取得
    gd1 = None
    gd2 = None
    data1 = []
    r  = DaillyPatients.objects.filter(Q(target_date__gt=s1) & Q(target_date__lte=s2) & Q(area_code='JP')).order_by('target_date')
    wk = None
    for d in r:
        if not wk:
            wk = d.patients
            gd1 = d.target_date.strftime('%Y/%m/%d')
            continue
        if d.target_date.day == 1:
            v['labels'].append('%d/%d' % (d.target_date.month, d.target_date.day))
        else:
            v['labels'].append(str(d.target_date.day))
        wk = d.patients - wk
        data1.append(0 if wk < 0 else wk)
        wk = d.patients
    gd2 = list(r)[-1].target_date.strftime('%Y/%m/%d')
    v['graph_title'] = '日毎の新規感染者数 (%s - %s)' % (gd1, gd2, )
    #都道府県データの取得
    r  = DaillyPatients.objects.filter(Q(target_date__gt=s1) & Q(target_date__lte=s2) & Q(area_code=areaCode)).order_by('target_date')
    data2 = []
    wk = None
    for d in r:
        if not wk:
            wk = d.patients
            continue
        wk = d.patients - wk
        data2.append(0 if wk < 0 else wk)
        wk = d.patients
    v['area']['data'] = data2
    #全国のデータから都道府県のデータを引く
    for i, num in enumerate(data1):
        data1[i] = num - data2[i]
    v['area_jp']['data'] = data1

    return v

def _getAreaAll():
    return [{'title': '北海道・東北' , 'data' : getAreaGroup('01')},
            {'title': '関東'        , 'data' : getAreaGroup('02')},
            {'title': '中部'        , 'data' : getAreaGroup('03')},
            {'title': '近畿'        , 'data' : getAreaGroup('04')},
            {'title': '中国・四国'   , 'data' : getAreaGroup('05')},
            {'title': '九州・沖縄'   , 'data' : getAreaGroup('06')}]

def _getLineChartData(request):
    area_code = request.GET.get(key="area_code", default=_DEFAULT_AREA_CODE)
    graph_type = request.GET.get(key="graph_type", default=_DEFAULT_GRAPH_TYPE)
    return {'covid_data': json.dumps(_getCovid19DataA(area_code)),
            'graph_type' : graph_type,
            'area_code' : area_code,
            'area_all': _getAreaAll(),
           }

def _getBarChartData(request):
    area_code = request.GET.get(key="area_code", default=_DEFAULT_AREA_CODE)
    graph_type = request.GET.get(key="graph_type", default=_DEFAULT_GRAPH_TYPE)
    return {'covid_data': json.dumps(_getCovid19DataB(area_code)),
            'graph_type' : graph_type,
            'area_code' : area_code,
            'area_all': _getAreaAll(),
           }

def index(request):
    graph_type = request.GET.get(key="graph_type", default=_DEFAULT_GRAPH_TYPE)
    if graph_type == 'line':
        c = _getLineChartData(request)
    elif graph_type == 'bar':
        c = _getBarChartData(request)
    else:
        raise Http404("No graph type. (%s)" % (graph_type, ))

    return render(request, 'covid19sum/index.html', c)

#[EOF]