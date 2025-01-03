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

1. Clone the project:
```bash
git clone https://github.com/moustafa126/react-agent-project.git
cd react-agent-project
```

2. Install required dependencies:
```bash
pip install feedparser requests beautifulsoup4 langchain-google-genai
```

3. Set up your Google API key:
```bash
os.environ["GOOGLE_API_KEY"] = "AIzaSyBWqs0UBXFY5KWdsLV55o5CD3Tt3pB8lwU"
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

## Sample Usage & Output

### Business News Example
```python
user_input = "Fetch the latest business articles from the BBC"
```

**Sample Output:**
```
Here are the latest business articles from BBC:

1. **American Airlines resumes flights after technical issue**

American Airlines experienced a nationwide halt in flights for approximately an hour due to a "vendor technology issue." The disruption occurred on Christmas Eve, one of the busiest travel days of the year. The airline has since resumed flights but delays are expected. This incident follows a similar grounding of flights in July caused by a global IT crash from cybersecurity firm Crowdstrike.

2. **Car industry consulted over 2030 petrol and diesel ban**

The UK government is seeking input from the motor industry on how to implement the ban on new petrol and diesel cars by 2030. The ban was previously extended to 2035 but Labour's election manifesto promised to reinstate the earlier deadline. Concerns remain about the cost of electric vehicles and charging infrastructure. The consultation aims to provide clarity for manufacturers and encourage investment in the UK automotive industry.

3. **Morrisons Christmas delays extend to second day**

Morrisons customers experienced a second day of disruptions following "systems issues" on December 23rd. Customers reported delayed or cancelled deliveries, and in-store discounts were not applied. While Morrisons has apologized and offered a 10% discount to loyalty scheme members, they have yet to disclose the cause of the problems. The incident highlights the importance of reliable IT systems, especially during peak shopping seasons.

```

### Sports News Example
```python
user_input = "Fetch the latest sports articles from the Guardian"
```

**Sample Output:**
```
FINAL RESPONSE:
**Summary 1: The Guardian**

This article reflects on the Paris 2024 Olympics, four months after its conclusion. It highlights the event's success, noting that it was well-received by a global audience, particularly Gen Z. The article emphasizes the successful execution of the original plans, including the opening ceremony on the Seine and the use of iconic landmarks as venues. It also acknowledges some issues, such as the rain during the opening ceremony and controversies surrounding some athletes. The article concludes by discussing the legacy of the Games, including the cleaning of the Seine and increased sports facilities.

**Key Points:**

*   Paris 2024 Olympics were considered a success, with high viewership and positive feedback.
*   The Games successfully implemented its original plans and embraced both Olympic and French values.
*   The event faced some challenges, including weather and athlete controversies.
*   The Olympics left a positive legacy, including infrastructure improvements and increased physical activity in schools.

**Summary 2: The Guardian**

This article discusses the situation of Marcus Rashford at Manchester United. Manager Ruben Amorim emphasizes that Rashford has a "big responsibility" to help the team during a low point. Rashford has been excluded from recent match-day squads due to performance issues. Amorim insists that Rashford wants to play and that his exclusion is a matter of the manager's decision. The article also touches on the team's poor performance, currently 13th in the league, and the manager's frustration with the situation.

**Key Points:**

*   Marcus Rashford has been excluded from Manchester United's squad due to performance issues.
*   Manager Ruben Amorim calls on Rashford to show leadership and help the team.
*   Amorim insists Rashford wants to play and that his exclusion is his decision.
*   The article highlights Manchester United's poor performance and the manager's frustration.

**Summary 3: The Guardian**

This article analyzes Manchester City's recent decline, contrasting their current struggles with their success a year ago. It points out the team's drop in performance, attributing it to factors such as Rodri's injury, the impact of financial charges, and the possibility of manager Pep Guardiola's influence waning. The article also discusses the impact of Erling Haaland's signing, suggesting that while he is a goal scorer, he doesn't contribute to the team's overall play. The article concludes that the team has become tactically aged and that the manager has been unable to find new ways to win.

**Key Points:**

*   Manchester City has experienced a significant drop in performance compared to last year.
*   Factors contributing to the decline include Rodri's injury, financial charges, and potentially Guardiola's waning influence.
*   Erling Haaland's signing, while adding goals, has not improved the team's overall play.
*   The team is seen as tactically aged, and the manager has struggled to find new strategies.
```

### Both Business & Sports News Example
```python
    user_input = "Fetch the latest business and sports articles from the BBC"
```

**Sample Output:**
```
FINAL RESPONSE:
**Summary 1 (BBC Business):** American Airlines experienced a technical issue that caused a nationwide halt of flights for around an hour on Christmas Eve. The issue, attributed to a "vendor technology issue," disrupted travel plans during one of the busiest travel days of the year. While flights have resumed, delays are still being reported at major US airports. Passengers were temporarily held on the tarmac or asked to disembark from their planes. This is not the first such incident for American Airlines, as they had a similar issue due to a global IT crash in July.

**Summary 2 (BBC Business):** The UK government is consulting with the car industry on how to phase out new petrol and diesel car sales by 2030. This ban had been extended to 2035 but the current Labour government wants to restore the 2030 deadline. Car industry leaders have expressed concerns that the switch to electric vehicles is not happening quickly enough due to cost and infrastructure issues. The government said the consultation aims to provide clarity for manufacturers and the charging industry, encouraging long-term investment. The consultation also includes hybrid vehicles, vans and small volume manufacturers.

**Summary 3 (BBC Business):** Morrisons, a UK supermarket chain, experienced significant delivery delays and discount issues on the biggest grocery shopping day of the year, December 23rd. Customers experienced order cancellations and voucher issues. Morrisons has apologized for the "systems issues" but has yet to explain the cause of the problems. The supermarket is offering a 10% discount to loyalty card members as compensation.  A consumer expert emphasized the need for transparency and making amends with loyal customers.

**Summary 4 (BBC Sport):**  Manchester City is currently facing a crisis, having lost nine out of their last 12 matches. This is a significant downturn for the team, which was previously unbeaten and leading the Premier League. The article delves into the reasons for the crisis, including injuries to key players like Rodri, uncharacteristic errors from players, and a drop in confidence. Manager Pep Guardiola is reportedly trying different strategies to address the issues, and the club is planning significant changes to the squad, potentially replacing five or six regular starters, by the end of his current contract.

**Summary 5 (BBC Sport):** This article explores how Sir Alex Ferguson built his last great Manchester United side, culminating in their 2008 Champions League victory. It highlights key moments, such as the dressing room incident where Ferguson brought a young Cristiano Ronaldo to tears and his speech to his players in Moscow, emphasizing hard work and his working-class roots.  It underscores Ferguson's ability to reinvent his squad and adapt to the evolving landscape of the Premier League, by integrating global talent and tactics. It also notes the influence of assistant manager Carlos Queiroz.

**Summary 6 (BBC Sport):** The International Cricket Council has released the fixtures for the 2025 Champions Trophy. India will face Pakistan in Dubai on February 23rd. The tournament will be hosted by Pakistan and in Dubai as a neutral venue from February 19 to March 9. The tournament includes eight teams, divided into two groups, with Pakistan and India in Group A. Due to ongoing political tensions, India will play all of their group games, plus the first semi-final in Dubai, and the final will also move to Dubai if India makes it.

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
