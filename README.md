# OIMS
A Flexible, Extensible, Machine-Readable, Human-Intelligible, and Ontology-Agnostic Metadata Schema

### read me file metadata
Author: \[ \
  { \
          Author name: Gideon Kruseman \
          Author affiliation: Alliance Bioversity International & CIAT- CGIAR \
          Author email: g.kruseman@cgiar.org \
  } \
\] \
Date: 22 Decenmber 2023 \
published OIMS Version: 2.3 \
current OIMS version: 2.4 \
OIMS documentation version: 2.3.2 \
Status: current version validated and almost ready for use only thing missing is the persistent identity and AN update to the documentation to capture the latest improvements.

## Purpose
For enhancing data interoperability working towards the standardization on metadata is essential. OIMS is a lightweight, flexible, extensible, machine readable and human-intelligible metadata schema that does not depend on a specific ontology. The metadata schema for metadata of data files is based on the concept of data lakes where data is stored as they are. The purpose of the schema is to enhance data interoperability. The lack of interoperability of messy socio-economic datasets that contain a mixture of structured, semi-structured, and unstructured data means that many datasets are underutilized. Adding a minimum set of rich metadata and describing new and existing data dictionaries in a standardized way goes a long way to make these high-variety datasets interoperable and reusable and hence allows timely and actionable information to be gleaned from those datasets. The presented metadata schema OIMS can help to standardize the description of metadata. Kruseman (2022) introduces overall concepts of metadata, discusses design principles of metadata schemes, and presents the structure and an applied example of OIMS.

Building on that paper, this GitHub repository provides the underlying metadata schemas that are used for the operationalization of OIMS.

## version notes
Change log from 2.2.0.3 to 2.3.0.0

change to snake case: all properties in the OIMS base metadata schema have been converted to snake case. Moreover it is all lower case except for OIMS as a term in the attributes.
In OIMS_content.OIMS_content_object_properties. An intermediate level has been added, called metadata. OIMS_content_object_properties was an array of objects. It still is and one of those objects is “metadata” which is an array of objects, namely the metadatametadata. Other possible objects of OIMS_content_object_properties are entity identification and relevant entity relationships. These entity relationships are not relevant in the OIMS_base schema.
Entity related metadata is added to the metadata under "OIMS_content_object": "OIMS_Structure_Metadata".
Minor issues

Change log from 2.3.0.0 to 2.3.1.0

Ensured that mapping info in the main structure is an array of objects
Changed the name of the data-type “compound” to “compound_object”.
Ensured that all comments are an array of strings.
Changed the data-type “Controlled vocabulary” to “controlled_vocabulary”.
Ensured that OIMS_content_object sections were populated correctly. Not all attributes were mapped correctly.
“controlled_vocabulary_item” and “vocabulary_element_name” were used interchangeably. This has been made uniform using “vocabulary_element_name”. similarly for "controlled_vocabulary_item_description" and "vocabulary_element_description" the latter is used
There were some required in applicable attributes that were tagged with required. This has been remedied.
The attribute data_type is not multiple. In the case that more than one data type is allowed we have added the data type “any”
Minor edits of typos

Change log from 2.3.1.0 to 2.3.2.0

There were some missing elements related to the OIMS content properties that have been added for consistency.

Change log from 2.3.2.0 to 2.3.2.1

In OIMS 2.3.2.0 two typos were detected using a novel tool under development for OIMS consistency testing. Moreover, the json schema validation files were updated to reflect the changes in version 2.3.

Change to version 2.3.3 Improved tagging for entities and entity relationships.

Change to version 2.4 Added persistent identifiers to metadata schema section of the header to ensure greater FAIR-ness. Moreover, the url links are noiw completely machine readable. 


## Citation
When publishing papers based on the schema we encourage the authors to provide the link to the [github directory](https://github.com/ForesightInitiative/OIMS) and use the following citation: \
Kruseman G., LaPorte M.-A. 2023. A Flexible, Extensible, Machine-Readable, Human-Intelligible, and Ontology-Agnostic Metadata Schema (OIMS) version 2.3.2.0. https://github.com/ForesightInitiative/OIMS  

## Further reading / references
Kruseman G. 2022.A Flexible, Extensible, Machine-Readable, Human-Intelligible, and Ontology-Agnostic Metadata Schema (OIMS). _Frontiers in Sustainable Food Systems_ vol. 6. DOI=10.3389/fsufs.2022.767863  
