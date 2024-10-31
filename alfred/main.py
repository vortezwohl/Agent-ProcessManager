import sys

from process_manager.agent import process_manager
from alfred.action import find_information_about_the_assistant

process_manager.grant_ability(find_information_about_the_assistant)


def main():
    process_manager.assign(query="帮我找到三的三次方个最占用内存的进程").just_do_it()
    exit(0)


if __name__ == "__main__":
    main()
