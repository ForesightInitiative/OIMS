# User Guide for Developing OIMS-based metadata schemnas and related Tools
version 2.2
Gideon Kruseman

## Introduction:
The Open Ontology-Based Interoperable Information Asset Metadata Schema (OIMS) is a flexible and extensible metadata schema designed to standardize and organize metadata for various information assets like datasets, documents, models, and publications, making them more accessible, transparent, and reusable. To understand the importance of OIMS, let's first discuss some basic concepts.
In our data-driven world, we often deal with large amounts of information. To make sense of this information and use it efficiently, we need metadata. Metadata is like a label or a description that provides details about the data itself, making it easier to find, understand, and use.
Different industries and organizations use various standards to manage their data and metadata, which can create challenges when trying to share or combine data from multiple sources. These standards are often specific to certain contexts and can become outdated as the information landscape evolves.
To address these challenges, the OIMS approach focuses on standardizing the metadata's structure, rather than the data itself. Think of it as creating a common language for describing data, even if the data comes from different sources or domains. This common language helps ensure that the metadata remains flexible and adaptable, even as new attributes or changes occur over time.
Some efforts have been made to standardize general descriptive metadata, like DataCite and Dublin Core. However, more specialized metadata often lacks standardization, leading to inconsistencies across different data sources. This is where OIMS comes in, offering a standardized structure for the "metadata of the metadata."
In simpler terms, the OIMS approach is like creating a universal system for organizing information about data, regardless of where it comes from or how it's structured. By having a consistent way to describe and manage metadata, it becomes easier for people and organizations to share, understand, and reuse information assets in a more efficient manner.

This user guide, aimed at tech-savvy individuals, covers the essential aspects of working with OIMS, from understanding its structure to developing metadata schemas and related tools. The guide is structured into the following chapters: The chapter "Understanding the OIMS Structure" discusses the high-level structure of OIMS. The structure is designed to be both human-intelligible and machine-readable, making it suitable for a variety of use cases. OIMS is a JSON-based schema consisting of two main sections:

1. "OIMS_Header": This section contains essential information about the metadata schemas and file descriptors used in the OIMS content objects. The most crucial part is the "MetadataSchema", which indicates which OIMS-compatible metadata schema describes the content of "OIMS_Content_Object_Properties".
2. "OIMS_Content": This section has a structure that allows for a consistent and organized representation of different metadata components, making it easier to understand their relationships and extend the schema as needed.

The following chapter "Converting Metadata Files to OIMS-Compatible Format" discusses how Metadata files from various structured formats can be converted into OIMS-compatible metadata files. The conversion process requires describing the metadata fields with meta-metadata, using the OIMS self-describing metadata schema. In this Chapter the core elements of the OIMS base self-describing metadata schema are discussed in-depth. The Chapter also discusses how the nesting of schemas works and how to minimize the lnesting levels.

The next chapter "Developing Querying Tools for OIMS" discusses key elements to consider when developing OIMS-compatible tools. When developing querying tools, consider the following:

1. Metadata extraction: Design tools that can efficiently extract metadata from the OIMS JSON structure, focusing on "OIMS_Content_Object_Properties" and the relationships between various metadata components.
2. Query optimization: Optimize queries for speed and performance by converting the nested OIMS JSON structure into a machine-readable format. This format should be optimized for querying but may not be as human-intelligible as the original JSON format.
3. Open-source tools: Utilize open-source tools for conversions to promote transparency and reproducibility.

The next chapeter "Developing Conversion Tools for OIMS" discusses how to create tools that can convert structured metadata files, such as CSV files, into OIMS-compatible JSON files, while maintaining the flexibility and extensibility of the OIMS schema.

The final Chapter "Developing Analysis Tools for OIMS" discusses how to develop analysis tools that can work with OIMS-compatible metadata files to enhance the access, transparency, and use of information assets. These tools should be able to handle both the OIMS JSON format and the machine-readable format optimized for querying.

Each chapter consists of a summary, the actual content, and a section on the next steps envisioned by the OIMS development team. By following this user guide, you'll be better equipped to create tools that effectively enhance the accessibility, transparency, and usability of various information assets using the OIMS approach.
