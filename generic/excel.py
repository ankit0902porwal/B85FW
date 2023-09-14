import openpyxl
class Excel:
    @staticmethod
    def get_cell_data(path, sheet, row, col):
        try:
            wb = openpyxl.load_workbook(path)
            v = wb[sheet].cell(row, col).value
            return v
        except:
            return ""
