import logging

from process_manager.agent import process_manager

log = logging.getLogger("ceo")
log.setLevel(logging.DEBUG)

result = process_manager.assign('帮我把微信关了吧，（可能叫WeChat.exe，你找找）').just_do_it()

print(result)
