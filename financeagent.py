from dotenv import load_dotenv
load_dotenv()   # <-- this loads .env into environment

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

agent =Agent(

    name ="web search agent",
    role= "Search the web",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],

    instructions=["Always include the source"],
    show_tool_calls=False,
    markdown=True,
)

## financial agent
finance_agent= Agent(
    name="finance_agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True),

    ],
    instructions=["use tables to display the data"],
    show_tool_calls=False,
    markdown=True,

)

multi_ai_agent=Agent(
    team=[agent,finance_agent],
    model=Groq(id="llama-3.3-70b-versatile"), 
    instructions=["always include the sources","Use the table to display the data"],
    markdown=True,
    show_tool_calls=False,

)

multi_ai_agent.print_response("summarize analyst recommendation and share the latest news for nvdia",stream=True)


 