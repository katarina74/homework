import xlrd, xlwt


# класс ошибки неправильных входных данных
class MyError(Exception):
    def __init__(self, text):
        self.txt = text


# проверка корректности входных данных
def correct_test(preferences):
    if preferences["Market A"].keys() != preferences["Market B"].keys():
        return True
    elif set(preferences["Market A"].keys()) != set(preferences["Market B"].keys()):
        return True
    return False


# создание базы данных
def get_data_base(fname):
    try:
        rb = xlrd.open_workbook(fname, formatting_info=True)
        sheet = rb.sheet_by_index(0)

        preferences = {"Market A": dict(), "Market B": dict()}
        s = sheet.nrows
        n = int(sheet.nrows/2)
        if n*2 != s:
            raise MyError("неравное количество мужчин и женщин!")

        for row_num in range(n):
            preferences["Market A"][row_num+1] = list(map(int, sheet.row_values(row_num)[1:]))
        for row_num in range(n):
            preferences["Market B"][row_num+1] = list(map(int, sheet.row_values(row_num+n)[1:]))
        if correct_test(preferences):
            raise MyError("неправильно заданы предпочтения!")
        return preferences

    except xlrd.biffh.XLRDError:
        return "неправильный формат файла!"
    except MyError as mr:
        return mr
    except:
        return "неправильные входные данные или не выбран файл!"


def save_result(solution, f_name):
    if f_name[-4:] == ".xls":
        wb = xlwt.Workbook()
        ws = wb.add_sheet('result')
        for i in range(len(solution)):
            ws.write(i, 0, solution[i][0])
            ws.write(i, 1, solution[i][1])
        wb.save(f_name)
    else:
        return "Неверный формат файла, решение не может быть сохранено!"
