"""This script will automate requests to github's RESTful api 
    to check for differences between previous day and new day followers for account
"""

import argparse
import logging
import sys
import requests
import os
from yaml import load, dump, FullLoader

from datetime import date

__author__ = "404answernotfound"
__copyright__ = "404answernotfound"
__license__ = "MIT"

_logger = logging.getLogger(__name__)
today = date.today().strftime("%d%m%Y")

# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.

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

def search_user(username):
    print(os.getcwd(), os.listdir())
    response = requests.get("https://api.github.com/users/{}/followers".format(username))
    response = response.json()
        
    with open('logs/{}.txt'.format(today), 'w') as file:
        for i, res in enumerate(response):
            file.write(str(res) + '\n')
            
    commit_to_repo()
            
def print_today_logs():
    with open('logs/{}.txt'.format(today)) as file:
        lines = file.readlines()
        for line in lines:
            print(line)
            
def commit_to_repo():
    os.system('ls -la')
    os.system('git add * && git commit -m "automagit is uploading new log file {}" && git push https://404answernotfound@github.com/404answernotfound/automagit'.format(today))
    print('Committed changes to repo')

def commit_with_message(commit_message):
    os.system('ls -la')
    os.system('git add * && git commit -m "automagit -m {}" && git push https://404answernotfound@github.com/404answernotfound/automagit'.format(commit_message))
    print('Committed changes to repo')

def project_check():
    """Returns the answer"""
    print('42')

def check_config():
    with open('config/automa.yaml') as config:
        data = load(config, Loader=FullLoader)
        print('Working')
    
def main(args):
    """
    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    # Config test
    functions = None
    with open('config/automa.yaml') as config:
            data = load(config, Loader=FullLoader)
            functions = data["automa"]["functions"]

    if args.function in functions:
        os.system('echo "# Starting a function call"')
        if functions[args.function]["args"] is None:
            os.system(functions[args.function]["eval"])
        else:
            os.system(functions[args.function]["eval"].format(args.parameter))

    else:
        pass
    # End config test
    print("Automagit is working")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    run()