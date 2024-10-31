import logging

from process_manager.agent import process_manager

log = logging.getLogger("ceo")
# log.setLevel(logging.DEBUG)

result = process_manager.assign('看看我电脑的配置').just_do_it()

print(result)
