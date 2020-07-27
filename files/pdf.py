import PyPDF2
from PyPDF2 import PdfFileReader


# https://realpython.com/pdf-python/


pdf_path = '/home/pit/Desktop/the_hobbit.pdf'


def open_pdf(file_path):
    # open in read binary mode
    pdf_file = open(file_path, 'rb')
    # pass the object to PyPDF2
    return PyPDF2.PdfFileReader(pdf_file)


def get_page_number(r: PdfFileReader):
    return r.numPages


def get_page_content(r: PdfFileReader, page_n):
    try:
        page = r.getPage(page_n)
    except IndexError:
        return 'The PDF has to page n°' + str(page_n)
    return page.extractText()


if __name__ == '__main__':
    reader = open_pdf(pdf_path)
    print(get_page_number(reader))
    exit(0)
