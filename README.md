# Dengue Genome Analysis

A Django-based application for analyzing and managing dengue virus genome sequences. This project includes scripts for adding genome data from FASTA files, calculating nucleotide percentages, and managing genome entries in a database.

## Features

- Parse and analyze genome sequences from FASTA files
- Calculate nucleotide percentages (A%, T%, C%, G%, GC%)
- Manage genome entries in a Django database
- Avoid duplicate entries
- Remove specific or duplicate entries from the database

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dengue-genome-analysis.git
    cd dengue-genome-analysis
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the Django project:
    ```sh
    python manage.py migrate
    ```

## Usage

### Adding Genomes

To add genome data from a FASTA file, use the `add_genomes.py` script. You can specify a description for the genome entry.

```sh
python add_genomes.py

python remove_specific_entries.py

python remove_duplicates.py

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Contact
For any questions or inquiries, please contact yourname.

