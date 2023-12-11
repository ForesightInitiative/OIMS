#*<%REGION File header%>
#*=============================================================================
#* File      : OIMS_schema_consistency_test.py
#* Author    : Gideon Kruseman <g.kruseman@cgiar.org>
#* Version   : 1.0
#* Date      : 11/20/2023 9:41:58 AM
#* Changed   :
#* Changed by:
#* Remarks   :
#
"""
*! <%GTREE 0 tool documentation%>

*! <%GTREE 0.1 technical information%>
language: python
version: 1.0.0
data: November 2023
author: Gideon Kruseman <g.kruseman@cgiar.org>
status: under development

*! <%GTREE 0.2 input%>


*! <%GTREE 0.3  command line parameters%>
*! <%GTREE 0.3.1 required command line paremers%>

*! <%GTREE 0.4  description of the script%>
*_ Initialization:

The script starts by initializing necessary libraries and checking command-line arguments

*! <%GTREE 0.99  notes%>

"""
#
#*=============================================================================
#*<%/REGION File header%>
#*! <%GTREE 1 initialization%>
#*! <%GTREE 1.1 import libraries%>
#*! <%GTREE 1.1.1 import system libraries%>
import sys
import argparse
import os


#*! <%GTREE 1.1.2 import json libraries%>
import json

#*! <%GTREE 1.1.3 import pdf write libraries%>
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
print("line 51")

#*! <%GTREE 1.2 Check command line arguments for settings file path%>
parser = argparse.ArgumentParser(description='check consistency of an OIMS compatible metadata file against its underlying schemas')
parser.add_argument('--schema_to_test_path', required=True, help='Path to the OIMS compatible emetadata schema that needs to be tested')
parser.add_argument('--OIMS_basic_path', required=True, help='Path to the OIMS basic self describing metadata schema version used')
parser.add_argument('--OIMS_content_object', required=True, help='OIMS_content_object to be tested')
parser.add_argument('--OIMS_content_object_schema_path', required=True, help='Path to schema describing the OIMS_content_object to be tested')
parser.add_argument('--OIMS_to_python_type_mapping_path',  help='path to json file with OIMS to python data type mappings')

args = parser.parse_args()

#*! <%GTREE 1.3 initialize an issues list%>
# Initialize an empty list to store issues
issues = []
warning_issues = []

#*! <%GTREE 1.4 data type mappings%>
#*! <%GTREE 1.4.1 json to python data type mappings%>
json_to_python_type_mapping = {
    "string": "str",
    "number": "int",  # or "float" based on precision needed
    "array": "list",
    "object": "dict",
    "boolean": "bool",
    "null": "NoneType"
}
print("line 78")

#*! <%GTREE 1.4.1 OIMS to python data type mappings%>
OIMS_to_python_type_mapping = {
    "string": ["str"],
    "text": ["str"],
    "date": ["str"],
    "uri": ["str"],
    "url": ["str"],
    "controlled_vocabulary": ["str"],
    "email": ["str"],
    "html": ["str"],
    "integer": ["int"],
    "float": ["float"],
    "compound_object": ["dict"],
    "boolean": ["bool"],
    "null": ["NoneType"],
    "any": ["str", "int", "float", "dict", "bool", "NoneType"]  # 'any' can be any of these types
}
#*! <%GTREE 2 define functions%>
#*! <%GTREE 2.1 validate file for OIMS structure %>
"""
to be expanded
"""
print("line 102")
#*! <%GTREE 2.1.1 validate file for general OIMS structure %>
def validate_oims_structure(file_path):
    try:
        # Load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Validate root element
        if not data.get("OIMS"):
            return "Invalid file: Root element 'OIMS' not found."

        oims_data = data["OIMS"]

        # Validate required objects in OIMS
        if "OIMS_header" not in oims_data or "OIMS_content" not in oims_data:
            return "Invalid file: 'OIMS_header' or 'OIMS_content' not found."

        # Validate OIMS header
        header_validation_result = validate_oims_header(oims_data["OIMS_header"])
        if header_validation_result is not None:
            return header_validation_result

        # Validate OIMS content
        content_validation_result = validate_oims_content(oims_data["OIMS_content"], oims_data["OIMS_header"])
        if content_validation_result is not None:
            return content_validation_result

        return "OIMS file is valid."

    except json.JSONDecodeError:
        return "Invalid file: File is not a valid JSON."
    except Exception as e:
        return f"An error occurred: {e}"

print("line 137")
#*! <%GTREE 2.1.2 validate header section%>
def validate_oims_header(header_data):
    required_components = ["mapping_info", "metadata_schema", "file_descriptors"]
    for component in required_components:
        if component not in header_data:
            return f"Invalid OIMS header: '{component}' not found."
    # Further validation of each component can be added here
    return None

#*! <%GTREE 2.1.3 validate content section%>
def validate_oims_content(content_data, header_data):
    # Validation logic based on metadata_schema
    # This is a placeholder function and needs specific implementation
    return None

#*! <%GTREE 2.1.4 function to test if file exists%>
def file_exists(file_path):
    """
    Check if a file exists at the given path.

    Args:
    file_path (str): The path of the file to check.

    Returns:
    bool: True if the file exists, False otherwise.
    """
    return os.path.exists(file_path) and os.path.isfile(file_path)

#*! <%GTREE 2.1.5 function toUse ReportLab to generate a PDF from the combined list%>
def generate_pdf(report, filename="report.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter  # Get width and height of the page
    y_position = height - 40  # Start position for the first line

    for line in report:
        c.drawString(40, y_position, line)
        y_position -= 20  # Move to the next line
        if y_position < 40:  # Check for new page
            c.showPage()
            y_position = height - 40

    c.save()
print("line 180")
#*! <%GTREE 3 read files%>
#*! <%GTREE 3.1 OIMS compatible metadata file to be tested%>
#*! <%GTREE 3.1.1 test file existence%>
"""
File path is in args.schema_to_test_path
check if file exists

for each check if not valid return an error and append the error or warning with key information to a list of issues
"""
# Check for the existence of the OIMS compatible metadata file
if not file_exists(args.schema_to_test_path):
    print(f"Error: OIMS compatible metadata file to be tested'{args.schema_to_test_path}' does not exist.")
    issues.append(f"Error: OIMS compatible metadata file to be tested'{args.schema_to_test_path}' does not exist.")
#*! <%GTREE 3.1.2 test if OIMS compatible emtadata file at structure level%>
else:
    # Validate the OIMS structure of the file
    validation_result = validate_oims_structure(args.schema_to_test_path)
    if validation_result != "OIMS file is valid.":
        issues.append(validation_result)
print("line 200")
#*! <%GTREE 3.1.3 extract some key information from the file%>
"""
for the OIMS_content_object to be tested get the identifier from args.OIMS_content_object
find the version of the underlying metadata schema in the array of compond objects [OIMS][OIMS_header][metadata_schema] where version is in
[OIMS][OIMS_header][metadata_schema][schema_properties][schema_version] and where [OIMS][OIMS_header][metadata_schema][OIMS_content_object] == args.OIMS_content_object
store this version id in a container OIMS_content_object_metadata_version
also store [OIMS][OIMS_header][metadata_schema][schema_properties][OIMS_content_object] in a container OIMS_content_object_metadata_OIMS_content_object

"""
# # Extracting and storing metadata schema information
if not issues:
    with open(args.schema_to_test_path, 'r') as file:
        oims_data_to_test = json.load(file)["OIMS"]

        # Extract the OIMS_content_object identifier
        oims_content_object = args.OIMS_content_object

        # Find the matching content object in the metadata schema array
        found = False
        for content_object in oims_data_to_test["OIMS_header"]["metadata_schema"]:
            if content_object["OIMS_content_object"] == oims_content_object:
                # Extract and store the version and other details of the metadata schema
                for schema_property in content_object["schema_properties"]:
                    if "schema_version" in schema_property and "OIMS_content_object" in schema_property:
                        oims_content_object_metadata_version = schema_property["schema_version"]
                        oims_content_object_metadata_OIMS_content_object = schema_property["OIMS_content_object"]

                        found = True
                        break
                if found:
                    break

        if not found:
            issues.append(f"Error: OIMS_content_object '{oims_content_object}' not found in the OIMS_header metadata_schema.")
        elif not oims_content_object_metadata_version or not oims_content_object_metadata_OIMS_content_object:
            issues.append(f"Error: Missing metadata version or OIMS_content_object in the OIMS schema for '{oims_content_object}'.")

found = False
if not issues:
    found = False
    for content_object in oims_data_to_test["OIMS_content"]:
        if content_object["OIMS_content_object"] == oims_content_object:
            if found:
                issues.append(f"Error: multiple instances of OIMS_content_object: {oims_content_object} found in metadata file to test.")
                break
            else:
                for prop in content_object["OIMS_content_object_properties"]:
                    if "metadata" in prop:
                        oims_data_to_test_metadata = prop["metadata"]
                        found = True
                        break


print("line 254")

#*! <%GTREE 3.2 OIMS base self describing metadata %>#*! <%GTREE 3.1.1 test file existence%>
#*! <%GTREE 3.2.1 test file existence%>
"""
File path is in args.OIMS_basic_path
check if file exists if not return an error and append the error with key information to a list of issues
"""
# Check for the existence of the OIMS compatible metadata file
if not file_exists(args.OIMS_basic_path):
    print(f"Error: OIMS basic self-describing metadata file '{args.OIMS_basic_path}' does not exist.")
    issues.append(f"Error: OIMS basic self-describing metadata file '{args.OIMS_basic_path}' does not exist.")
#*! <%GTREE 3.2.2 test if OIMS compatible emtadata file at structure level%>
else:
    # Validate the OIMS structure of the file
    validation_result = validate_oims_structure(args.OIMS_basic_path)
    if validation_result != "OIMS file is valid.":
        issues.append(validation_result)

#*! <%GTREE 3.2.3 extract some key information from the file%>
"""
extract the version of the OIMS_basic.json file from [OIMS][OIMS_header][file_descriptors][metadata_version][current_version]
warning if version is not in valid version list:
    2.3.0.0
    2.3.1.0
    2.3.2.0
    2.3.3.0
    2.4.0.0

"""
print("line 282")
# Valid versions list
valid_versions = ["2.3.1.0", "2.3.2.0", "2.3.3.0","2.4.0.0"]
obsolete_versions = ["2.3.0.0"]

if not issues:
     with open(args.OIMS_basic_path, 'r') as file:
        oims_basic_data = json.load(file)["OIMS"]
        current_version = oims_basic_data["OIMS_header"]["file_descriptors"]["metadata_version"]["current_version"]

        # Check if the current version is in the valid versions list
        if current_version in obsolete_versions:
            warning_issues.append(f"Warning: The version '{current_version}' of the OIMS_basic.json file is in the list of obsolete versions.")
        if current_version not in valid_versions:
            issues.append(f"Warning: The version '{current_version}' of the OIMS_basic.json file is not in the list of valid versions.")

#*! <%GTREE 3.3 underlying metametadata schema %>
#*! <%GTREE 3.3.1 test file existence%>
"""
File path is in args.OIMS_content_object_schema_path
check if file exists if not return an error and append the error with key information to a list of issues
"""
print("line 304")
# Check for the existence of the content object schema file
if not file_exists(args.OIMS_content_object_schema_path):
    print(f"Error: OIMS content object schema file '{args.OIMS_content_object_schema_path}' does not exist.")
    issues.append(f"Error: OIMS content object schema file '{args.OIMS_content_object_schema_path}' does not exist.")

else:
    #*! <%GTREE 3.3.2 test if OIMS compatible emtadata file at structure level%>
    """
    validate file for OIMS structure using the function  validate_oims_structure(file_path)
    """
    # Validate the OIMS structure of the file
    validation_result = validate_oims_structure(args.OIMS_content_object_schema_path)
    if validation_result != "OIMS file is valid.":
        issues.append(validation_result)

    #*! <%GTREE 3.2.3 extract some key information from the file%>
    """
    extract the version of the OIMS_basic.json file from [OIMS][OIMS_header][file_descriptors][metadata_version][current_version] and test if equal to value of OIMS_content_object_metadata_version

    check [OIMS][OIMS_content] for instances in the array of compound objects where "OIMS_content_object" == OIMS_content_object_metadata_OIMS_content_object. This requires iterating through the OIMS_content array.

    """
    # If the metametadata file is valid, proceed to extract information
    if validation_result == "OIMS file is valid.":
        with open(args.OIMS_content_object_schema_path, 'r') as file:
            metametadata_data = json.load(file)["OIMS"]

            # Extract current version from the file
            extracted_version = metametadata_data["OIMS_header"]["file_descriptors"]["metadata_version"]["current_version"]

            # Check if extracted version matches with OIMS_content_object_metadata_version
            if extracted_version != oims_content_object_metadata_version:
                issues.append(f"Error: Metametadata file version mismatch. Extracted version {extracted_version} does not match version in the metadata schema defined in the header ofv the OIMS compatible metadata file that is tested  {oims_content_object_metadata_version}.")

            found = False
            for content_object in metametadata_data["OIMS_content"]:
                if content_object["OIMS_content_object"] == oims_content_object_metadata_OIMS_content_object:
                    found = True
                    for prop in content_object["OIMS_content_object_properties"]:
                        if "metadata" in prop:
                            metametadata = prop["metadata"]
                        break

        if not found:
            issues.append(f"Error: the OIMS_content_object '{oims_content_object_metadata_OIMS_content_object}' not found in the OIMS_content section of the metametadata file.")


print("line 352")



#*! <%GTREE 4 test schema%>
#*! <%GTREE 4.1 test header%>
"""
Use the metadata contents of OIMS base self describing metadata schema in the instance in the array of compound objects [OIMS][OIMS_content] where "OIMS_content_object" == "OIMS_Header_Metadata"
the metadata_contents are found in [OIMS][OIMS_content][metadata]
check the consistency of the OIMS_header section of the file we are testing [in args.OIMS_content_object_schema_path] with the information from the self-describing metadata schema.

for each check if not valid return an error and append the error or warning with key information to a list of issues
"""
#*! <%GTREE 4.2 test contents%>
"""
In the underlying metametadata schema the metadata attributes that we can find the file that is being tested in the following way:
[OIMS][OIMS_content][metadata] is an array of compound_objects that have at least the following attributes
                                "attribute_name": "<name of the metadata attribute",
                                "attribute_description": "description of the metadata attribute",
                                "data_type": "the data type of the metadata attribute",
                                "requirement_level": element from a contyrolled environment,
                                "data_type_class": "primitive" or "compound",
                                "multiple": true or false
for each metadata element in the OIMS_contents section of the file that is being tested where "OIMS_content_object" == args.OIMS_content_object that corresponds to a value of "attribute_name" in the underlyinh schema
"""
#*! <%GTREE 4.2.1 test preparetory checks%>
#*! <%GTREE 4.2.1.1.1 get standard valid OIMS data types from  OIMS_to_python_type_mapping%>
"""
To ensure that the data_type specified in each attribute of your metametadata is a valid OIMS data type, you can perform a check against the keys of your OIMS_to_python_type_mapping dictionary.
This will validate that each data_type is one of the recognized OIMS data types.
"""
valid_oims_types = OIMS_to_python_type_mapping.keys()

#*! <%GTREE 4.2.1.1.2 Iterate over attributes in metametadata and check if valid standard OIMS metadata%>

def test_datatypemapping(mapping_id, metametadata, valid_oims_types):
    require_data_type_mapping = False
    warnings = []
    invalid_types = set()

    # Iterate over attributes in metametadata
    for attribute in metametadata:
        oims_type = attribute.get("data_type")

        # Check if the data_type is a valid OIMS type
        if oims_type not in valid_oims_types:
            warnings.append(f"Invalid OIMS data type '{oims_type}' in metametadata for attribute '{attribute['attribute_name']}' using {mapping_id}.")
            invalid_types.add(oims_type)
            require_data_type_mapping = True

    return require_data_type_mapping, warnings, invalid_types

require_data_type_mapping, warnings, invalid_types = test_datatypemapping("OIMS standard mapping", metametadata, valid_oims_types)
warning_issues.extend(warnings)


#*! <%GTREE 4.2.1.1.3 if external mapping is required make sure it is loaded%>
if require_data_type_mapping:
    # Check for the existence of the external data type mapping file
    if not file_exists(args.OIMS_to_python_type_mapping_path):
        issues.append(f"Error: External data type mapping file '{args.OIMS_to_python_type_mapping_path}' does not exist.")
    #*! <%GTREE 3.1.2 test if OIMS compatible emtadata file at structure level%>
    else:
        with open(args.args.OIMS_to_python_type_mapping_path, 'r') as file:
            OIMS_to_python_type_mapping = json.load(file)
            valid_oims_types = OIMS_to_python_type_mapping.keys()

        # Re-check with the external mapping
        require_data_type_mapping, new_warnings, new_invalid_types = test_datatypemapping("provided data type mapping", metametadata, valid_oims_types)
        warning_issues.extend(new_warnings)

        #*! <%GTREE 4.2.1.1.4 the data check %>
        if require_data_type_mapping:
            issues.append(f"Invalid OIMS data types found in file to be tested, see warnings for details.")

print("line 427")
#*! <%GTREE 4.2.2 actual test%>
if not issues:
    # Iterate over key-value pairs in oims_data_to_test_metadata
    for compound_object in oims_data_to_test_metadata:
        # Iterate over key-value pairs in each compound object
        for key, value in compound_object.items():
            # 'key' is the attribute name in the compound object
            # 'value' is the value of that attribute
            found = False

        for meta_attribute in metametadata:
            if meta_attribute["attribute_name"] == key:
                found = True
                expected_data_type = meta_attribute["data_type"]
                python_types = OIMS_to_python_type_mapping.get(expected_data_type, [])

                """
                1.  what is the data type of metadata_field_value?
                    is that compatible with the data type identifier in attributes["atrribute_name"]?
                """
                """
                2.  if  attributes["multiple"] is true then metadata_field_value is an array
                """
                # Check if 'multiple' is true and value is a list
                if meta_attribute["multiple"]:
                    if not isinstance(value, list):
                        issues.append(f"Error: '{key}' should be an array as per metametadata.")
                    else:
                        # Check the data type of each element in the list
                        for item in value:
                            if type(item).__name__ not in python_types:
                                issues.append(f"Data type mismatch in array '{key}': Expected element of type {python_types}, found {type(item).__name__}.")
                        """
                        3.  if "data_type_class":"primitive" then the value is a simple value if "data_type_class":"compound" then the value is a compound object
                        """
                        if meta_attribute ["data_type_class"] == "compound" and not isinstance(item, dict):
                            issues.append(f"Error: '{key}' should be a compound object as per metametadata.")
                        elif meta_attribute ["data_type_class"] == "primitive" and isinstance(item, dict):
                            issues.append(f"Error: '{key}' should be a primitive value as per metametadata.")
                else:
                    # For non-array values, check the data type directly
                    if type(value).__name__ not in python_types:
                        issues.append(f"Data type mismatch for '{key}': Expected {python_types}, found {type(value).__name__}.")

                    """
                    3.  if "data_type_class":"primitive" then the value is a simple value if "data_type_class":"compound" then the value is a compound object
                    """
                    if meta_attribute ["data_type_class"] == "compound" and not isinstance(value, dict):
                        issues.append(f"Error: '{key}' should be a compound object as per metametadata.")
                    elif meta_attribute ["data_type_class"] == "primitive" and isinstance(value, dict):
                        issues.append(f"Error: '{key}' should be a primitive value as per metametadata.")

                break  # Exit loop as the field is found

        if not found:
            issues.append(f"Error: Metadata field '{key}' not found in metametadata.")
    for meta_attribute  in metametadata:
        # For each element in the underlying metadata schema where "requirement_level":"required" the metadata attribute identified in "attribute_name" should be checked in the relevant metadata section in file hat is tested if it is present and has a value
        if (meta_attribute ["requirement_level"] == "required") :
            required_field = meta_attribute["attribute_name"]
            if not any(required_field in compound_object for compound_object in oims_data_to_test_metadata):
                issues.append(f"Error: Required metadata field '{required_field}' not found in file: {args.schema_to_test_path}.")

print("line 491")
#*! <%GTREE 5 write report%>
"""
Generate a report in pdf format from the warnings list and the issues list.
1. combine the two list with clear demarcation between warnings (warning_issue) and fatal errors (issues).
2. export to pdf
"""
combined_report = []

# Add warnings to the combined report
if warning_issues:
    combined_report.append("Warnings:")
    combined_report.extend(warning_issues)
    combined_report.append("\n")  # Add a newline for separation

# Add issues to the combined report
if issues:
    combined_report.append("Fatal issues:")
    combined_report.extend(issues)

path_to_output_file = os.path.splitext(args.schema_to_test_path)[0] +  "_OIMS_test_Report.pdf"
generate_pdf(combined_report,path_to_output_file)
print("line 513")
#*============================   End Of File   ================================