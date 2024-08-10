import os
import shutil

class VersionControl:
    def track(self, document_path):
        version = 1
        versioned_file = f"{document_path}_v{version}.docx"
        while os.path.exists(versioned_file):
            version += 1
            versioned_file = f"{document_path}_v{version}.docx"
        shutil.copy(document_path, versioned_file)
        return versioned_file
