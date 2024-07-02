import requests
import yaml
import pandas as pd
import sys

def fetch_and_parse_linkml_schema(url):
    # Fetch the content of the LinkML schema file
    response = requests.get(url)
    schema_yaml = response.text

    # Load the YAML content
    schema = yaml.safe_load(schema_yaml)
    return schema

def extract_attributes(schema, table_name):
    classes = schema.get('classes', {})
    if table_name not in classes:
        print(f"Table '{table_name}' not found in the schema.")
        return []

    attributes = classes[table_name].get('attributes', {})
    table = []

    if isinstance(attributes, list):
        print(f"Warning: Expected a dictionary for attributes of '{table_name}', but got a list. Details: {attributes}")
        new_attributes = {}
        for item in attributes:
            if isinstance(item, dict):
                for name in item.keys():
                    item_name = name
                    item_range = item[name].get('range', 'unknown')
                    item_description = item[name].get('description', '').strip()
                    new_attributes[item_name] = {'range': item_range, 'description': item_description}
            else:
                print(f"Warning: Skipping item {item} because it is not a dictionary or lacks a 'name' key.")
        attributes = new_attributes

    for name, details in attributes.items():
        if isinstance(details, dict):
            attr_type = details.get('range', 'unknown')
            description = details.get('description', '').strip()
        else:
            print(f"Warning: Expected a dictionary for attribute '{name}', but got {type(details)}")
            attr_type = 'unknown'
            description = ''
        table.append((name, attr_type, description))

    return table

def main(url, table_name):
    # Fetch and parse the schema
    schema = fetch_and_parse_linkml_schema(url)

    # Extract attributes for the specified table
    attributes_table = extract_attributes(schema, table_name)

    # Create a DataFrame
    attributes_df = pd.DataFrame(attributes_table, columns=['Attribute Name', 'Type', 'Description'])

    # Output the DataFrame to a TSV file
    output_file = f'{table_name}_attributes.tsv'
    attributes_df.to_csv(output_file, sep='\t', index=False)

    print(f"Attributes table for '{table_name}' has been written to {output_file}")

if __name__ == "__main__":
    # URL for the LinkML schema file
    linkml_schema_url = "https://raw.githubusercontent.com/bfurner/bdchm/eace35242e686da61e8e4c4198639fd8dadae408/src/bdchm/schema/bdchm.yaml"

    # Table name to extract attributes from
    table_name = "ResearchStudy"

    main(linkml_schema_url, table_name)

