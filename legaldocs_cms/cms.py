from legaldocs_cms.modules.document_assembly import DocumentAssembly
from legaldocs_cms.modules.version_control import VersionControl
from legaldocs_cms.modules.access_permissions import AccessPermissions

class LegalDocsCMS:
    def __init__(self):
        self.doc_assembly = DocumentAssembly()
        self.version_control = VersionControl()
        self.access_permissions = AccessPermissions()

    def create_document(self, template_name, data):
        return self.doc_assembly.create_document(template_name, data)

    def track_version(self, document):
        return self.version_control.track(document)

    def set_permissions(self, document, user, permission_level):
        return self.access_permissions.set_permission(document, user, permission_level)

if __name__ == "__main__":
    cms = LegalDocsCMS()
    data = {"client_name": "John Doe", "case_number": "12345"}
    document = cms.create_document("contract_template.docx", data)
    cms.track_version(document)
    cms.set_permissions(document, "lawyer", "edit")
