from openpyxl import workbook

wb = workbook.Workbook()
ws = wb.active
for i in range(400000):
    print(i)
    data = list(range(100))
    ws.append(data)
wb.save('/tmp/a.xlsx')