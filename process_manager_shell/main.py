import sys

from process_manager.agent import process_manager


def main():
    process_manager.assign(query="我的cpu咋样").just_do_it()
    exit(0)


if __name__ == "__main__":
    main()