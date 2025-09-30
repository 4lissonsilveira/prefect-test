import os
import xml.etree.ElementTree as ET

def process_object(object_name):
    # Paths for the object
    object_path = f"salesforce_project/force-app/main/default/objects/{object_name}/{object_name}.object"
    fields_dir = f"salesforce_project/force-app/main/default/objects/{object_name}/fields"
    permissionset_dir = "salesforce_project/force-app/main/default/permissionsets"
    permissionset_path = os.path.join(permissionset_dir, f"All{object_name}Fields.permissionset-meta.xml")

    # Ensure the fields and permissionset directories exist
    os.makedirs(fields_dir, exist_ok=True)
    os.makedirs(permissionset_dir, exist_ok=True)

    # Parse the object XML
    tree = ET.parse(object_path)
    root = tree.getroot()

    # Salesforce metadata namespace
    ns = {"sf": "http://soap.sforce.com/2006/04/metadata"}

    # Collect field API names for the permission set
    field_api_names = []

    for field in root.findall("sf:fields", ns):
        # Get the field name
        full_name = field.find("sf:fullName", ns).text

        # Skip standard fields (fields without "__c" in their API name)
        if not full_name.endswith("__c"):
            print(f"Skipping standard field: {full_name}")
            continue

        # Create a new XML tree for the field
        field_xml = ET.Element("CustomField", xmlns="http://soap.sforce.com/2006/04/metadata")
        for child in field:
            field_xml.append(child)

        # Add the field to the list for the permission set
        field_api_names.append(full_name)

        # Write the field XML to file
        filename = os.path.join(fields_dir, f"{full_name}.field-meta.xml")
        ET.ElementTree(field_xml).write(filename, encoding="utf-8", xml_declaration=True)

    # Create the permission set XML
    ps_root = ET.Element("PermissionSet", xmlns="http://soap.sforce.com/2006/04/metadata")

    # Add the label (required for permission sets)
    label = ET.SubElement(ps_root, "label")
    label.text = f"All {object_name} Fields"

    for api_name in field_api_names:
        fp = ET.SubElement(ps_root, "fieldPermissions")
        editable = ET.SubElement(fp, "editable")
        editable.text = "true"
        field_tag = ET.SubElement(fp, "field")
        field_tag.text = f"{object_name}.{api_name}"
        readable = ET.SubElement(fp, "readable")
        readable.text = "true"

    # Write the permission set XML to file
    ET.ElementTree(ps_root).write(permissionset_path, encoding="utf-8", xml_declaration=True)

    print(f"Done! Created field files in {fields_dir} and permission set in {permissionset_path}")

# Example usage for Warranty__c
process_object("Warranty__c")