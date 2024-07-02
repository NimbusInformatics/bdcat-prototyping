# Data Model Exploration

This project aims to explore data models in Gen3 and LinkML format, extract attributes of each table, and generate a relatedness score for each table pair based on semantic comparison of concepts.

## Setup

### Step 1: Install Conda

If you don't already have Conda installed, you can download and install it from the Miniconda or Anaconda website.

### Step 2: Create a Conda Environment

Open a terminal or command prompt.
Create a new Conda environment:

```bash
conda create --name datamodelcomp python=3.9
```

Replace datamodelcomp with the name you want to give your environment.

Activate the Conda environment:
```bash
conda activate datamodelcomp
```

### Step 3: Install Dependencies with Pip

Once the environment is activated, you can install the required dependencies using pip.

Install pip if it's not already installed:

```bash
conda install pip
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Parsing Data Models

To parse data models in Gen3 and LinkML format, follow these steps:

1. Install the necessary dependencies.
2. Define a parser class for each data model format.
3. Implement the parsing logic for each parser class.
4. Test the parsers with sample data models.

## Extracting Attributes

To extract attributes of each table, use the following approach:

1. Parse the data models using the previously defined parsers.
2. Traverse the parsed data models to identify tables and their attributes.
3. Store the extracted attributes in a suitable data structure for further processing.

## Semantic Comparison and Relatedness Score

To semantically compare concepts and generate a relatedness score for each table pair, follow these steps:

1. Define a similarity metric for comparing concepts.
2. Iterate over each pair of tables.
3. Extract the concepts from each table's attributes.
4. Calculate the semantic similarity between the concepts using the defined metric.
5. Assign a relatedness score to each table pair based on the calculated similarity.

## Usage

To use this project, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Run the main script to parse data models, extract attributes, and generate relatedness scores.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
