import warnings
from app.src.crew import My_Crew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew
    """
    My_Crew().crew().kickoff()

if __name__ == "__main__":
    run()