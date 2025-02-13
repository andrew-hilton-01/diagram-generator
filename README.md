# Mermaid.js AI Diagram Generator

This project is a web-based tool that generates and renders **Mermaid.js** diagrams using AI-generated code. It integrates **FastAPI** and **Uvicorn** on the backend to communicate with **Claude 3.5 Haiku** via OpenRouter API, providing an interactive way to create Mermaid.js diagrams from natural language prompts.

## Features
- **AI-powered Mermaid.js code generation**: Users enter a prompt, and the backend retrieves structured Mermaid.js code using Claude 3.5 Haiku.
- **Live diagram rendering**: Users can modify the generated Mermaid.js code and render or re-render it with the Mermaid.js API.
- **Customizable AI behavior**: The system prompt can be adjusted to use different instructions or desired graph outputs.

## How It Works
1. **User Input**: The user enters a prompt in the first text area.
2. **Generate Code**: Clicking "Generate Code" sends the prompt to the backend.
3. **AI Processing**: The backend calls OpenRouter API, using a few-shot prompt strategy to get structured Mermaid.js code.
4. **Code Display**: The generated code is displayed in the second text area, allowing the user to edit it.
5. **Render Diagram**: Clicking "Render" passes the Mermaid.js code to the API and displays the generated diagram.

## Tech Stack
- **Frontend**: HTML, JavaScript, Mermaid.js API
- **Backend**: Python, FastAPI, Uvicorn
- **AI Model**: Claude 3.5 Haiku via OpenRouter API

## Screenshots
Use a more detailed prompt like the examples in backend.py, but this is roughly what a bad prompt can get you if you just let the LLM assume:
![image](https://github.com/user-attachments/assets/b8c8e32c-f63d-4ee0-9ba8-6add4d34bb38)
![image](https://github.com/user-attachments/assets/221e92c8-3635-48b7-bafc-44bb504b6623)
![image](https://github.com/user-attachments/assets/a0434e80-5124-4602-8eb9-142358e3700d)



## Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/andrew-hilton-01/diagram-generator
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn openai dotenv
   ```
3. Set up your OpenRouter API key in an .env file in root:
   ```bash
   OPENROUTER_API_KEY="your-api-key" // No Quotes
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn backend:app --reload
   ```
5. Open `frontend.html` in your browser to start using the tool.

## Customization
- Modify the **system prompt** in `backend.py` to tweak the AI’s behavior.
- Replace **Claude 3.5 Haiku** with another model available via OpenRouter.
- Adjust the **Examples** in `backend.py` for different desired graphs or diagrams.

## Future Improvements
- Add examples.json file to more easily load few-shot examples.
- Add support for different AI models dynamically.
- Build on the UI.
- Implement error handling for AI-generated code. I.E. regex fallbacks.
- Enable saving and exporting of diagrams.

## Contributing
Feel free to fork the repository and submit pull requests with improvements or fixes.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

