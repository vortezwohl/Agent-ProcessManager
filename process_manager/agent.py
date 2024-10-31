from dotenv import load_dotenv
from ceo import Agent, get_openai_model

from process_manager.action import (
    find_all_processes,
    find_process_by_name,
    find_top_k_processes_with_the_highest_cpu_usage,
    find_top_k_processes_with_the_highest_memory_usage,
    kill_a_process_by_pid,
    show_specifications_of_current_computer,
    constant_calculate
)

load_dotenv()

abilities = [
    find_all_processes,
    find_process_by_name,
    find_top_k_processes_with_the_highest_cpu_usage,
    find_top_k_processes_with_the_highest_memory_usage,
    kill_a_process_by_pid,
    show_specifications_of_current_computer,
    constant_calculate
]
process_manager = Agent(name='process_manager', abilities=abilities, brain=get_openai_model())
