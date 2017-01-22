from cStringIO import StringIO

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams

def get_pages(pdf_file):
    ''' 
    Takes in the name of a PDF file and yields out the text of each page.
    '''
    # This is a good start. It needs to be cleaned up a bit for error handling
    # and some cleaner syntax. Maybe I can refactor without having to create a 
    # PDFDocument object and then a new instance of the same object for each
    # page?
    with open(pdf_file, 'rb') as in_file:
        parser = PDFParser(in_file)
        document = PDFDocument(parser)
        sio = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        if not document.is_extractable:
            print 'Cannot extract'
        rsrcmgr = PDFResourceManager() 
        new_device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, new_device)
        for page in PDFPage.create_pages(document):
            page_rsrcmgr = PDFResourceManager() 
            page_sio = StringIO()
            page_device = TextConverter(page_rsrcmgr, page_sio, codec=codec, laparams=laparams)
            page_interpreter = PDFPageInterpreter(page_rsrcmgr, page_device)
            page_interpreter.process_page(page)
            text = page_sio.getvalue() 
            yield text
            page_device.close()
        new_device.close()

if __name__ == '__main__':
    # Simple CLI interface for testing PDF files:
    import sys
    try:
        in_file = sys.argv[1]
    except IndexError:
        print 'Please give the PDF file name that you wish to convert.'
    
    pdf_file = 'Curse of the Riven Sky.pdf'
    pages = get_pages(pdf_file)

    for p in pages:
        print p
