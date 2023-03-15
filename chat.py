#!/usr/bin/env python3

import click
from click import clear
import json
import openai
import os
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
import re
import signal
import sys
from termcolor import colored


openai.api_key = os.getenv("OPENAI_API_KEY")

def processChatGPT(input_str, n=1):
  params = {
    "engine": "text-davinci-002",
    "prompt": input_str,
    "max_tokens": 50,
    "temperature": 0.7,
    "n": n
  }
  response = openai.Completion.create(**params)
  return response


@click.command()
def cli():
    signal.signal(signal.SIGINT, signal_handler)
    session = PromptSession(history=FileHistory('.history'))
    while True:
        try:
            input_str = session.prompt("chatGPT(input)> ")
            if input_str == "exit":
              sys.exit(0)
            elif input_str == "\q":
              sys.exit(0)
            elif input_str == "test":
              print("No, this will bork chatGPT")
              next
            elif input_str == "clear":
              clear()
            else:
              match = re.search(r'(.*)\[(\d+)\]', input_str)
              if match: 
                response = processChatGPT(input_str, int(match.group(2)))
              else:
                response = processChatGPT(input_str)
              print("chatGPT(response)>")
              for i, choice in enumerate(response.choices):
                click.echo(f"\t{choice.text.strip()}")
        except KeyboardInterrupt:
            click.echo("Exiting...")
            sys.exit(0)

def signal_handler(sig, frame):
    click.echo("You pressed Ctrl+C!")
    sys.exit(0)

if __name__ == "__main__":
    cli()
