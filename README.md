# 📌 Project Description
My Zootopia API - is a Python project that connects to an external API to fetch detailed data about animals. The program prompts the user to enter the name of an animal (e.g., fox) and returns a list of all matching animals from the database along with relevant information.
If matches are found, the program automatically generates an HTML file displaying the animals as cards, each showing key data such as the animal’s name, type, and other relevant information.
If no matches are found, the script still generates a user-friendly HTML page with a message stating that no animals were found.



# 💡 What Problem Does It Solve?
Manually searching for animal species and their data can be time-consuming. This tool:
* Allows quick, structured exploration of animal data from an external API
* Presents the data in a clean, visual format (HTML cards)
* Handles missing or incorrect input gracefully
* Demonstrates secure handling of API credentials using .env files



# 👥 Intended Audience
* Python beginners learning about API consumption
* Developers building small data-driven apps
* Students working on projects involving animals, biology, or environmental studies
* Anyone curious about building secure, interactive command-line tools



# 🚀 Usage
*✅ Prerequisites*
* Python 3.8 or higher
* requests and python-dotenv libraries (included in requirements.txt)

*📦 Installation*
* Clone the repository:
```
git clone https://github.com/your-username/My-Zootopia-API.git
cd My-Zootopia-API
```
* Install dependencies:
```
pip install -r requirements.txt
```
* Create a .env file in the project root:
```
API_KEY=your_api_key_here
```

⚠️ Do not commit your .env file — it should be added to .gitignore to keep credentials secure.



# 💻 How to Run
Simply run the Python script:
```
python main.py
```

You will be prompted to enter the name of an animal:
```
Enter a name of an animal: fox
```

If animals are found:
* An HTML file (e.g., results.html) is generated
* Each matching animal is displayed as a card with its name, type, and other details
* The HTML can be opened in any browser

If no animals are found:
* An HTML page is still generated, showing a friendly message like: 
```
The animal doesn't exist.
```



# ⚙️ Configuration
All API-related values (e.g., keys and endpoints) are stored in the .env file.
The script uses:
* requests for API calls
* dotenv for environment variable management
* os for accessing variables securely
* Basic HTML generation with Python string formatting or templates


