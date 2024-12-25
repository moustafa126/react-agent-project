# ReAct News Agent

A sophisticated news aggregation agent that leverages the ReAct (Reason + Act) paradigm to fetch and summarize news articles from major sources including BBC, The Guardian, and Reuters.

## Features

- **Multi-Source Support**: Fetches articles from BBC, The Guardian, and Reuters
- **Category-Based Filtering**: Retrieve articles by categories (Sports, Business, Technology, etc.)
- **Smart Processing**: Uses ReAct approach for reasoned, step-by-step article processing
- **Content Extraction**: Scrapes and summarizes article content
- **Link Discovery**: Finds and validates related article links

## Technologies Used

- LangChain for agent and tool management
- Google Generative AI (via langchain_google_genai) for LLM capabilities
- Feedparser for RSS feed processing
- Requests and BeautifulSoup for web scraping

## Installation

1. Download the code:
```bash
cd react-agent-project
```

2. Install required dependencies:
```bash
pip install feedparser requests beautifulsoup4 langchain-google-genai
```

3. Set up your Google API key:
```bash
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
```

## Project Structure

```
react_agent_project/
└── main.py  # Main script containing all functionality
```

## Core Functions

### `fetch_news(url: str) -> Union[str, List[str]]`
Fetches up to 3 or 5 article links from a given RSS feed URL.

### `scrape_page_content(url: str) -> str`
Extracts and returns the textual content from a webpage.

### `scrape_links(url: str) -> List[str]`
Discovers and returns up to 5 valid links from a given webpage.

## Usage

1. Initialize the agent with your API key:
```python
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

2. Run the script:
```bash
python main.py
```

3. Example query:
```python
user_input = "Fetch the latest technology articles from Reuters"
```

## Customization Options

### Modify the Prompt Template
Adjust the agent's reasoning process by modifying the template variable in the code:

```python
template = """
Your custom instructions here...
"""
```

### Add New Tools
Extend functionality by implementing additional tools:

```python
tools = [
    Tool(
        name="Your New Tool",
        func=your_tool_function,
        description="Description of what your tool does"
    ),
    # ... existing tools
]
```

### Change LLM Model
Update the model configuration if you have access to different Google PaLM models:

```python
llm = ChatGoogleGenerativeAI(model="your-preferred-model")
```

## Author

[Moustafa Abada]
