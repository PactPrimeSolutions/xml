from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from xml.etree import ElementTree as ET
from django.contrib import messages
import xml.dom.minidom

def upload_file(request):
    if request.method == 'POST' and 'xml_file' in request.FILES:
        uploaded_file = request.FILES['xml_file']

        if uploaded_file.size == 0:
            messages.error(request, "The uploaded file is empty.")
            return render(request, 'editor/upload.html')

        try:
            # Save the file temporarily
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.path(filename)

            # Read the file content with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            # Parse the file as XML
            root = ET.fromstring(content)

            # Extract data into a dictionary for editing
            xml_data = {child.tag: child.text for child in root}

            # Pass the data to the form template for editing
            return render(request, 'editor/edit_form.html', {'xml_data': xml_data})

        except ET.ParseError as e:
            messages.error(request, f"The uploaded file is not a valid XML file. Error: {e}")
            return render(request, 'editor/upload.html')
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {e}")
            return render(request, 'editor/upload.html')

    return render(request, 'editor/upload.html')

def download_xml(request):
    if request.method == 'POST':
        # Create a new XML root element
        root = ET.Element('root')

        # Update the XML structure with the form data
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':  # Ignore the CSRF token
                element = ET.SubElement(root, key)
                element.text = value

        # Serialize the updated XML into a string
        updated_xml = ET.tostring(root, encoding='utf-8', xml_declaration=True)

        # Format the XML for better readability
        formatted_xml = xml.dom.minidom.parseString(updated_xml)
        pretty_xml = formatted_xml.toprettyxml(indent="  ")

        # Create the response for displaying the XML content in the browser
        response = HttpResponse(pretty_xml, content_type='application/xml')
        response['Content-Disposition'] = 'attachment; filename="updated.xml"'  # Trigger download
        return response

    return redirect('upload_file')

def parse_xml_to_dict(xml_data):
    return {child.tag: child.text for child in xml_data}
