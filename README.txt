# Restaurant Name Generator

A modern, AI-powered web app to generate creative restaurant names and menu suggestions based on your chosen cuisine. Built with Streamlit and LangChain, this project helps entrepreneurs, marketers, and foodies brainstorm unique restaurant concepts in seconds.

## Features
- **AI-Generated Restaurant Names:** Instantly get catchy, relevant names for your restaurant idea.
- **Menu Suggestions:** Receive a list of menu items tailored to your selected cuisine.
- **Beautiful, Responsive UI:** Enjoy a sleek, professional interface with custom branding and logo support.
- **Easy to Use:** Simple, intuitive controls for fast ideation.

## Demo
https://restaurant-name-suggestor.streamlit.app/

## Getting Started

### Prerequisites
- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nbdyknws-abhi/Restaurant-Name-Generator.git
   cd Restaurant-Name-Generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
Run the Streamlit app:
```bash
streamlit run main.py
```

Open your browser and go to the local URL provided by Streamlit (usually http://localhost:8501).

## Project Structure
```
├── main.py                # Streamlit app UI
├── langchain_helper.py    # AI logic for name and menu generation
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── Logo.png              # App logo
```

## Customization
- To change the logo, replace `Logo.png` with your own image.
- You can adjust the color scheme and layout in `main.py` (CSS section).

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or new features.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [LangChain](https://github.com/hwchase17/langchain)
- OpenAI and the AI community
