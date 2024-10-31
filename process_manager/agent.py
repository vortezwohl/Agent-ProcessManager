from dotenv import load_dotenv
from ceo import Agent, get_openai_model

from process_manager.action import get_process_by_name, show_all_processes

load_dotenv()
process_manager = Agent([get_process_by_name, show_all_processes], get_openai_model())
