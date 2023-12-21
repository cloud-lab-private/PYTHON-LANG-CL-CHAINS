import langchain_core.messages.ai
import requests
from main.lab import sample
from main.lab import lab

"""
This file will contain some sample code to send the output of the functions in lab.py to the 
console. You may modify this file in any way, it will not affect the test results.
"""


def main():
    user_input = input("Enter some text here to prompt the sports chain to talk about sports:")
    result = sample(user_input)
    print(result)
    print("Now let's test the chain you've built, which should only accept music prompts.")
    user_input = input("Enter some text here to prompt the music chain to talk about music:")
    result = lab(user_input)
    if type(result) is langchain_core.messages.ai.AIMessage:
        print(result)
    else:
        print("the lab() function did not produce an AI message result.")


if __name__ == '__main__':
    main()
