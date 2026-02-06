from crewai import Task, Crew, Process
from src.agents.investment_agents import InvestmentAgents
from src.models.investment import InvestmentRecommendation
from src.config.settings import settings, setup_logging
import logging
import argparse

logger = logging.getLogger(__name__)

def run_investment_committee(stock_symbol: str):
    agents = InvestmentAgents()
    
    # 1. Initialize Agents
    fundamental_agent = agents.fundamental_analyst()
    technical_agent = agents.technical_analyst()
    sentiment_agent = agents.sentiment_analyst()
    chair_agent = agents.committee_chair()

    # 2. Define Tasks
    task_fundamental = Task(
        description=f"Analyze the fundamental health of {stock_symbol}. Focus on revenue growth, debt-to-equity, and FCF.",
        expected_output="A detailed summary of the company's financial status.",
        agent=fundamental_agent
    )

    task_technical = Task(
        description=f"Perform technical analysis on {stock_symbol}. Identify key support/resistance and trend indicators.",
        expected_output="A report on price action and technical outlook.",
        agent=technical_agent
    )

    task_sentiment = Task(
        description=f"Analyze current market sentiment for {stock_symbol} from recent news headlines.",
        expected_output="A brief on whether the market sentiment is bullish, bearish, or neutral.",
        agent=sentiment_agent
    )

    task_consensus = Task(
        description=f"Review the reports from the analysts and provide a final recommendation for {stock_symbol}.",
        expected_output="A structured final investment recommendation.",
        agent=chair_agent,
        output_json=InvestmentRecommendation,
        context=[task_fundamental, task_technical, task_sentiment]
    )

    # 3. Form the Crew
    investment_crew = Crew(
        agents=[fundamental_agent, technical_agent, sentiment_agent, chair_agent],
        tasks=[task_fundamental, task_technical, task_sentiment, task_consensus],
        process=Process.sequential, # Can be hierarchical for more complex logic
        verbose=True
    )

    # 4. Kick off the work
    logger.info(f"Kicking off Investment Committee for {stock_symbol}...")
    result = investment_crew.kickoff()
    return result

def main():
    setup_logging()
    
    parser = argparse.ArgumentParser(description="Run the Virtual Investment Committee Agent")
    parser.add_argument("--stock", type=str, required=True, help="Stock symbol (e.g., AAPL)")
    args = parser.parse_args()

    if not settings.GEMINI_API_KEY:
        logger.error("GEMINI_API_KEY is missing. Please set it in your .env file.")
        return

    try:
        recommendation = run_investment_committee(args.stock)
        print("\n" + "="*50)
        print(f"FINAL RECOMMENDATION FOR {args.stock}")
        print("="*50)
        print(recommendation)
    except Exception as e:
        logger.error(f"Execution failed: {e}", exc_info=True)

if __name__ == "__main__":
    main()
