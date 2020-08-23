import docx

demo_path = '/home/pit/Documents/python_projects/python-structure/files/demo.docx'


'''
Document object contains Paragraph objects.
Paragraph objects contain Run objects.
'''


def get_doc_object(obj_path):
    d = docx.Document(obj_path)
    return d.paragraphs


if __name__ == '__main__':
    print(get_doc_object(demo_path))
    exit(0)
