from docx import Document

class DocumentAssembly:
    def create_document(self, template_name, data):
        doc = Document(f'legaldocs_cms/document_templates/{template_name}')
        for key, value in data.items():
            for paragraph in doc.paragraphs:
                if key in paragraph.text:
                    paragraph.text = paragraph.text.replace(f'{{{{{key}}}}}', value)
        file_name = f"{data['client_name']}_document.docx"
        doc.save(file_name)
        return file_name
