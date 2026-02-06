from crewai import Agent
from src.tools.finance_tools import fetch_stock_financials, fetch_stock_history
from src.config.settings import settings
from crewai_tools import SerperDevTool
from langchain_google_genai import ChatGoogleGenerativeAI
import os

class InvestmentAgents:
    def __init__(self):
        self.gemini_llm = ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL_NAME,
            verbose=True,
            temperature=0.5,
            google_api_key=settings.GEMINI_API_KEY
        )

    def fundamental_analyst(self) -> Agent:
        return Agent(
            role="Fundamental Analyst",
            goal="Provide a deep-dive analysis of a company's financial health and intrinsic value.",
            backstory="""You are a seasoned Wall Street analyst with an MBA and 20 years of experience 
            in valuing companies. You look at balance sheets, cash flows, and revenue growth. 
            Your reports are data-driven and avoid hype.""",
            tools=[fetch_stock_financials, SerperDevTool()],
            llm=self.gemini_llm,
            verbose=True,
            allow_delegation=False
        )

    def technical_analyst(self) -> Agent:
        return Agent(
            role="Technical Analyst",
            goal="Identify price trends, support/resistance levels, and momentum patterns.",
            backstory="""You are a masterful chartist who believes that everything is reflected in the price. 
            You use historical price data and volume to predict future movements. 
            You are quick to spot breakouts and reversals.""",
            tools=[fetch_stock_history],
            llm=self.gemini_llm,
            verbose=True,
            allow_delegation=False
        )

    def sentiment_analyst(self) -> Agent:
        return Agent(
            role="Sentiment Analyst",
            goal="Gauge market sentiment and public perception from news and social media.",
            backstory="""You are an expert in behavioral finance and NLP. You understand that 
            fear and greed drive markets. You monitor headlines and social trends to see if 
            the market is overly optimistic or pessimistic about a stock.""",
            tools=[SerperDevTool()],
            llm=self.gemini_llm,
            verbose=True,
            allow_delegation=False
        )

    def committee_chair(self) -> Agent:
        return Agent(
            role="Investment Committee Chair",
            goal="Synthesize reports from all analysts into a final, high-conviction recommendation.",
            backstory="""You are the ultimate decision-maker. You take the detailed reports from 
            your fundamental, technical, and sentiment analysts and resolve any conflicting 
            viewpoints to provide a clear Buy, Sell, or Hold rating with a detailed rationale.""",
            llm=self.gemini_llm,
            verbose=True,
            allow_delegation=True
        )
