\# JARVIS - AI Voice Assistant



An intelligent voice-based virtual assistant built with Python, powered by OpenAI's GPT technology. JARVIS listens to your voice commands and responds intelligently with a natural, conversational interface.



\## Features



✨ \*\*Voice Recognition \& Response\*\*

\- Real-time speech-to-text conversion

\- Natural language understanding

\- Text-to-speech output with voice feedback



🤖 \*\*ChatGPT Integration\*\*

\- Advanced AI conversations using OpenAI's API

\- Context-aware responses

\- Multi-turn conversation support



🎵 \*\*Media Control\*\*

\- Play music and songs

\- Control playback

\- Query history for recent interactions



🎨 \*\*GUI Interface\*\*

\- User-friendly graphical interface

\- Real-time query display

\- Visual feedback for voice commands



\## Installation



\### Prerequisites

\- Python 3.7 or higher

\- pip (Python package manager)

\- OpenAI API key

\- Microphone for voice input

\- Speakers for audio output



\### Setup Steps



1\. \*\*Clone the repository\*\*

&#x20;  ```bash

&#x20;  git clone https://github.com/Akku125/jarvis.git

&#x20;  cd JARVIS

&#x20;  ```



2\. \*\*Install dependencies\*\*

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  ```



3\. \*\*Set up OpenAI API Key\*\*

&#x20;  - Get your API key from \[OpenAI](https://platform.openai.com/api-keys)

&#x20;  - Set it as an environment variable:

&#x20;  ```bash

&#x20;  # Windows

&#x20;  set OPENAI\_API\_KEY=your\_api\_key\_here

&#x20;  

&#x20;  # Mac/Linux

&#x20;  export OPENAI\_API\_KEY=your\_api\_key\_here

&#x20;  ```



4\. \*\*Run JARVIS\*\*

&#x20;  ```bash

&#x20;  python JARVIS/gui.py

&#x20;  ```



\## Usage



1\. Launch the application by running the GUI

2\. Speak your commands naturally (e.g., "What's the weather?", "Play my favorite song")

3\. JARVIS will process your voice and respond with an answer

4\. Chat mode: Activate ChatGPT integration for advanced conversations

5\. View query history to see past interactions



\## Project Structure



```

JARVIS/

├── JARVIS/

│   ├── gui.py              # Main GUI application

│   ├── features.py         # Core features and functions

│   ├── song.py             # Music playback module

│   ├── assets/             # UI assets and images

│   └── PyWhatKit\_DB.txt    # Database for web automation

├── test.py                 # Testing module

└── requirements.txt        # Project dependencies

```



\## Requirements



\- \*\*pyttsx3\*\* - Text-to-speech engine

\- \*\*SpeechRecognition\*\* - Voice recognition library

\- \*\*openai\*\* - OpenAI API client

\- \*\*PyAudio\*\* - Audio I/O library

\- \*\*PyWhatKit\*\* - Web automation toolkit

\- \*\*PyQt5\*\* or \*\*Tkinter\*\* - GUI framework



\## Configuration



Edit the configuration in `gui.py` to customize:

\- Voice speed and rate

\- Microphone sensitivity

\- OpenAI model preferences

\- Response timeout values



\## Features in Detail



\### Voice Commands

\- \*\*Ask questions\*\* - Get instant answers from ChatGPT

\- \*\*Play music\*\* - Request songs by name

\- \*\*Search web\*\* - Quick internet searches

\- \*\*Control system\*\* - Basic system commands

\- \*\*Tell jokes\*\* - Get entertainment



\### ChatGPT Mode

\- Activate ChatGPT for advanced conversations

\- Maintains context across multiple queries

\- Natural, human-like responses



\### Query History

\- Automatically saves your queries

\- Review past interactions

\- Track conversation history



\## Troubleshooting



\*\*Microphone not detected:\*\*

\- Check if PyAudio is installed correctly

\- Ensure microphone is connected and enabled



\*\*OpenAI API errors:\*\*

\- Verify your API key is valid

\- Check API rate limits

\- Ensure sufficient credits on your OpenAI account



\*\*Speech recognition issues:\*\*

\- Speak clearly and avoid background noise

\- Adjust microphone input levels

\- Ensure internet connection is stable



\## Future Enhancements



\- \[ ] Multi-language support

\- \[ ] Offline voice recognition

\- \[ ] Custom wake-word detection

\- \[ ] Integration with smart home devices

\- \[ ] Improved error handling

\- \[ ] Advanced machine learning models



\## Contributing



Contributions are welcome! Please feel free to submit a Pull Request.



\## License



This project is open source and available under the MIT License.



\## Author



\*\*Akanksha\*\* - \[GitHub Profile](https://github.com/Akku125)



\## Support



For issues, questions, or suggestions, please open an issue on the \[GitHub repository](https://github.com/Akku125/jarvis/issues).



\---



\*\*Note:\*\* This project requires an active OpenAI API key with available credits. Please manage your API usage responsibly.



Built with ❤️ using Python and AI

