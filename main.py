#main

import argparse

from todo import (
    add_task,
    list_tasks,
    done_task,
    remove_task
)


def main():
    parser = argparse.ArgumentParser(
        prog="todo",
        description="CLI Todo приложение"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("id", type=int)
    
    #автор DARKle

    remove_parser = subparsers.add_parser("remove")
    remove_parser.add_argument("id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.text)

    elif args.command == "list":
        list_tasks()

    elif args.command == "done":
        done_task(args.id)

    elif args.command == "remove":
        remove_task(args.id)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()