import argparse
import sys
import os
from yaml import load, FullLoader
from .utils import search_user, check_config, project_check

__author__ = "404answernotfound"
__copyright__ = "404answernotfound"
__license__ = "MIT"

def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Automated Gittron Automata, AGA")
    parser.add_argument(dest="function", help="function to run", type=str, metavar="STRING")
    parser.add_argument('--param', dest="parameter", help="function parameters", type=str, metavar="STRING")

    return parser.parse_args(args)
    
def main(args):
    """
    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    functions = None
    with open('config/automa.yaml') as config:
            data = load(config, Loader=FullLoader)
            functions = data["automa"]["functions"]

    if args.function in functions:
        os.system('echo "# Starting a function call"')
        if functions[args.function]["system"] is False:
            eval(functions[args.function]["eval"])
        elif functions[args.function]["args"] is None:
            os.system(functions[args.function]["eval"])
        else:
            os.system(functions[args.function]["eval"].format(args.parameter))

    else:
        pass

    print("Automagit is working")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()