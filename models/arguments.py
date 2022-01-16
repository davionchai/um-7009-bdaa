from argparse import Namespace


class ArgumentModel:
    def __init__(self, source_args: Namespace):
        self.with_aliases: bool = source_args.with_aliases
