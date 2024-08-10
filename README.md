# LegalDocsCMS

LegalDocsCMS is a Python-based Content Management System (CMS) designed specifically for managing legal documents within a law firm. This system automates document creation, version control, and access permissions, ensuring that legal documents are managed efficiently, accurately, and securely.

## Features

- **Automated Document Assembly**: Generate legal documents using predefined templates and custom data inputs.
- **Version Control**: Track changes to documents and maintain a history of versions.
- **Access Permissions**: Implement role-based access controls to ensure that only authorized personnel can view or edit documents.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/OleksandrOstroukhov/LegalDocsCMS.git

2. Navigate to the project directory:
	```bash
   cd LegalDocsCMS

3. Create and activate a virtual environment (recommended):
	```bash
   python -m venv venv

4. On Windows:
	```bash
   venv\Scripts\activate

5. On macOS/Linux:
	```bash
   source venv/bin/activate

6. Install the required dependencies:
	```bash
   pip install -r requirements.txt

#### Usage

1. To create a new document using the CMS:
	```bash
   python legaldocs_cms/cms.py
   
This will generate a document based on the template and data provided in the script.

2. To create a new document using the CMS:
	```bash
   python -m unittest discover legaldocs_cms/testspython legaldocs_cms/cms.py
   
This will run all the unit tests to ensure the system is functioning correctly.

#### Project Structure

legaldocs_cms/
	
__init__.py: Initializes the CMS module.
	
cms.py: The main file that controls the overall workflow of the CMS.
	
document_templates/: Contains the document templates used for automated document assembly.
	
modules/: Contains individual modules such as document_assembly.py, version_control.py, and 
access_permissions.py.
	
integration/: Placeholder for future integration with other systems.
	
tests/: Contains unit tests for the CMS modules.
	
utils/: Placeholder for utility scripts.
	
#### Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

#### License
This project is licensed under the MIT License - see the LICENSE file for details.
