# OIMS version 2.2 technical documentation 


## User Guide for Developing OIMS-based metadata schemas and related Tools

**Gideon Kruseman<sup>1*</sup>**

<sup>1</sup> Alliance of Bioversity International and CIAT

<sup>*</sup> Corresponding author: [g.kruseman@cgiar.org](mailto:g.kruseman@cgiar.org) 

May 15, 2023



This working paper shares insights from work in progress by the CGIAR Foresight Initiative, and is shared for discussion. This paper has gone through a light review process at the initiative team leadership level and is shared with the approval of the relevant work package leader, but it has not been formally peer reviewed.

![WorkingPaperImage](https://github.com/ForesightAndMetrics/OIMS/assets/103105585/78e9825e-b558-49b5-ba7e-858a910eef1d)


The CGIAR Initiative on Foresight combines state-of-the-art analytics, innovative use of data, and close engagement with national, regional and global partners to offer better insights into alternative transformation pathways that can inform choices and sharpen decision-making today, leading to more productive, sustainable and inclusive food, land and water systems in the future. More information can be found at [https://www.cgiar.org/initiative/24-foresight-and-metrics-to-accelerate-inclusive-and-sustainable-agrifood-system-transformation/](https://www.cgiar.org/initiative/24-foresight-and-metrics-to-accelerate-inclusive-and-sustainable-agrifood-system-transformation/). 

**Acknowledgements**

This report was prepared by &lt;implementation team and affiliation(s) as needed> and financially supported by the CGIAR Initiative on Foresight and Metrics to Accelerate Food, Land and Water Systems Transformation. CGIAR is a global research partnership for a food-secure future, dedicated to transforming food, land, and water systems in a climate crisis. We would like to thank all funders who supported this research through their contributions to the CGIAR Trust Fund: [https://www.cgiar.org/funders/](https://www.cgiar.org/funders/) . 






## Table of Contents


1. [Introduction](#1-introduction)
2. [Context and Background](#2-context-and-background)
3. [High level structure of OIMS compatible metadata files](#3-high-level-structure-of-oims-compatible-metadata-files)
4. [Core properties](#4-core-properties)
5. [Required if applicable attributes](#5-required-if-applicable-attributes)
6. [Optional attributes](#6-optional-attributes)
7. [References](#7-references)
8. [Notes](#8-notes)



## 1. Introduction

The Open Ontology-Based Interoperable Information Asset Metadata Schema (OIMS) is a flexible and extensible metadata schema designed to standardize and organize metadata for various information assets like datasets, documents, models, and publications, making them more accessible, transparent, and reusable. To understand the importance of OIMS, let's first discuss some basic concepts.

In our data-driven world, we often deal with large amounts of information. To make sense of this information and use it efficiently, we need metadata. Metadata is like a label or a description that provides details about the data itself, making it easier to find, understand, and use.

Different industries and organizations use various standards to manage their data and metadata, which can create challenges when trying to share or combine data from multiple sources. These standards are often specific to certain contexts and can become outdated as the information landscape evolves.

To address these challenges, the OIMS approach focuses on standardizing the metadata's structure, rather than the data itself. Think of it as creating a common language for describing data, even if the data comes from different sources or domains. This common language helps ensure that the metadata remains flexible and adaptable, even as new attributes or changes occur over time.

Some efforts have been made to standardize general descriptive metadata, like DataCite and Dublin Core. However, more specialized metadata often lacks standardization, leading to inconsistencies across different data sources. This is where OIMS comes in, offering a standardized structure for the "metadata of the metadata."

In simpler terms, the OIMS approach is like creating a universal system for organizing information about data, regardless of where it comes from or how it's structured. By having a consistent way to describe and manage metadata, it becomes easier for people and organizations to share, understand, and reuse information assets in a more efficient manner.

The purpose of this document is twofold. The first purpose is to provide the technical documentation for the Ontology-based Information Asset Metadata Schema (OIMS). OIMS is a comprehensive and structured approach to managing and organizing valuable information assets. Designed with a strong foundation in ontology, OIMS ensures efficient organization and retrieval of data resources within complex information systems. By leveraging standardized metadata schema, OIMS promotes interoperability, consistency, and clarity across various data domains. Its adaptable and extensible structure allows for seamless integration into a wide range of applications, empowering organizations to harness the full potential of their information assets and drive data-driven decision-making processes.

The second purpose of this user guide, aimed at tech-savvy individuals, is to cover the essential aspects of working with OIMS, from understanding its structure to developing metadata schemas and related tools. The guide is structured into a number of chapters, which we describe briefly below.

The Chapter 2 "Context and Background" provides some background information and history that has led to the development of the OIMS approach to metadata.

The Chapter 3 "Understanding the OIMS Structure" discusses the high-level structure of OIMS. The structure is designed to be both human-intelligible and machine-readable, making it suitable for a variety of use cases. OIMS is a JSON-based schema consisting of two main sections:



1. "OIMS_Header": This section contains essential information about the metadata schemas and file descriptors used in the OIMS content objects. The most crucial part is the "MetadataSchema", which indicates which OIMS-compatible metadata schema describes the content of "OIMS_Content_Object_Properties".
2.  "OIMS_Content": This section has a structure that allows for a consistent and organized representation of different metadata components, making it easier to understand their relationships and extend the schema as needed.

This Chapter includes the JSON.schema rendering of an OIMS-compatible metadata file for validating OIMS-compatible metadata files.

In Chapter 4, we discuss the foundational OIMS self-describing metadata schema, and the following Chapter 5 we showcase a key example of how OIMS can be utilized for tagging valuable datasets. Specifically, we employ a standard template to capture metadata of datasets and their underlying data files, describing them using OIMS-compatible metadata. We then supply the metadata of this metadata, which is more comprehensive than the foundational metadata schema discussed in Chapter 4. As a final step, we describe the meta-metadata-metadata using the self-describing metadata schema.

In the following chapter 6 "Converting Metadata Files to OIMS-Compatible Format" discusses how Metadata files from various structured formats can be converted into OIMS-compatible metadata files. The conversion process requires describing the metadata fields with meta-metadata, using the OIMS self-describing metadata schema. It provides a description of the tools to used in the key example of Chapter 5.  

The next chapter 7 "Developing Querying Tools for OIMS" discusses key elements to consider when developing OIMS-compatible tools. When developing querying tools, consider the following:



1. Metadata extraction: Design tools that can efficiently extract metadata from the OIMS JSON structure, focusing on "OIMS_Content_Object_Properties" and the relationships between various metadata components.
2. Query optimization: Optimize queries for speed and performance by converting the nested OIMS JSON structure into a machine-readable format. This format should be optimized for querying but may not be as human-intelligible as the original JSON format.
3. Open-source tools: Utilize open-source tools for conversions to promote transparency and reproducibility.

The next chapter 8 "Developing Conversion Tools for OIMS" discusses how to create tools that can convert structured metadata files, such as CSV files, into OIMS-compatible JSON files, while maintaining the flexibility and extensibility of the OIMS schema.

The final Chapter 9 "Developing Analysis Tools for OIMS" discusses how to develop analysis tools that can work with OIMS-compatible metadata files to enhance the access, transparency, and use of information assets. These tools should be able to handle both the OIMS JSON format and the machine-readable format optimized for querying.

Each technical chapter consists of a summary, the actual content, and a section on the next steps envisioned by the OIMS development team. By following this user guide, you'll be better equipped to create tools that effectively enhance the accessibility, transparency, and usability of various information assets using the OIMS approach.





## 2. Context and Background

Metadata management plays a critical role in facilitating data discovery, sharing, and reuse in various domains. Metadata is essentially data about data, providing information that describes the content, structure, and context of a dataset. Metadata can include information such as title, description, keywords, author, date created, file format, and licensing terms as well as key information concerning the contents such as variables and their attributes.

Effective metadata management enables users to quickly and easily discover relevant data and metrics, data related tools and models, and the relevant documents. Metadata management enables user to determine if the data and related assets are suitable for their needs, and retrieve the relevant assets in a consistent and organized manner. It also supports interoperability between different datasets and systems, allowing data to be shared and reused across different domains and applications.

In addition, metadata management helps to ensure data quality and accuracy by providing information about the data source, processing methods, and any limitations or caveats associated with the data. This information is essential for researchers, policymakers, and other stakeholders to make informed decisions based on the data.

Organizations face various challenges in managing heterogeneous metadata across different systems and domains. These challenges can hinder the effective management and sharing of metadata, which is essential for facilitating data discovery, sharing, and reuse in various domains.

Five main challenges should be mentioned. The first is the lack of standardization (Borgman, 2012). Metadata is often created and managed differently by different organizations and systems, leading to a lack of standardization. This can make it difficult to share and integrate metadata across different systems. The second challenge is limited interoperability. In addition to the lack of standardization, limited interoperability between systems can also hinder the sharing and integration of metadata. Different systems may use different formats, structures, or vocabularies for metadata, making it difficult to exchange and merge metadata across different systems. The third challenge is data complexity. As the amount and complexity of data increase, it becomes more challenging to manage metadata effectively. For example, some data may be structured, while others may be unstructured, making it difficult to create a consistent metadata schema. The fourth challenge is the lack of metadata documentation. Metadata documentation is often limited or incomplete, making it difficult for other users to understand and use the metadata. This can lead to duplication of efforts and errors. The fifth key challenge is changes in data and metadata. As data and metadata change over time, it becomes challenging to maintain accurate and up-to-date metadata. This is especially true for large datasets that are frequently updated or revised.

OIMS was initially developed as a schema to provide both metadata and metadata of data dictionaries for messy structured and unstructured socio-economic datasets within the scope of the CGIAR Platform for Big Data in Agriculture (Kruseman, 2022). The goal was to create a lightweight, flexible, and extensible ontology-agnostic, machine-readable, and human-intelligible metadata schema to enhance the interoperability of datasets that historically, and for valid reasons, were not standardized, often lacking comprehensive metadata, and not interoperable or reusable in their current form. These messy datasets do not meet the FAIR requirements (Wilkinson, 2016) of open science. During the schema's development, the aim was to ensure that it would not only cater to the needs of social sciences but also enable interoperability with data from other fields.

The foundation of the OIMS approach to metadata management is the recognition that data are often not standardized. While standardization is desirable where possible, in many cases, standards become obsolete even before implementation. If datasets themselves cannot be standardized, the question arises whether it is possible to standardize data dictionaries. Standardizing metadata of data can help create the necessary interoperability to enhance the reusability of valuable datasets. In our data-driven world, datasets increasingly come with their metadata. Moreover, standardizing metadata can be difficult, as the type of metadata attached depends on the data's purpose. Consequently, data dictionary standardization is not always possible. However, metadata is data itself, so it should also have its metadata. This becomes interesting, as data dictionaries often lack accompanying metadata describing the data dictionary. Thus, our starting point was the development of metadata to describe data dictionaries (metadata). This meta-metadata can be described with metadata as well. Theoretically, this process could continue indefinitely. However, it soon becomes possible to describe the metadata with self-describing metadata, signifying that the foundational level has been reached.

OIMS uses the lightweight JSON annotation and has evolved since its initial publication (Kruseman, 2022) to be even more flexible. 





## 3. High level structure of OIMS compatible metadata files
###    3.1. Overview

In Figure 1 (below) we observe the high-level structure of OIMS which we will discuss shortly.[^1]



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.png "image_tooltip")


Fig 1. High level structure of OIMS 

Any OIMS-compatible metadata schema has the same high-level structure. “OIMS” is the root element of the JSON file. This indicates that it is an OIMS-compatible metadata file. The root element “OIMS” has two required objects: “OIMS_Header” and “OIMS_Content”. The OIMS header object has the purpose of providing information on the metadata of the metadata provided in the OIMS_Content section. Before diving in-depth into the main components of an OIMS-compatible JSON metadata file we will first discuss the concept or property of "OIMS_Content_Object".



 ###   3.2.  OIMS_Content_Object

The “OIMS_Content_Object” property is used in both the header and the content section of an OIMS file. In the OIMS content section it identifies the type of metadata that is covered by the metadata file. In the OIMS header section it identifies the underlying metadata schema that describes the metadadat in the OIMS_content section. In the OIMS header section “OIMS_Content_Object” appears twice. The first time is the link with the OIMS content section, which is especially important if there are multiple sets of metadata covered in the metadata file. The second time it occurs in the OIMS header it indicates which part of the OIMS content ion the underlying metadata file should be taken into account. 

The pros of this approach are:



1. Consistent design: Aligning the "OIMS_Content" section with the "OIMS_Header" section's design provides consistency across the schema, making it easier for users to understand and work with the schema.
2. Clearer organization: Grouping metadata components into "OIMS_Content_Object" with properties offers a more organized structure, clarifying how different metadata components are related.
3. Extensibility: This design allows for easier modification or extension of the schema in the future, as new metadata components or properties can be added without affecting existing implementations.

The cons of the approach that are important for development processes:



1. Increased complexity: The additional level of abstraction may make the schema more complex to read and understand, particularly for users who are not familiar with the concept.
2. Indirect access: Accessing metadata components requires navigating through the "OIMS_Content_Object" property, which may be less efficient than accessing it directly in an array.
3. Potentially slower querying: Queries and searches may be slower due to the need to navigate through the additional level of abstraction.
###    3.3. OIMS header
####        3.3.1. Main structure

The OIMS header object is denoted by "OIMS_Header" and comprises three components: "mapping_info," "MetadataSchema," and "FileDescriptors."

The most crucial component, "MetadataSchema," offers information on how to read the OIMS_Content section. Although we will discuss the "MetadataSchema" object in more detail shortly, let's briefly touch upon the other components. The "mapping_info" property indicates whether the metadata schema was filled in manually or by a machine or tool, and it specifies the non-human's characteristics.

The "FileDescriptors" component provides information about the metadata file itself. At a glance, users can determine if the file is a metadata file for a dataset, a model or ETL procedure, a document or document collection, or metadata of metadata. While the descriptor part is not essential for machine readability, it is crucial for human intelligibility. Furthermore, it supplies the contact details of the person, persons, or organization to contact regarding the metadata. It is important not to confuse the contact person with the data, model, or document owner for which the metadata is provided. The metadata provider can be entirely different from the asset owner. The metadata provider may work to enhance the findability and reusability of existing datasets and data-related assets, such as models, tools, or documents.



####        3.3.2. Mapping information
<span style="color: red;">work in progress</span>
####        3.3.3. Underlying metadata schema information
<span style="color: red;">work in progress</span>

####        3.3.4. Metadata file descriptors
<span style="color: red;">work in progress</span>

###    3.4. OIMS Content
<span style="color: red;">work in progress</span>


## 4. Core properties

The core properties are defined in the OIMS content section as metadata metadata. These core properties include:
[Comment attribute](#41--the-comment-property)
[Attribute name](#42-atrributename-the-identifier-of-the-property)
[Attribute description](#43-attributedescription-description-of-the-property)
[Data type](#44-datatype-the-datatype)
[Requirement level](#45-attribute-requirementlevel)
[Data type class](#46-attribute-datatypeclass)
[Multiple](#47-attribute-multiple)


### 4.1. “\\”:  the comment property

The "\\" property is an optional attribute that allows users to add comments, explanations, observations, or criticisms to the metadata. This attribute supports multiple values and can be expressed as plain text or HTML.

The following JSON code snippet illustrates the definition of the "\\" attribute in the OIMS schema:



<p id="gdcalert2" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image2.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert3">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image2.png "image_tooltip")


We now explain each key aspect of the "\\" property:



* **&lt;%GTREE 2.1 attribute \\ [comment] %>:** This GTREE tag allows the structured file to be browsed in a tree structure using the GTREE Integrated Development Environment (IDE). GTREE tags enable easier navigation and understanding of the schema structure.
* **"AttributeName": "\\"**: Specifies the attribute name, which is represented by "\". This naming convention is used to indicate that this attribute is meant for comments.
* **"AttributeDescription**": **"comment field"**: Provides a brief description of the attribute, stating that it is a comment field.
* **"Datatype**": **["text", "HTML"]:** Indicates that the attribute accepts values in two formats: plain text and HTML. This provides flexibility for users to add comments with or without HTML formatting.
* **"Status": "optional"**: Specifies that the comment field is optional, meaning that users may choose whether or not to include comments in the metadata.
* **"TypeClass": "primitive"**: Indicates that the attribute belongs to the "primitive" type class. Primitive attributes are basic data types that can be directly represented as a value.
* **"Multiple": "TRUE"**: States that multiple comments can be added to the metadata using the "\" attribute.
* **"OntologyTerm"**: Provides information about the corresponding ontology term for the attribute, which helps to standardize and align the attribute with existing ontologies. In this case, the "comment" term from the National Cancer Institute Thesaurus (NCIT) ontology is used, with the term ID "NCIT_C25393" and an exact match in term quality.
### 4.2. “AtrributeName”: the identifier of the property

The "AttributeName" property is a required attribute that serves as the identifier for a metadata field in the OIMS schema. This attribute is a string value, can appear only once for each metadata field, and belongs to the "primitive" type class.

The following JSON code snippet illustrates the definition of the "AttributeName" property in the OIMS schema:


```
       {
        "\\":"<%GTREE 2.2 attribute AttributeName %>",
        "AttributeName":"AttributeName",
        "AttributeDescription":"name of the data dictionary metadata field",
        "Datatype":"string",
        "Status":"required",
        "TypeClass":"primitive",
        "Multiple":"FALSE",
        "OntologyTerm": [
           {
              "OntologyTermName":"Name",
              "OntologyTermDescription":"The words or language units by which a thing is known.",
              "OntologyName":"NCIT",
              "OntologyTermID":"NCIT_C42614",
              "OntolgyURL":"http://purl.obolibrary.org/obo/NCIT_C42614",
              "OntologyTermQuality":"to be confirmed"
           }
        ]
       }
```


We now each key aspect of the "AttributeName" property:



* **&lt;%GTREE 2.2 attribute AttributeName %>:** Similar to the previous example, this GTREE tag is used to enable the browsing of the structured file in a tree structure using the GTREE Integrated Development Environment (IDE).
* **"AttributeName": "AttributeName"**: Specifies the attribute name, which is "AttributeName" in this case. This is the unique identifier for the metadata attribute.
* **"AttributeDescription": "name of the data dictionary metadata field":** Provides a brief description of the attribute, explaining that it represents the name of the metadata field in the data dictionary.
* **"Datatype": "string":** Indicates that the attribute accepts values in the string format. This means that the attribute name should be provided as a sequence of characters.
* **"Status": "required":** Specifies that the attribute is required, meaning that it must be included for every metadata field in the schema.
* **"TypeClass": "primitive":** Indicates that the attribute belongs to the "primitive" type class, which means it can be directly represented as a value.
* **"Multiple": "FALSE":** States that the attribute can only have a single value, ensuring that each metadata field has a unique name.
* **"OntologyTerm":** Provides information about the corresponding ontology term for the attribute. In this case, the "Name" term from the National Cancer Institute Thesaurus (NCIT) ontology is used, with the term ID "NCIT_C42614". However, the term quality is marked as "to be confirmed", indicating that the match between the ontology term and the attribute may need further validation.[^2]


 ### 4.3. “AttributeDescription”: description of the property

The "AttributeDescription" property is used to provide a clear and concise description of each metadata attribute in the OIMS schema. This attribute is required for all metadata fields to help users better understand the purpose and context of each property.

The following JSON code snippet illustrates the definition of the "AttributeDescription" property in the OIMS schema:



<p id="gdcalert3" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image3.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert4">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image3.png "image_tooltip")


each key aspect of the "AttributeDescription" property:



* **&lt;%GTREE 2.3 attribute AttributeDescription %>:** This GTREE tag is used to enable the browsing of the structured file in a tree structure using the GTREE Integrated Development Environment (IDE).
* **"AttributeName": "AttributeDescription":** Specifies the attribute name, which is "AttributeDescription" in this case. This attribute provides a brief description of each metadata field.
* **"AttributeDescription": "description of the data dictionary metadata field":** Offers a short explanation of the attribute, stating that it represents the description of the metadata field in the data dictionary.
* **"Datatype": "text":** Indicates that the attribute accepts values in the text format, allowing for more extended descriptions of metadata fields.
* **"Status": "required":** Specifies that the attribute is required, ensuring that a description is provided for every metadata field in the schema.
* **"TypeClass": "primitive":** Indicates that the attribute belongs to the "primitive" type class, which means it can be directly represented as a value.
* **"Multiple": "FALSE":** States that the attribute can only have a single value, ensuring that each metadata field has only one description.
* **"OntologyTerm"**: Provides information about the corresponding ontology term for the attribute. In this case, the "Description" term from the National Cancer Institute Thesaurus (NCIT) ontology is used, with the term ID "C25365". However, the term quality is marked as "to be confirmed", indicating that the match between the ontology term and the attribute may need further validation.[^3]


### 4.4. “DataType”: the datatype 

The "DataType" property is a required primitive type with a controlled vocabulary. It is used to specify the form that a value will have within the data dictionary metadata fields. The controlled vocabulary includes several terms to describe the possible datatypes (see code snippet below).



1. "string": For general textual data, including simple character strings.
2. "text": For more substantial amounts of alphanumeric characters or longer text.
3. "compound": For properties with an array of properties as values.
4. "date": For date values used in properties like version date.
5. "URI": For properties with URL or URI values.
6. "Controlled Vocabulary": For properties with values that are items in a controlled vocabulary, enumeration, or list.
7. "email": For properties with email address values.

The JSON code snippet also includes an ontology term for the "DataType" property itself. The term comes from the Dublin Core Metadata Initiative (DCMI) ontology, which is widely used for metadata representation. This term is an exact match for "DataType" and comes from the DCMI ontology. The controlled vocabulary and associated ontology terms ensure that the "DataType" property is well-defined and consistently used across the OIMS self-describing metadata schema.



<p id="gdcalert4" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image4.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert5">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image4.png "image_tooltip")




### 4.5. Attribute “RequirementLevel”

The attribute requirement level indicates if an attribute is required, recommended or optionaleither always or when applicable.



### 4.6. Attribute DataTypeClass: 

Metadata fields in a system can be classified into two main classes: primitive and compound. The classification is based on the nature of the attribute's data type and structure.

In the case of primitive data types, a metadata attribute represents a single value of a specific data type. This means that the attribute holds a singular piece of information without any complex structure. Examples of primitive data types include integers, floating-point numbers, strings, booleans, and dates. These data types are indivisible and cannot be further broken down into sub-attributes.

On the other hand, compound data types indicate that the metadata attribute is composed of multiple sub-attributes, each having its own specified data type. In this case, the attribute represents a more complex structure that consists of several interconnected pieces of information. Compound attributes are often used when there is a need to capture and organize multiple related aspects or properties of a certain entity. The sub-attributes within a compound attribute can be of any valid data type, including both primitive and other compound types.

For instance, consider a metadata field representing a person's address. If the address is stored as a compound attribute, it could consist of sub-attributes such as street, city, state, and postal code. Each sub-attribute would have its own data type (e.g., street as a string, city as a string, state as a string, and postal code as an integer), forming a composite structure within the address attribute.

In summary, metadata fields can be classified as primitive or compound based on the nature of their data types. Primitive data types represent single values of specific types, while compound data types indicate attributes composed of multiple sub-attributes, each with its own specified data type. This classification allows for the representation of both simple and complex metadata structures in a system.



### 4.7. Attribute Multiple

Multiple is a Boolean that takes on the value true or false. If set to true it means the attribute being described can have multiple values. The attribute "multiple" is a common characteristic found in certain metadata fields. It refers to the ability of an attribute to hold multiple values instead of just a single value. When an attribute is marked as "multiple," it signifies that it can accommodate more than one occurrence or instance of the associated data.

The use of the "multiple" attribute is particularly relevant in situations where there is a need to capture and store a variable number of values for a specific attribute. This flexibility allows for the representation of scenarios where multiple options or choices are applicable.

For instance, consider a metadata field called "Tags" for categorizing articles. If the "Tags" attribute is designated as "multiple," it means that a single article can have multiple tags associated with it. This allows for a more comprehensive classification system, where an article can be tagged with various topics or keywords, enhancing searchability and organization.

In practical terms, the "multiple" attribute can be implemented in different ways depending on the specific system or data model being used. It may involve storing the multiple values as an array, a list, or through other suitable data structures.

In summary, the attribute "multiple" signifies that a metadata field can hold multiple values instead of just one. It is used to represent scenarios where multiple occurrences or options are applicable for a given attribute, allowing for greater flexibility and richer data representation.





## 5. Required if applicable attributes
### 5.1. Controlled vocabulary

If the data type of an attribute is a controlled vocabulary, list, enumeration or well-defined factor, then the controlled vocabulary elements need to be specified. Especially at higher levels of abstraction (metametadata), these controlled vocabulary elements need to be well described in unambiguous terms. Controlled vocabulary attribute is a compound type with controlled vocabulary item name “ControlledVocabularyItem” and a description "ControlledVocabularyItemDescription". Ideally, the controlled vocabulary terms come with ontology terms attached to them.



### 5.2. Ontology terms

Ontology terms play a crucial role in knowledge representation and organization within various domains. They serve as building blocks for creating structured and meaningful relationships between concepts, entities, and attributes. Here are several reasons why ontology terms are important:



1. Consistent and standardized vocabulary: Ontology terms provide a common and agreed-upon vocabulary for a specific domain. They establish a standard language that ensures consistency and clarity when describing and discussing domain-specific concepts. This facilitates effective communication among stakeholders, researchers, and systems operating within the domain.
2. Semantic interoperability: Ontology terms enable semantic interoperability by capturing the meaning and relationships between concepts. They go beyond simple textual representation and provide a rich semantic structure that allows for better understanding, integration, and exchange of information across different systems, databases, and applications. Ontology terms enable data integration and facilitate knowledge sharing, making it easier to combine and analyze information from diverse sources.
3. Knowledge organization and retrieval: Ontology terms provide a structured framework for organizing and categorizing knowledge. They allow for the hierarchical classification of concepts and the establishment of relationships such as subclass-superclass or part-whole relationships. This structured organization enhances the ability to locate, retrieve, and navigate relevant information within a domain. Ontology terms can serve as a backbone for effective search engines, recommendation systems, and data exploration tools.
4. Reasoning and inference: Ontology terms enable logical reasoning and inference capabilities. By defining relationships, constraints, and rules, ontologies provide a foundation for automated reasoning systems to make deductions, draw conclusions, and infer new knowledge. This reasoning ability is valuable in various domains such as healthcare, finance, and artificial intelligence, where complex relationships and decision-making processes are involved.
5. Domain understanding and knowledge sharing: Ontology terms facilitate a deeper understanding of a domain by capturing its underlying concepts, properties, and relationships. They serve as a means to capture expert knowledge, domain expertise, and best practices. Ontologies provide a shared representation that allows experts and practitioners to capture, document, and share their knowledge in a structured and reusable manner, fostering collaboration and learning within the domain.

Overall, ontology terms are important for establishing a common vocabulary, enabling semantic interoperability, organizing knowledge, supporting reasoning and inference, and facilitating domain understanding and knowledge sharing. They are a powerful tool for structuring and leveraging information within complex domains, improving data integration, and enhancing decision-making processes.

In the OIMS framework, the compound attribute "OntologyTerm" encompasses several sub-attributes that collectively provide detailed information about a specific term within an ontology. The sub-attributes associated with the "ontology term" compound attribute include "OntologyTermName," "OntologyTermDescription," "OntologyName," "OntologyTermID," "OntologyURL," and "OntologyTermQuality." Each of these sub-attributes serves a distinct purpose in describing and contextualizing the ontology term.

The "OntologyTermName" sub-attribute represents the actual name or label assigned to the ontology term. It serves as a human-readable identifier that succinctly captures the essence of the term. For example, if the ontology term refers to a specific biological process, the "OntologyTermName" could be "Cell Cycle" or "Photosynthesis."

The "OntologyTermDescription" sub-attribute provides a more comprehensive explanation or definition of the ontology term. It offers additional context, clarifying the meaning, scope, and characteristics of the term. This description helps users and systems understand the purpose and significance of the ontology term within the broader ontology.

The "OntologyName" sub-attribute specifies the name of the ontology to which the term belongs. Ontologies are knowledge frameworks that organize and define concepts within a particular domain. The "OntologyName" sub-attribute establishes the context and source of the term, enabling users to locate and reference the relevant ontology.

The "OntologyTermID" sub-attribute represents a unique identifier assigned to the ontology term within its respective ontology. This identifier serves as a globally unique reference that allows for precise identification and retrieval of the term. It facilitates integration and linking of information across different systems and datasets.

The "OntologyURL" sub-attribute provides a URL or web address pointing to the location of the ontology term within the ontology hierarchy. This link allows users to access further information, navigate the ontology, and explore related terms and concepts. The "OntologyURL" enhances the usability and accessibility of the ontology term within digital environments.

The "OntologyTermQuality" sub-attribute captures the quality or reliability of the ontology term. It can include metrics, ratings, or assessments that reflect the accuracy, completeness, or consensus regarding the term. This sub-attribute helps users evaluate the trustworthiness and appropriateness of the ontology term for their specific needs.

In summary, the compound attribute "ontology term" consists of sub-attributes such as "OntologyTermName," "OntologyTermDescription," "OntologyName," "OntologyTermID," "OntologyURL," and "OntologyTermQuality." These sub-attributes collectively provide a comprehensive description of a term within an ontology, including its name, definition, ontology association, unique identifier, URL location, and quality assessment. This compound attribute enables precise and detailed representation of ontology terms, supporting effective knowledge organization, retrieval, and sharing within the domain.



### 5.3. Attribute value elements

If an attribute is of the type compound and elements of the attribute are fixed, then the elements should be identified in the metametadata. The attribute “AttributeValueElements” captures the sub-attributes that are part of a compound attribute.

When an attribute is classified as a compound type and its elements are fixed, it is important to identify and document those elements in the metametadata. The metametadata refers to the metadata that describes the structure and organization of the metadata itself. 

To capture the sub-attributes that make up a compound attribute with fixed elements, the attribute "AttributeValueElements" is utilized. This attribute serves as a container or list that explicitly enumerates the sub-attributes that are associated with the compound attribute. By including the "AttributeValueElements" attribute in the metametadata, it becomes possible to define and document the specific elements that compose the compound attribute.

For example, let's consider a compound attribute called "Address" that consists of fixed sub-attributes such as "Street," "City," "State," and "PostalCode." In the metametadata, the "AttributeValueElements" attribute would be employed to list these sub-attributes explicitly. The value of the "AttributeValueElements" attribute would be a collection or array containing the names or identifiers of the sub-attributes, in this case, "Street," "City," "State," and "PostalCode."

By including the "AttributeValueElements" attribute in the metametadata, the structure and composition of compound attributes can be documented and understood. This information proves useful for data validation, data modeling, and system interoperability, as it provides a clear specification of the sub-attributes that are expected within a compound attribute.

In summary, the "AttributeValueElements" attribute is used in the metametadata to identify and document the sub-attributes that comprise a compound attribute with fixed elements. It allows for the explicit listing of these elements, providing valuable information for data management and system integration.





## 6. Optional attributes
### 6.1. “DefaultValue”: Default value of an attribute if a value is not provided

In this section, we discuss the "DefaultValue" property, which defines the default value of an attribute if it is not set in the metadata. The provided screenshot shows the corresponding JSON code snippet:



<p id="gdcalert5" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image5.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert6">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image5.png "image_tooltip")


The "DefaultValue" property is a recommended primitive type if applicable, with a datatype of "text". It allows for the specification of a default value for an attribute when the value is not explicitly provided in the metadata. This can be particularly useful for attributes with optional values, where a default value may be needed for consistency or when certain values are more commonly used. The "DefaultValue" property can have multiple values, allowing for a range of default values to be provided for a given attribute when necessary.

For the "DefaultValue" property, an ontology term from the QUDT (Quantities, Units, Dimensions, and Data Types) ontology can be used. The QUDT ontology term for "DefaultValue" provides an exact match for the property's intended usage in the context of the OIMS metadata schema.



### 6.2. “ValueReservedWords”: reserved words in text fields

In this section, we discuss the "ValueReservedWords" property and its sub-properties, "ReservedWordName" and "ReservedWordDescription". These properties define reserved words that have a special meaning in the context of the attribute and are not covered by Controlled Vocabulary. The provided screenshot shows the corresponding JSON code snippet below.

The "ValueReservedWords" property is a compound datatype, recommended if applicable, and can have multiple values. Its attribute value elements include "ReservedWordName" and "ReservedWordDescription".

The "ReservedWordName" property is a required primitive type if applicable and has a "text" datatype. It represents the reserved word itself. The "ReservedWordDescription" property is a recommended primitive type if applicable, with a "text" datatype, and it provides a definition for the reserved word in the context of the attribute.



<p id="gdcalert6" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image6.png). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert7">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image6.png "image_tooltip")


Regarding ontology terms for "ValueReservedWords", "ReservedWordName", and "ReservedWordDescription", to date, we could not find suitable ontology terms that match these properties' intended usages. These concepts are quite specific to the context of the OIMS metadata schema, and there might not be general ontology terms that cover them. We have also checked for close matches, but no appropriate ontology term was found.



### 6.3. The attribute content object

The attribute "ContentObjects" is another attribute somewhat comparable to “attributeValueElements” that consists of two sub-attributes: "AllowedContentObjects" and "AllowedContentRule". These sub-attributes define the rules and restrictions associated with the content objects allowed within a certain context or system.

The "AllowedContentObjects" sub-attribute specifies the list or set of content objects that are permitted or allowed within the given context. It can be a controlled vocabulary, an enumeration, or any other defined set of values that represent the acceptable content objects. This sub-attribute serves as a reference for determining which content objects are valid within the system.

The "AllowedContentRule" sub-attribute, on the other hand, is a compound attribute that further refines the constraints for content objects. It consists of two additional attributes: "AllowedContentRuleType" and "AllowedContentRuleNumber".

The "AllowedContentRuleType" is a controlled vocabulary attribute that indicates the type of rule applied to the allowed content objects. It typically takes on values from a predefined list of options, in this case, "AtLeast", "AtMost", and "Exactly". These values define the specific conditions that must be met regarding the number of content objects allowed.

If the "AllowedContentRuleType" is either "AtLeast" or "AtMost", the "AllowedContentRuleNumber" attribute is used. This attribute specifies an integer value that provides additional context to the rule. For example, if the "AllowedContentRuleType" is "AtLeast", the "AllowedContentRuleNumber" could specify the minimum number of content objects required. Similarly, if the "AllowedContentRuleType" is "AtMost", the "AllowedContentRuleNumber" could specify the maximum number of content objects allowed.

By using the "AllowedContentObjects" and "AllowedContentRule" sub-attributes together, it becomes possible to define and enforce specific rules regarding the content objects that are allowed within a given system or context. This structured approach helps ensure consistency, validation, and adherence to defined criteria for content management and data processing.

In summary, the "ContentObjects" attribute consists of sub-attributes "AllowedContentObjects" and "AllowedContentRule". "AllowedContentObjects" specifies the valid content objects, while "AllowedContentRule" refines the restrictions by incorporating the "AllowedContentRuleType" and "AllowedContentRuleNumber" attributes. This structure facilitates the definition and enforcement of rules for content object management and processing.





## 7. References

<!-- Footnotes themselves at the bottom. -->


## 8. Notes

[^1]:
     [https://github.com/ForesightAndMetrics/OIMS/blob/main/BasicSchemas/OIMS_structure.json](https://github.com/ForesightAndMetrics/OIMS/blob/main/BasicSchemas/OIMS_structure.json) 

[^2]:

     To determine whether the ontology term is correct, we need to evaluate if the selected term from the National Cancer Institute Thesaurus (NCIT) ontology accurately represents the meaning and context of the "AttributeName" property in the OIMS schema.
    The "AttributeName" property is used to specify the unique identifier or name for each metadata attribute in the OIMS schema. It is a required field and should be provided as a string. Iit appears that the "Name" term from the NCIT ontology could be suitable for the "AttributeName" property. The term description, "The words or language units by which a thing is known," aligns with the purpose of the "AttributeName" property in the OIMS schema, which serves as the unique identifier or name for metadata attributes.
    However, it is essential to note that ontologies are domain-specific, and NCIT is primarily focused on cancer research and related biomedical fields. The use of a more general or domain-agnostic ontology, such as Dublin Core Metadata Initiative (DCMI) or Schema.org, might be more appropriate for the "AttributeName" property. However, neither Dublin Core Metadata Initiative (DCMI) nor Schema.org appears to have a specific ontology term that directly matches the "AttributeName" property in the OIMS schema.
    Dublin Core Metadata Initiative (DCMI):
    DCMI provides a set of 15 core elements to describe a wide range of resources. However, none of the DCMI core elements seem to match the concept of the "AttributeName" property directly. The core elements focus on describing the resource itself rather than describing metadata attributes or their naming conventions.
    Schema.org:
    Schema.org is a collaborative, community activity that maintains a collection of schemas for structured data on the internet. While Schema.org offers a rich vocabulary for describing various entities and their properties, it does not have a specific term that would directly correspond to the "AttributeName" property in the OIMS schema. Schema.org focuses on describing entities and their relationships, rather than metadata attribute naming conventions.
    In summary, the "Name" term from the NCIT ontology, with the term description "The words or language units by which a thing is known," might still be the closest match, despite the domain-specific focus of the NCIT ontology.

[^3]:

     1. National Cancer Institute Thesaurus (NCIT): The selected ontology term "Description" from NCIT seems to be a suitable choice for the "AttributeDescription" property in the OIMS schema, as it accurately captures the concept of providing a written or verbal explanation of something.
    2. Dublin Core Metadata Initiative (DCMI): DCMI provides a term called "Description" as one of its 15 core elements. The Dublin Core "Description" element is defined as "An account of the resource." While this term aligns with the purpose of the "AttributeDescription" property, it is mainly used for describing resources rather than metadata attributes. Thus, it may not be the best fit in this context.
    3. Schema.org: Schema.org has a property called "description" that is defined as "A description of the item." The Schema.org "description" property is used to describe various entities and their properties, making it a possible candidate for the "AttributeDescription" property. However, it is important to note that Schema.org is primarily designed for describing web content and its relationships, not specifically metadata attributes or schemas.
    4. Friend of a Friend (FOAF) Ontology: For "AttributeDescription": Similar to "AttributeName," there is no direct term in FOAF that corresponds to the concept of an attribute description. The "mbox" property could be considered, which represents an "Email address of a person, group, or organization," but this term is not a suitable match for the "AttributeDescription" property.
    5. Simple Knowledge Organization System (SKOS) Ontology: For "AttributeDescription": The "scopeNote" property in SKOS might be applicable, which is defined as "A note that helps to clarify the meaning, context or proper usage of a concept." This term aligns with the purpose of providing a description for metadata attributes. However, it is important to note that this term is primarily intended for describing concepts within controlled vocabularies and not specifically metadata attributes.
    While more general ontologies offer potential terms for the "AttributeDescription" property, they may not be the best fit for the specific context of OIMS schema. The NCIT ontology terms previously discussed are more aligned with the purpose and context of the OIMS schema properties.
