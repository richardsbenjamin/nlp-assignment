# NLP-ASSIGNMENT

Setting basic configuration to run our first chat client model.

## Requirements
- Python 3.8 or higher
- Virtualenv

## Installation and Usage

```bash
# 1. Clone the Repository
git clone https://github.com/richardsbenjamin/nlp-assignment.git
cd nlp-assignment.git

# 2. Set Up a Virtual Environment
# MacOS/Linux (Ubuntu)
python3 -m venv .venv
source venv/bin/activate

# Windows
python -m venv .venv
.\venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Create a .env File
# In the root directory of the project, create a .env file to store your API key:
# Add the following line and replace 'your_mistral_api_key_here' with your actual API key
# Do the same for the mistral model:
echo "API_KEY=API_KEY=ejYjkzOHDUHUe0IcHWEHMgLbjVGjqmnK" > .env
echo "MODEL=mistral-large-latest" > .env

# 5. Run the Application
# MacOS/Linux (Ubuntu)
python main.py

# Windows
python main.py

# 6. Do not forget
# When you make changes with new libs, do not forget to add them to the requirements file, using the following command
pip freeze > requirements.txt