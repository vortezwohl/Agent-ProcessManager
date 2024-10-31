import logging

from process_manager.agent import process_manager

# log = logging.getLogger("ceo")
# log.setLevel(logging.DEBUG)

result = process_manager.assign('tell me all things about process which has pid 23180').just_do_it()

print(result)
