**📌 Project Description**
My Zootopia API - is a Python project that connects to an external API to fetch detailed data about animals. The program prompts the user to enter the name of an animal (e.g., fox) and returns a list of all matching animals from the database along with relevant information.
If no match is found, the program gracefully handles the case by displaying a message and generating a simple response page indicating that no results were found.


**💡 What Problem Does It Solve?**
Manually searching for animal species and their information can be time-consuming or inconsistent. This tool offers a fast, user-friendly way to explore animal data programmatically, with clean error handling and security in mind.

It also demonstrates best practices like:
-+ Secure API key handling via .env files
-+ User input validation and feedback
-+ Simple CLI-based interaction for educational or utility use


**👥 Intended Audience**
-+ Python beginners learning about API consumption
-+ Developers building small data-driven apps
-+ Students working on projects involving animals, biology, or environmental studies
-+ Anyone curious about building secure, interactive command-line tools


**🚀 Usage**
*✅ Prerequisites*
Python 3.8 or higher
requests and python-dotenv libraries (included in requirements.txt)

*📦 Installation*
-+ Clone the repository:
git clone https://github.com/your-username/animal-info-finder.git
cd animal-info-finder
-+ Install dependencies:
pip install -r requirements.txt
-+ Create a .env file in the project root:
API_KEY=your_api_key_here
API_URL=https://example-api.com/animals
⚠️ Do not commit your .env file — it should be added to .gitignore to keep credentials secure.


**💻 How to Run**
*Simply run the Python script:*
python main.py

1.+ You will be prompted to enter the name of an animal:
Enter a name of an animal: fox

2.+ The program will fetch data from the API and display information about all fox-related species found.

3.+ If no animals are found:
The animal doesn't exist.