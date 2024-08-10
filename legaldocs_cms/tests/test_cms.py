import unittest
from legaldocs_cms.cms import LegalDocsCMS

class TestCMS(unittest.TestCase):
    def setUp(self):
        self.cms = LegalDocsCMS()

    def test_create_document(self):
        data = {"client_name": "John Doe", "case_number": "12345"}
        document = self.cms.create_document("contract_template.docx", data)
        self.assertTrue(document.endswith("_document.docx"))

    def test_version_control(self):
        document = "John_Doe_document.docx"
        versioned_document = self.cms.track_version(document)
        self.assertTrue("_v1.docx" in versioned_document)

if __name__ == "__main__":
    unittest.main()
