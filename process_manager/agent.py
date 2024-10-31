from dotenv import load_dotenv
from ceo import Agent, get_openai_model

from process_manager.action import (
    find_all_processes,
    find_process_by_name,
    kill_a_process_by_pid,
    show_specifications_of_current_computer,
    constant_calculate
)

load_dotenv()

actions = [
    find_all_processes,
    find_process_by_name,
    kill_a_process_by_pid,
    show_specifications_of_current_computer,
    constant_calculate
]
process_manager = Agent(actions, get_openai_model())
