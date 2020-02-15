import xlrd, xlwt


# класс ошибки неправильных входных данных
class MyError(Exception):
    pass


# проверка корректности входных данных
def correct_test(n, preferences):
    lst = list(range(1, n + 1))
    set_lst = set(lst)
    if list(preferences["Market A"].keys()) != lst or list(preferences["Market B"].keys()) != lst:
        return True
    for i, j in zip(preferences["Market A"].values(), preferences["Market B"].values()):
        if set(i) != set_lst or set(j) != set_lst or n != len(i) or n != len(j):
            return True
    return False


# создание базы данных
def get_data_base(fname):
    try:
        rb = xlrd.open_workbook(fname, formatting_info=True)
        sheet = rb.sheet_by_index(0)

        preferences = {"Market A": dict(), "Market B": dict()}
        s = sheet.nrows
        n = int(s/2)
        if s % 2:
            raise MyError("Неравное количество мужчин и женщин!")
        for row_num in range(n):
            preferences["Market A"][row_num+1] = list(map(int, sheet.row_values(row_num)[1:]))
        for row_num in range(n):
            preferences["Market B"][row_num+1] = list(map(int, sheet.row_values(row_num+n)[1:]))
        if correct_test(n, preferences):
            raise MyError("Неправильно заданы предпочтения!")

    except xlrd.biffh.XLRDError:
        return "Неправильный формат файла!"
    except MyError as mr:
        return str(mr)
    except:
        return "Неправильные входные данные или не выбран файл!"
    else:
        return preferences


def save_result(solution, f_name):
    if f_name[-4:] == ".xls":
        wb = xlwt.Workbook()
        ws = wb.add_sheet('result')
        for i in range(len(solution)):
            ws.write(i, 0, solution[i][0])
            ws.write(i, 1, solution[i][1])
        wb.save(f_name)
        return "Решение успешно сохранено!"
    else:
        return "Неверный формат файла! Решение не может быть сохранено!"
