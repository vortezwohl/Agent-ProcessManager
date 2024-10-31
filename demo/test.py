import logging

from process_manager.agent import process_manager

log = logging.getLogger("ceo")
log.setLevel(logging.DEBUG)

result = process_manager.assign('帮我把QQ关了吧，太吵了').just_do_it()

print(result)
