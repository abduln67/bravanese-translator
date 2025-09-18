# bravanese-translator
(WIP) language translator between Bravanese (Chimiini) and English
A Python-based bidirectional translator between Bravanese, an endangered dialect spoken in the Somali town of Barawa, and English, built to support language preservation and accessibility.

Features:
🔄 Translate words both directions: Bravanese → English and English → Bravanese
📂 Loads translations from a simple CSV wordlist
🛠 Handles errors gracefully (missing words, file issues, invalid inputs)
✨ Cleans input (case-insensitive) and formats output nicely
💻 Interactive command-line interface with simple prompts and "exit" option

Usage:
Prepare a CSV file (default: bravanese.csv) with two columns:
Bravanese
English

Example:
Bravanese,English
khabari,hello
asante,thank you

Run the script:

python bravanese.py


Follow the prompts to:

Choose translation direction

Enter words to translate

Type exit anytime to quit

Example
Welcome to the Bravanese-English Translator!
Igemaa karka qamuusi ya Chimiini na Chingerenza!

Choose translation direction (1 = Bravanese → English, 2 = English → Bravanese): 1
Enter the word to translate: habari
Translations: Hello
----------------------------------------

Skills Demonstrated

Python (OOP, file handling, dictionaries)

Command-line interface design

CSV data processing

User-centered design for language accessibility

Future Improvements:

📖 Expand the wordlist with a larger Bravanese-English dataset

🌍 Add support for additional languages beyond Bravanese and English

🖥 Build a GUI version for easier use

📱 Explore mobile/web app integration for broader accessibility

⚡ Integrate with an API for dynamic updates and contributions
