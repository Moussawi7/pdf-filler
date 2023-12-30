import fitz


class FitzExportService:

    def __init__(self):
        pass

    def export_file_system(self, pdf_streams, destination):
        pdf_document = fitz.open()
        for pdf_stream in pdf_streams:
            pdf_document_stream = fitz.open("pdf", pdf_stream)
            pdf_document.insert_pdf(pdf_document_stream)

        pdf_document.save(destination)
        pdf_document.close()

        return destination

    def export_raw(self, pdf_streams):
        pdf_document = fitz.open()
        for pdf_stream in pdf_streams:
            pdf_document_stream = fitz.open("pdf", pdf_stream)
            pdf_document.insert_pdf(pdf_document_stream)

        pdf_bytes = pdf_document.write()
        pdf_document.close()

        return pdf_bytes
