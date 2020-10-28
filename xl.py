from openpyxl import Workbook
wb = Workbook()

ws = wb.active

ws.append([1, 2, 3])
ws.append([1, 2, 3])
wb.save('test.xlsx')