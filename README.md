# kaggle-cooking
Use recipe ingredients to categorize the cuisine


# Project Title

## Setup with pyenv and virtual environment

### Prerequisites
- Make sure you have `pyenv` installed. If not, install it by following instructions [here](https://github.com/pyenv/pyenv#installation).

### Steps

1. **Clone the repository**

   Download the project to your local machine and navigate into its directory.
   
    ```bash
    git clone https://github.com/arnrxn/kaggle-cooking
    cd kaggle-cooking
    ```

2. **Set Python version pyenv for the project**

   Install the Python version specified in the `.python-version` file using `pyenv`.

    ```bash
    pyenv install
    ```

3. **Create a Virtual Environment**

   Create a virtual environment in a folder named ".venv".
   
    ```bash
    python -m venv .venv
    ```

4. **Activate the Virtual Environment**

   Activate the virtual environment.

     ```bash
     source .venv/bin/activate
     ```

5. **Install dependencies**

    Install the dependencies specified in the `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```
   
## Download Data from Kaggle

### 1. Install Kaggle API

   Install Kaggle API client, to interact with Kaggle datasets and competitions.

   ```bash
   pip install kaggle
   ```

#### 2. Setup Kaggle API Credentials

   Place your `kaggle.json` API token in the proper directory. 
   You can download this file from your Kaggle account settings page.

   ```bash
   mkdir -p ~/.kaggle && cp path/to/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

#### 3. Create a Data Directory

   Create a directory where the dataset will be stored.
   ```bash
   mkdir data/raw
   ```

#### 4. Download the Dataset

   Downloads the dataset from Kaggle into the `data/raw` directory.

   ```bash
   kaggle competitions download -c whats-cooking -p data/raw
   ```

#### 5. Unzip the Dataset

   Unzip the downloaded dataset into the `data/raw` directory.

   ```bash
   unzip data/raw/whats-cooking.zip
   unzip data/raw/sample_submission.csv.zip
   unzip data/raw/test.json.zip           
   unzip data/raw/train.json.zip           
   ```

#### 6. Clean up

   Remove the downloaded zip files to clean up the `data/raw` directory.

   ```bash
   rm data/raw/whats-cooking.zip
   rm data/raw/sample_submission.csv.zip
   rm data/raw/test.json.zip           
   rm data/raw/train.json.zip 
   ```