#!/usr/bin/env python3
"""эмулятор оболочки этап 1 REPL"""
import shlex
import sys

VFS_NAME = "vfs"  


class ShellError(Exception):
    """Ошибка выполнения команды."""


def cmd_ls(args):
    # заглушка
    print("ls", args)


def cmd_cd(args):
    # заглушка
    print("cd", args)


def cmd_exit(args):
    sys.exit(0)


COMMANDS = {"ls": cmd_ls, "cd": cmd_cd, "exit": cmd_exit}


def execute(line):
    try:
        argv = shlex.split(line)  # четко разбирает кавычки
    except ValueError as e:
        raise ShellError(f"ошибка разбора: {e}")
    if not argv:
        return
    name, args = argv[0], argv[1:]
    if name not in COMMANDS:
        raise ShellError(f"{name}: команда не найдена")
    if name == "exit" and args:
        raise ShellError("exit: команда не принимает аргументов")
    COMMANDS[name](args)


def main():
    while True:
        try:
            line = input(f"user@{VFS_NAME}:/$ ")
        except EOFError:  # сtrl+d
            print()
            break
        except KeyboardInterrupt:  # сtrl+с
            print()
            continue
        try:
            execute(line)
        except ShellError as e:
            print(e, file=sys.stderr)


if __name__ == "__main__":
    main()
