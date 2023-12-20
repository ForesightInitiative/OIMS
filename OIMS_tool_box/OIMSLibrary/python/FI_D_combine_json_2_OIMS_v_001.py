#*<%REGION File header%>
#*=============================================================================
#* File      : FI_D_combine_json_2_OIMS_v_001.py
#* Author    : Gideon Kruseman <g.kruseman@cgiar.org>
#* Version   : 1.0
#* Date      : 10/26/2023 11:34:46 AM
#* Changed   :
#* Changed by:
#* Remarks   :
"""
*! <%GTREE 0 tool documentation%>
This tool is part of the toolbox that has been designed to convert the foresight initiative dataset metadata
template in EXCEL into an OIMS-compatible json metadata file.

The way it has been designed is to be as generic as possible to allow other templates
that contain metadata to be converted to OIMS

This component is specifically focussed on data and metrics metadata.

This component does the following:
1. it creates the OIMS compatible metadata file structure
2. fills it with relevant information collected through templates and other sources


*! <%GTREE 0.1 technical information%>
language: python
version: 1.0.0
data: October 2023
author: Gideon Kruseman <g.kruseman@cgiar.org>

*! <%GTREE 0.2 input%>

*! <%GTREE 0.3  command line parameters%>
*! <%GTREE 0.3.1 required command line paremers%>
--template_in_json_fp                  : The path to the json file of the converted template using the tool FI_convert_template_v_001.py  version 1.0.0

*! <%GTREE 0.3.2 optional command line parameters%>
--dataverse_descriptive_dataset_fp     : the path to the json file with extracted dataverse metadata
--dataverse_descriptive_dataset_vers   : version of the structure of the json file of dataverse metadata
             valid values :    cimmyt2023
--stata_structural_fp                  : the path to the json file with extracted information using get_stata_metadata.R version 1.0.0

*! <%GTREE 0.4  description of the script%>
*_ Initialization:

The script starts by initializing necessary libraries and checking command-line arguments for the main file path,
settings file path, and output file path.

*_ Functions:


"""
#
#
#
#*=============================================================================
#*<%/REGION File header%>
#*! <%GTREE 1 initialization%>
#*! <%GTREE 1.1 import libraries%>
import json
import argparse
import os

#*! <%GTREE 1.2 Check command line arguments %>
#
parser = argparse.ArgumentParser(description='Script to process Excel data.')

parser.add_argument('--argument', help='placeholder')
parser.add_argument('--template_in_json_fp', required= True, help='path to the json file of the converted template')
parser.add_argument('--dataverse_descriptive_dataset_fp', help='path to the json file with extracted dataverse metadata')
parser.add_argument('--dataverse_descriptive_dataset_vers', default='cimmyt2023', help='version of the structure of the json file of dataverse metadata')
parser.add_argument('--stata_structural_fp', help='path to the json file with extracted stata metadata')

args = parser.parse_args()


#*! <%GTREE 2 define functions%>
#*! <%GTREE 2.1 initiate_OIMS_foresight_schema%>
def initiate_OIMS_foresight_schema() :
    json_schema = {
        "OIMS":{
            "OIMS_header":{
                "mapping_info": [{}],
                "meta_data_schema": [
                    {
                        "OIMS_content_object": "Structural",
                        "schema_properties": [
                            {
                                "schema_name": "OIMS_FMI_data_1_5",
                                "schema_description": "OIMS foresight initiative metadata schema for data and metrics",
                                "schema_type": "datadictionary and data set metadata metadata schema",
                                "schema_version": "1.5.0.0",
                                "schema_url": "https://raw.githubusercontent.com/GideonKruseman/OIMStest/main/schemas/OIMS_base.json",
                                "OIMS_content_object": "MetadataMetadata",
                                "include_property": [
                                    "ALL"
                                ]
                            }
                        ]
                    }
                ]
            },
            "OIMS_content":[
                {
                    "OIMS_content_object":"descriptive_metadata_dataset",
                    "OIMS_content_object_properties":{
                        "Persistent_Entity_ID":[{}],
                        "Entity_Relastionship":[{}],
                        "Metadata":[{}]
                    }

                }
            ]
        }
    }
    return json_schema

#*! <%GTREE 2.1 initiate_OIMS_foresight_schema%>
def add_mapping_info(mapper_tool_name, mapper_tool_version, mapper_tool_url):
    mapping_info_instance = {
        "mapper_tool_name": mapper_tool_name,
        "mapper_tool_version": mapper_tool_version,
        "mapper_tool_url": mapper_tool_url
    }
    return mapping_info_instance

#*! <%GTREE 3 build the OIMS compatible metadata file%>
#*! <%GTREE 3.1 create OIMS metadata file as dictionary%>
OIMS_metadata_dictionary = initiate_OIMS_foresight_schema()

#*! <%GTREE 3.1 add OIMS_header information%>
OIMS_metadata_dictionary[OIMS][OIMS_header][mapping_info].append(
    add_mapping_info("FI_convert_template_v_001.py","1.0.0","https://github.com/ForesightInitiative/OIMS/tools/OIMS_tool_box")
)

print(OIMS_metadata_dictionary)
#*============================   End Of File   ================================