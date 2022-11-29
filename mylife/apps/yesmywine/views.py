from urllib import response
import webbrowser
from django.shortcuts import render
from django.views.generic import View

from django.http import HttpResponse
from openpyxl import Workbook, load_workbook
from tempfile import NamedTemporaryFile

def product_search(warehouse, ws1, ws2, ws3, ws4):
    i1 = 2
    invent = []
    warehouse = warehouse
    ws1 = ws1
    ws2 = ws2
    ws3 = ws3
    ws4 = ws4
    while(True):
        code = ws1.cell(i1,3).value
        if code == None:
            break

        number = section_search(code, warehouse, ws1, ws2, ws3, ws4)
        name = ws1.cell(i1, 2).value

        # 更新铂金库存
        if code=='PTXYA3536':
            max = 0
            max = bojin_search(code, warehouse, ws1, ws2, ws3, ws4)
            # 一瓶巴拿马 等于 20瓶麦克斯铂金
            number = number + max*20

        # 更新黑金库存
        if code=='PTXZA0065':
            max = 0
            max = bojin_search(code, warehouse, ws1, ws2, ws3, ws4)
            # 一瓶五粮液八代XMT 等于 4瓶麦克斯黑金
            number = number + max*4

        invent.append([name, code, number])
        i1 = i1 +1
        # print('prodect get:')
        # print(number)
    return(invent)


def section_search(code, warehouse, ws1, ws2, ws3, ws4):
    i2 = 2
    warehouse = warehouse
    ws1 = ws1
    ws2 = ws2
    ws3 = ws3
    ws4 = ws4
    while(True):
        section = ws2.cell(i2,1).value
        if section == None:
            break
        for x in range(3,7):
            section = ws2.cell(i2, x).value
            if section == code:
                number = 0
                for x in range(3,7):
                    check = ws2.cell(i2, x).value
                    if check != None:
                        x = erp_search(check, warehouse, ws1, ws2, ws3, ws4)
                        number = number + x
                # print('section return:')
                # print(number)
                return(number)

        i2 = i2 + 1


def erp_search(check, warehouse, ws1, ws2, ws3, ws4):
    i3 = 2
    number = 0
    warehouse = warehouse
    ws1 = ws1
    ws2 = ws2
    ws3 = ws3
    ws4 = ws4
    while(True):
        erp_section = ws3.cell(i3, 3).value
        if erp_section == None:
            break
        print('check is :'+check)
        print(erp_section)
        if erp_section == check and ws3.cell(i3, 1).value == warehouse:
            x = ws3.cell(i3, 9).value
            number = number + int(x)
            print(x)
        i3 = i3 + 1
        # print('erp return:')
        # print(number)
    return(number)

# 在第二张表搜索铂金库存
def bojin_search(code, warehouse, ws1, ws2, ws3, ws4):
    i = 3
    max = 0
    ws1 = ws1
    ws2 = ws2
    ws3 = ws3
    ws4 = ws4
    while(True):
        if ws4.cell(i, 2).value == warehouse and ws4.cell(i, 3).value == 'BJ18A0208':
            max = ws4.cell(i, 8).value
            return(max)
        if warehouse == '武汉总仓':
            if ws4.cell(i, 2).value == '武东分仓' and ws4.cell(i, 3).value == 'BJ18A0208':
                max = ws4.cell(i, 8).value
                return(max)
        if ws4.cell(i, 2).value == None:
            break
        i = i + 1
    return(max)
  
# 在第二张表搜索黑金库存
def bojin_search(code, warehouse, ws1, ws2, ws3, ws4):
    i = 3
    max = 0
    ws1 = ws1
    ws2 = ws2
    ws3 = ws3
    ws4 = ws4
    while(True):
        if ws4.cell(i, 2).value == warehouse and ws4.cell(i, 3).value == 'BJ21A0128':
            max = ws4.cell(i, 8).value
            return(max)
        if warehouse == '武汉总仓':
            if ws4.cell(i, 2).value == '武东分仓' and ws4.cell(i, 3).value == 'BJ21A0128':
                max = ws4.cell(i, 8).value
                return(max)
        if ws4.cell(i, 2).value == None:
            break
        i = i + 1
    return(max)

# Create your views here.
class InventView(View):
    def get(self, request):
        return render(request, 'yesmywine/invent.html')

    def post(self, request):
        danpin = request.FILES.get('danpin')
        kuanhao = request.FILES.get('kuanhao')
        kucun = request.FILES.get('kucun')
        try:
            if danpin is None:
                return HttpResponse('请选择要上传的文件')
            # 循环二进制写入
            wb1 = load_workbook(danpin)
            wb2 = load_workbook(kuanhao)
            wb3 = load_workbook(kucun)

            baishazhou = '武汉总仓'
            wansongyuan = '经济万松园店'
            ezhou = '仓储鄂州阳光货仓店'
            fuxin = '仓储富鑫常青店'
            sifang = '仓储肆方光谷店'
            binjiang = '仓储滨江国际店'

            ws1 = wb1.active
            ws2 = wb2.active
            ws3 = wb3.active
            ws4 = wb3.worksheets[1] # 抓取奔富麦克斯库存表格 

            print(request.POST)

            if 'baishazhou' in request.POST:
                name = baishazhou
            elif 'wansongyuan' in request.POST:
                name = wansongyuan
            elif 'ezhou' in request.POST:
                name = ezhou
            elif 'fuxin' in request.POST:
                name = fuxin
            elif 'sifang' in request.POST:
                name = sifang
            elif 'binjiang' in request.POST:
                name = binjiang
            invent = product_search(name, ws1, ws2, ws3, ws4)

            wb = Workbook()
            ws = wb.active

            x = 0
            for i in invent:
                ws.cell(x+2, 1).value = invent[x][0]
                ws.cell(x+2, 2).value = invent[x][1]
                ws.cell(x+2, 3).value = invent[x][2]
                x = x + 1

            with NamedTemporaryFile() as tmp:
                wb.save(tmp.name)
                tmp.seek(0)
                stream = tmp.read()
            response = HttpResponse(content=stream, content_type='application/ms-excel', )
            
            if name == baishazhou:
                name = 'baishazhou'
            elif name == wansongyuan:
                name = 'wansongyuan'
            elif name == ezhou:
                name = 'ezhou'
            elif name == fuxin:
                name = 'fuxin'
            elif name == sifang:
                name = 'sifang'
            elif name == binjiang:
                name = 'binjiang'
            
            s = f'attachment; filename={name}.xlsx'
            print(s)

            response['Content-Disposition'] = f'attachment; filename={name}.xlsx'
            return response
        except Exception as e:
            return HttpResponse(e)