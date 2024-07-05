import requests
import yaml
import pandas as pd
import sys
import argparse

# URL for the Gen3 study.yaml file
gen3_study_url = "https://raw.githubusercontent.com/uc-cdis/gtex-dictionary/master/gdcdictionary/schemas"

# Function to parse the schema and create a two-column table with property name and type
def extract_properties(schema):
    properties = schema.get('properties', {})
    system_properties = schema.get('systemProperties', [])
    table = []
    
    # Extract properties
    for name, details in properties.items():
        if isinstance(details, dict):
            prop_type = details.get('type', 'dict')
            prop_desc = details.get('description', 'desc')
        else:
            print(f"Warning: Expected a dictionary for property '{name}', but got {type(details)}")
            prop_type = type(details)
            prop_desc = 'desc'
        table.append((name, prop_type, prop_desc.strip()))
    
    # Extract system properties
    for name in system_properties:
        table.append((name, 'system_prop', ''))
    
    return table

def main(url, table_name):

    # Fetching the content of the study.yaml file
    gen3_study_response = requests.get(url+"/"+table_name+".yaml")
    gen3_study_yaml = gen3_study_response.text

    # Loading the YAML content
    gen3_study = yaml.safe_load(gen3_study_yaml)

    # Extract properties from Gen3 study schema
    gen3_properties_table = extract_properties(gen3_study)

    # Creating a DataFrame
    gen3_properties_df = pd.DataFrame(gen3_properties_table, columns=['Property Name', 'Type', 'Description'])

    # Displaying the DataFrame
    print(gen3_properties_df)

    # Outputting the DataFrame to a TSV file
    output_file = f'outputs/gen3_{table_name}_attributes.tsv'
    gen3_properties_df.to_csv(output_file, sep='\t', index=False)

    print(f"Properties table has been written to {output_file}")


if __name__ == "__main__":
 
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Extract attributes from a Gen3 data model schema.')

    # Add the table name argument
    parser.add_argument('--entity', type=str, help='Name of the table to extract attributes from')

    # Parse the command line arguments
    args = parser.parse_args()

    # Extract the table name from the parsed arguments
    table_name = args.entity

    # Run the main function
    main(gen3_study_url, table_name)