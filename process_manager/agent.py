import os

from ceo import Agent, get_openai_model

from process_manager.action import get_process_by_name, show_all_processes

os.environ['OPENAI_API_KEY'] = 'sk-mOzqTNBFENiFIilFT-gNaUaUR7GbbjXSj7oGychzSqT3BlbkFJWQjUtSGrwkfU3nd5m-GAN_pleB8VaRWFDrFMTHol4A'

process_manager = Agent([get_process_by_name, show_all_processes], get_openai_model())
