import logging

from process_manager.agent import process_manager

log = logging.getLogger("ceo")
log.setLevel(logging.DEBUG)

result = process_manager.assign('我的内存被谁用了').just_do_it()

print(result)
