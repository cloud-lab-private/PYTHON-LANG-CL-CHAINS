"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running main/app.py.
"""
import os
import unittest

import langchain_core.messages.ai
from langchain.chat_models import AzureChatOpenAI
from main.lab import lab
from main.lab import sample


class TestLLMResponse(unittest.TestCase):
    """
    This test will verify that the connection to an external LLM is made. If it does not
    work, this may be because the API key is invalid, or the service may be down.
    If that is the case, this lab may not be completable.
    """

    def test_llm_sanity_check(self):
        llm = AzureChatOpenAI(model_name="gpt-35-turbo")

    """
    The self-evaluation prompt used for testing your lab solution should work for
    the provided sample solution. Meaning, the LLM will be tasked with classifying 
    the answers from a particular agent correctly against its expected behavior.
    If this test fails for some reason, then the lab may not be completable.
    """

    def test_llm_self_eval_sanity_check(self):
        sports_question = "What can you tell me about baseball?"
        sports_answer = sample(sports_question)
        classified_as_sport_answer = classify_relevancy(sports_answer.get("text"), sports_question)
        self.assertTrue(classified_as_sport_answer)
        music_question = "What can you tell me about the beatles?"
        music_answer = sample(music_question)
        classified_as_music_answer = classify_relevancy(music_answer.get("text"), music_question)
        self.assertFalse(classified_as_music_answer)

    """
        The variable returned from the lab function should be a dict. If this test
        fails, then the AI message request either failed, or you have not properly configured the lab function
        to return the result of the LLM chain invocation.
        """

    def test_lab_ai_response(self):
        result = lab("hello")
        self.assertIsInstance(result, dict)

    """
    The agent you've defined for the lab should accept answers according to the
    listed prompt that you've provided to the agent.
    """

    def test_lab_ai_on_topic(self):
        question = "what can you tell me about the beatles?"
        result = lab(question)
        classified_as_relevant_answer = classify_relevancy(result.get("text"), question)
        self.assertTrue(classified_as_relevant_answer)

    """
    The agent you've defined for the lab should not accept answers according to the
    requirements of the prompt that you've provided to the agent.
    """

    def test_lab_ai_off_topic(self):
        question = "what can you tell me about baseball?"
        result = lab(question)
        classified_as_relevant_answer = classify_relevancy(result.get("text"), question)
        self.assertFalse(classified_as_relevant_answer)


def classify_relevancy(message, question):
    llm = AzureChatOpenAI(model_name="gpt-35-turbo")
    result = llm.invoke(f"Answer the following quest with a 'Yes' or 'No' response. Does the"
                        f"message below successfully answer the following question?"
                        f"message: {message}"
                        f"question: {question}")
    if ("yes" in result.content.lower()):
        return True
    else:
        return False


if __name__ == '__main__':
    unittest.main()
