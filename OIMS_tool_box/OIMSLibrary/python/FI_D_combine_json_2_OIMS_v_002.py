#*<%REGION File header%>
#*=============================================================================
#* File      : FI_D_combine_json_2_OIMS_v_002.py
#* Author    : Gideon Kruseman <g.kruseman@cgiar.org>
__version__ = "2.0.0"
#* Date      : 12/12/2023 10:37:01 AM
#* Changed   :
#* Changed by:
#* Remarks   :
"""
*! <%GTREE 0 Documentation of the OIMS schema consistency test version 2%>

language: python
version: 2.0.0
data: December 2023
author: Gideon Kruseman <g.kruseman@cgiar.org>
status: under development

*! <%GTREE 0.2 input%>


*! <%GTREE 0.3  command line parameters%>
*! <%GTREE 0.3.1 required command line parameters%>

*! <%GTREE 0.3.2 optional command line parameters%>
--FI_D_Excel_template_path         : template collecting metadata
--Dataverse_metadata_url           : url of dataverse metadata in json.schema format
--location_of_data_folder          : folder where the data is located for autimatic extraction of definition metadata at data container level.


The code should be as generic as possible. It should also be flexible and extensible.
The use of functions and classes is recommended as well asensuring reusqability of functions.

*! <%GTREE 0.5  description of the script%>


*! <%GTREE 0.6 version history%>

*! <%GTREE 0.99 Notes%>
"""
#*=============================================================================
#*<%/REGION File header%>
#*! <%GTREE 1.1  import libraries%>
#*! <%GTREE 1.1.1 basics  library%>
import os
import urllib.parse
import sys

#*! <%GTREE 1.1.2 command line parser linrary%>
import argparse

#*! <%GTREE 1.1.3 read external sources library%>
import json
import io
import requests


#*! <%GTREE 1.1.4 libraries to enhance reporting%>
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

#*! <%GTREE 1.1.5 enhanced error handling%>
import logging

#*! <%GTREE 1.1.6 unpacking rar files%>
from pyunpack import Archive

#*! <%GTREE 1.1.7 excel reader%>
import pandas as pd

#*! <%GTREE 1.2 define standard locations in the Foresight Initiative GitHub repository%>
oims_structure_url = 'https://raw.githubusercontent.com/ForesightInitiative/OIMS/main/BasicSchemas/OIMS_structure.schema.json'

#*! <%GTREE 1.3 standard text definitions for reporting purposes%>
report_text_boilerplate_intro=" <introductory text>"
report_text_title=" OIMS-compatible metadata file creation report"

#*! <%GTREE 1.4 initialize lists%>
#*! <%GTREE 1.4.1 initialize an issues list%>
# Initialize an empty list to store issues
#*! <%GTREE 1.4.1.1 initialize an fatal issues list in the process of extracting and converting various sources%>
fatal_issues = []
#*! <%GTREE 1.4.1.2 initialize an warnings issues list in the process of extracting and converting various sources%>
warning_issues = []
#*! <%GTREE 1.4.1.3 initialize an process list for transparanecy purposes%>
process_list = []

#*! <%GTREE 2 define classes%>
#*! <%GTREE 2.1 define main OIMS structure%>
class OIMSMetadata:
    def __init__(self):
        #place holder class
        pass

#*! <%GTREE 2.2 define OIMS factory%>
class OIMSMetadataFactory:
    @staticmethod
    def create_metadata(json_data,json_data_id):
        # Identify the structure of json_data and create OIMSMetadata accordingly
        if "some_unique_identifier" in json_data:
            # Process json_data to fit the expected structure
            processed_data,error,warning,process = process_FI_D_template_1_6_json_for_oims(json_data,json_data_id)
            return OIMSMetadata(processed_data)
        elif "some other unique identifier" in json_data:
            processed_data,error,warning,process = process_FI_D_template_1_2_json_for_oims(json_data,json_data_id)
            return OIMSMetadata(processed_data)
        elif is_dataverse_metadata(json_data):
            processed_data,error,warning,process = is_dataverse_metadata(json_data)(json_data,json_data_id)
            return OIMSMetadata(processed_data)
        # Add more conditions as necessary for different structures

    def process_FI_D_template_1_6_json_for_oims(json_data, json_data_id):
        process = f"extracting foresight initiative data metadata template version 1.6 metadata from {json_data_id}"
        # Process the JSON data to fit the OIMS structure
        # This might involve renaming keys, restructuring nested data, etc.
        processed_data = {}
        # ... processing logic ...
        return processed_data None None process

    def process_FI_D_template_1_2_json_for_oims(json_data):
        # Process the JSON data to fit the OIMS structure
        # This might involve renaming keys, restructuring nested data, etc.
        processed_data = {}
        # ... processing logic ...
        return processed_data None None process

    def is_dataverse_metadata(json_data)(json_data):
        # Process the dataverse JSON schema metadata file to fit the OIMS structure
        # This might involve renaming keys, restructuring nested data, etc.
        processed_data = {}
        # ... processing logic ...
        return processed_data None None process


#*! <%GTREE 2.3 define OIMS primary metadata container%>
class OIMSPrimaryMetadataContainer:
    def __init__(self, processed_data=None):
        """
        Initialize the container with processed primary metadata if available.
        Expected structure after processing:
        {
            "OIMS": {
                "OIMS_header":{},
                "OIMS_content":[{}]
            }
        }
        this is based on the high-level OIMS structure logic as documented in [add ref]
        """
        default_structure =  {
            "OIMS": {
                "OIMS_header" : {
                    "mapping_info":[{}],
                    "metadata_schema":[
                        {
                            "OIMS_content_object":"",
                            "schema_properties": [
                                {
                                    "schema_name":"",
                                    "schema_description":"",
                                    "schema_type": "",
                                    "schema_subtype": "",
                                    "schema_version": "",
                                    "schema_url": "",
                                    "OIMS_content_object": ""
                                }
                            ]
                        }
                    ],
                    "file_descriptors":{
                        "MetadataName"                : "",
                        "MetaDataDescription"         : "",
                        "MetadataVersion"  : {
                            "CurrentVersion"          : "",
                            "MetadataVersionStatus"   : ""
                           },
                        "Contact":[
                           {
                            "ContactName"             : "",
                            "ContactRole"             : "",
                            "ContactAffiliation"      : {
                                "ContactAffiliationName"     :"",
                                "ContactAffiliationAcronym"  :""
                                },
                            "ContactIdentifier": [
                                {
                                    "IdentifierScheme":"",
                                    "Identifier":""
                                }
                            ],
                            "ContactEmail": []
                            }
                        ]
                    }
                },
                "OIMS_content": [
                    {
                        "OIMS_Content_Object":"",
                        "OIMS_Content_Object_Properties": {
                            "persistent_entity_id":[],
                            "entity_relastionship":[],
                            "entity_class":""
                            "metadata_class": [],
                            "metadata":[{}]
                        }
                    }
                ]
            }
        }
        self.OIMS_primary_metadata_container = processed_data if processed_data else default_structure

    # Additional methods for manipulating the metadata can be added here

#*! <%GTREE 2.4 define OIMS metametadata container linked to primary metadata%>
class OIMSMetaMetadataContainer:
    def __init__(self, underlying_schema=None):
        """
        the metametadata related to the primary metadata
        """
        default_structure =  {
            "OIMS": {
                "OIMS_header" : {
                    "mapping_info":[{}],
                    "metadata_schema":[
                        {
                            "OIMS_content_object":"",
                            "schema_properties": [
                                {
                                    "schema_name":"",
                                    "schema_description":"",
                                    "schema_type": "",
                                    "schema_subtype": "",
                                    "schema_version": "",
                                    "schema_url": "",
                                    "OIMS_content_object": ""
                                }
                            ]
                        }
                    ],
                    "file_descriptors":{
                        "MetadataName"                : "",
                        "MetaDataDescription"         : "",
                        "MetadataVersion"  : {
                            "CurrentVersion"          : "",
                            "MetadataVersionStatus"   : ""
                           },
                        "Contact":[
                           {
                            "ContactName"             : "",
                            "ContactRole"             : "",
                            "ContactAffiliation"      : {
                                "ContactAffiliationName"     :"",
                                "ContactAffiliationAcronym"  :""
                                },
                            "ContactIdentifier": [
                                {
                                    "IdentifierScheme":"",
                                    "Identifier":""
                                }
                            ],
                            "ContactEmail": []
                            }
                        ]
                    }
                },
                "OIMS_content": [
                    {
                        "OIMS_Content_Object":"",
                        "OIMS_Content_Object_Properties": {
                            "metadata_class": ["metametadata"],
                            "metadata":[
                                {
                                    "attribute_name":"",
                                    "attribute_description":"",
                                    "data_type":"",
                                    "requirement_level":"",
                                    "data_type_class":"",
                                    "multiple": ,

                                }
                            ]
                        }
                    }
                ]
            }
        }
        self.OIMS_metametadata_container = processed_data if processed_data else default_structure

    # Additional methods for manipulating the metametadata can be added here


#*! <%GTREE 3. define functions%>
#*! <%GTREE 3.1 define data mananagement functions%>
#*! <%GTREE 3.1.1 function to test if file exists and generate relevant error%>

def check_file_existence(file_path, file_description, issues_list):
    if not os.path.exists(file_path):
        error_message = f"Error: {file_description} 'path of {file_path}' does not exist."
        issues_list.append(error_message)
        return False
    elif not os.path.isfile(file_path)
        error_message = f"Error: {file_description} '{file_path}' does not exist."
        issues_list.append(error_message)
        return False
    return True

#*! <%GTREE 3.1.2 function to load data from internet%>
def load_json_github(url,issue_list):
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # This will directly parse the JSON content
    else:
        error_message = f"Failed to retrieve data from {url}"
        issues_list.append(error_message)
        return None




#*! <%GTREE 3.1.3 test if a file is a dataverse metadata file in json schema format%>
def is_dataverse_metadata(json_data):
    # Check for specific keys and values
    if json_data.get('@type') == 'Dataset':
        if json_data.get('@context') == 'http://schema.org' :
            key_to_check = 'identifier'
            if key_exists(json_data, key_to_check):
                return True
    return False



#*! <%GTREE 3.1.4 check if a key exists in a json file%>

def key_exists(json_data, key):
    return key in json_data

#*! <%GTREE 4 define command line parameter read function%>
#*! <%GTREE 4.1 define command line parameter read function top level%>
def argumentparser():
    parser = argparse.ArgumentParser(description='Script to process metadata from various sources and convert to OIMS compatble metadata file.')
    """
    parser.add_argument('--argument', help='placeholder')

    required commandline parameters
    """
    parser.add_argument('--output_folder', required = True, help='folder to place output such as OIMS compatible metadata files and the process report.')

    """
    optional command line parameters as they are context specific. at least one should be chosen
    """
    parser.add_argument('--FI_D_Excel_template_path', required = False, help='path to template collecting metadata.')
    parser.add_argument('--Dataverse_metadata_url', required = False, help='url of dataverse metadata in json.schema format.')
    parser.add_argument('--location_of_data_folder', required = False, help='folder where the data is located for automatic extraction of definition metadata at data container level.')
    parser.add_argument('--metametadata_excel_template_path', required = False, help='path to excel file with metametadata using the Foresight initiative standard.')

    """
    optional command line parameter with a defaut value
    """
    parser.add_argument('--output_metadatafile_name', required = False, help='name of the output metadata file.')
    args = parser.parse_args()

    if not args.output_metadatafile_name:
          args.output_metadatafile_name="unspecified"
    return args

#*! <%GTREE 5 define extraction functions%>
#*! <%GTREE 5.1 excel template converters%>
#*! <%GTREE 5.1.1 main converter function%>
def  FI_convert_template(settings_df,template_path, issues_list, process_list):
    process_list.append(f"Running FI_convert_template on {template_path}")
    issues_list.append(f"Start running FI_convert_template on {template_path}")
    all_data = {}
    #*! <%GTREE 5.1.1.1 read sheets as defined by settings file%>
    for _, row in settings_df.iterrows():
        sheet = row['sheet_name']
        skip_col = str(row['skip_col'])
        skip_row = str(row['skip_row'])
        data_format = row['format']
        header_row = row['header_row']

        data_range = get_range(row['data'], row['format'])

        # Read the entire sheet
        # Read the sheet using the specified header row
        try:
            if not pd.isna(header_row):
                full_df = pd.read_excel(template_path, sheet_name=sheet, header=int(header_row)-1)
            else:
                full_df = pd.read_excel(template_path, sheet_name=sheet, header=None)
        except Exception as e:
            error_message = f"Error reading sheet {sheet}: {e}"
            issues_list.append(error_message)
            continue

        if full_df.shape[0] == 0:
           error_message = f"Sheet {sheet} is empty. Skipping..."
           issues_list.append(error_message)
           continue

        # Drop ignored rows
        if not pd.isna(skip_row):
            ignore_rows = [int(float(x)) - 1 for x in skip_row.split(',') if x.strip().lower() != "nan"]  # Assuming 1-indexed rows
            full_df = full_df.drop(ignore_rows).reset_index(drop=True)

        # Drop ignored columns
        if not pd.isna(skip_col):
            ignore_cols = [excel_column_to_index(x.strip()) for x in skip_col.split(',') if x.strip().lower() != "nan"]
            for idx, col in enumerate(ignore_cols):
                if col >= len(full_df.columns):
                    print(f"Skipping invalid column index: {col} from input: {skip_col.split(',')[idx]}")
                    ignore_cols[idx] = -1  # set to an invalid value
            col_names_to_drop = [full_df.columns[i] for i in ignore_cols if i != -1]  # filter out the invalid value
            full_df = full_df.drop(columns=col_names_to_drop)

        # Filter out invalid column indices:
        data_range = [idx for idx in data_range if idx < full_df.shape[1]]

        if not data_range:
            error_message = f"No valid column indices for sheet {sheet}. Skipping..."
            issues_list.append(error_message)
            continue

        if data_format == 'vars_in_cols':
            valid_columns = full_df.columns.dropna().tolist()
            data_df = full_df[valid_columns]

        elif data_format == 'vars_in_rows':
            valid_rows_mask = ~full_df[full_df.columns[1]].isna()
            data_df = full_df[valid_rows_mask]

        all_data[sheet] = data_df

    #*! <%GTREE 5.1.1.2 Transform data for sheets where data_format == 'vars_in_rows' %>

    for sheet, df in all_data.items():
        print(f"Checking sheet: {sheet}")

        if isinstance(df, pd.DataFrame):
            print(f"Sheet {sheet} is a DataFrame.")

            if 0 in df.columns:
                print(f"Sheet {sheet} has a column named '0'.")

                transformed_data = {}
                for _, row in df.iterrows():
                    key = row[0]
                    values = row.iloc[1:].dropna().tolist()
                    transformed_data[key] = values

                print(f"Transformed data for sheet {sheet}:")  # Debug statement
                print(transformed_data)  # Debug statement

                all_data[sheet] = transformed_data
            else:
                print(f"Sheet {sheet} does not have a column named '0'. Column names are: {df.columns}")
        else:
            print(f"Sheet {sheet} is not a DataFrame.")


    #*! <%GTREE 5.1.1.3 remove the instances with no 'nans'' %>
    for key, value in all_data.items():
        if isinstance(value, pd.DataFrame):
            all_data[key] = dataframe_to_dict_without_nans(value)

    issues_list.append(f"End running FI_convert_template on {template_path}")
    #end
    return all_data

#*! <%GTREE 5.1.2 auximiary converter function: column index numbers%>
def excel_column_to_index(column):
    index = 0
    for char in column:
        index = index * 26 + (ord(char.upper()) - ord('A') + 1)
    return index - 1

#*! <%GTREE 5.1.3 auximiary converter function: get range%>
def get_range(value, data_format, max_value=10000):
    """Convert a range string to a list of values based on data format."""
    is_col = True if data_format == 'vars_in_rows' else False

    if ":" in value:
        start, end = value.split(":")
        if is_col:  # If the values are Excel-style column labels
            start = excel_column_to_index(start)
            end = max_value if end == 'end' else excel_column_to_index(end)
        else:
            start = int(start) - 1
            end = max_value if end == 'end' else int(end)
        return list(range(start, end))
    else:
        if is_col:  # This part is adjusted to handle single Excel column labels
            return [excel_column_to_index(value)]
        else:
            return [int(value) - 1]

#*! <%GTREE 5.1.3 auximiary converter function: data frame to dictionary getting rid of nulls%>
def dataframe_to_dict_without_nans(df):
    return [
        {key: value for key, value in row.items() if pd.notna(value)}
        for _, row in df.iterrows()
    ]

#*! <%GTREE 5.1.4 auximiary converter function: test settings definitions%>
def test_template_conversion_settings(settings_file_path, sheet_name, issues_list):
    # Try reading the settings sheet from the main workbook
    try:
        settings_df = pd.read_excel(settings_file_path, sheet_name)
        return settings_df, False
    except Exception as e:
        error_message = f"Error reading the settings sheet from the file [{settings_file_path}]: {e}"
        issues_list.append(error_message)
        return None, True


#*! <%GTREE 6 define reporting functions%>


#*! <%GTREE 7 define main function%>
def main():
    #*! <%GTREE 7.1 read command line parameters%>
    args=argumentparser()

    #*! <%GTREE 7.2 if we have excel template defined read it%>
    if args.FI_D_Excel_template_path:
        #*! <%GTREE 7.2.1 test the settings information%>
        error = True
        if error:
            settings_df, error = test_template_conversion_settings(args.FI_D_Excel_template_path, "settings", issues_list)
        if error:



#*! <%GTREE 8 execute main%>
if __name__ == "__main__":
    main()


#*============================   End Of File   ================================