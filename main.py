import os
import feedparser
import requests
from bs4 import BeautifulSoup
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
import re


def fetch_news(url: str):
    url = url.strip().strip('"').strip("'")
    url = re.sub(r'[^\x20-\x7E]', '', url)
    url = re.sub(r'\s+', '', url)

    regex = re.compile(
        r'^(https?://)?'
        r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})'
        r'(/[A-Za-z0-9._~:/?#@!$&\'()*+,;=-]*)?$'
    )
    if not regex.match(url):
        return f"Invalid URL: {url}"

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    feed = feedparser.parse(url)
    if not feed.entries:
        return f"No entries found for URL: {url}"

    articles = [entry.get("link", "No Link") for entry in feed.entries[:5]]
    # return {"success": True, "articles": articles}
    return articles

def scrape_page_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return f"Failed to retrieve URL: {url} (status {response.status_code})"

        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text(separator="\n")
        return text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def scrape_links(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        domain = url.split("/")[2]
        links = []
        for tag in soup.find_all(['a', 'link'], href=True):
            link = tag.get('href')
            if link and not link.startswith(('javascript:', '#', 'mailto:')):
                if link.startswith('/') or domain in link:
                    links.append(link if link.startswith('http') else f"https://{domain}{link}")
        return links[:5]
    except Exception as e:
        return []

def main():
    os.environ["GOOGLE_API_KEY"] = "YOUR_KEY_HERE"

    tools = [
        Tool(
            name="FetchNews",
            func=fetch_news,
            description="Fetches top 5 articles from an RSS feed given a URL. Input: URL as a string."
        ),
        Tool(
            name="ScrapePageContent",
            func=scrape_page_content,
            description="Scrapes and returns the content of a webpage. Input: URL as a string."
        ),
        Tool(
            name="ScrapeLinks",
            func=scrape_links,
            description="Scrapes and returns up to 5 links from a given webpage. Input: URL as a string."
        )
    ]

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=1
    )


    template = """
You are a ReAct agent specialized in fetching and summarizing news. Use the following steps:

1. Find the correct RSS feed URL from the following list using journal name and category.
2. Use 'FetchNews' to get 3 articles. If it fails, use "ScrapeLinks" as fallback with the origianl journal link.
3. Scrape the 3 articles using 'scrape_page_content'
4. Summarize each article providing details and important key points. Number the summaries and mention the journal name.

-BBC (https://www.bbc.com/)
Sports: "http://feeds.bbci.co.uk/sport/rss.xml"
News: "http://feeds.bbci.co.uk/news/rss.xml"
Business: "http://feeds.bbci.co.uk/news/business/rss.xml"
Innovation: "http://feeds.bbci.co.uk/news/technology/rss.xml"
Culture: "http://feeds.bbci.co.uk/programmes/b006q2x0/episodes/downloads.rss"
Arts: "http://feeds.bbci.co.uk/arts/rss.xml"
Travel: "http://feeds.bbci.co.uk/news/world/rss.xml"

- Guardian (https://www.theguardian.com/)
Sports: "https://www.theguardian.com/sport/rss"
News: "https://www.theguardian.com/world/rss"
Business: "https://www.theguardian.com/business/rss"
Innovation: "https://www.theguardian.com/technology/rss"
Culture: "https://www.theguardian.com/culture/rss"
Arts: "https://www.theguardian.com/artanddesign/rss"
Travel: "https://www.theguardian.com/travel/rss"

- Reuters (https://www.reuters.com/)
Sports: "https://www.reuters.com/sports/rss"
News: "https://www.reuters.com/news/rss"
Business: "https://www.reuters.com/finance/rss"
Innovation: "https://www.reuters.com/technology/rss"
Culture: "https://www.reuters.com/lifestyle/rss"
Arts: "https://www.reuters.com/lifestyle/arts/rss"
Travel: "https://www.reuters.com/lifestyle/travel/rss"


Query: {{input}}
"""

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
        agent_kwargs={
            "prefix": template
        }
    )

    user_input = "Fetch the latest business articles from the BBC"

    try:
        print("Invoking agent with input:", user_input)
        response = agent.invoke({"input": user_input})
        print("\nFINAL RESPONSE:")
        print(response["output"])
    except Exception as e:
        print(f"Error during execution: {str(e)}")

if __name__ == "__main__":
    main()
