import openpyxl


def get_workbook(file_path):
    return openpyxl.load_workbook(file_path)


def get_sheet(file_path, s_name):
    workbook = get_workbook(file_path)
    # sheet = workbook.get_sheet_by_name(s_name) [deprecated]
    return workbook[s_name]


def get_sheets(file_path):
    workbook = get_workbook(file_path)
    # sheets = workbook.get_sheet_names() [deprecated]
    return workbook.sheetnames


def get_cell(file_path, s_name, cell_name):
    sheet = get_sheet(file_path, s_name)

    # for cell_name = 'A1' --> cell = sheet.cell(row=1, column=1)
    cell = sheet[cell_name]
    # write a def that check for the type and return it in a more appropriate way
    return str(cell.value)


def get_cells(file_path, s_name, row, column):
    sheet = get_sheet(file_path, s_name)
    for i in range(1, column + 1):
        for j in range(1, row + 1):
            msg = '{}:\t{}'.format(j, sheet.cell(row=j, column=i).value)
            if j == 1:
                print(msg.upper())
            else:
                print(msg)
        print('')


if __name__ == '__main__':
    ex_file = 'excel_file.xlsx'
    print(get_sheet(ex_file, 'Sheet1'))
    print(get_sheets(ex_file))
    print(get_cell(ex_file, 'Sheet1', 'A1'))
    get_cells(ex_file, 'Sheet1', 4, 5)
    exit(0)
