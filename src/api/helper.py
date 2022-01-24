from .models import *



def get_question(id: int):
    q = Question.objects.get(id=id)
    q.answers = Answer.objects.filter(question=q.id)
    return q

def get_test(id: int):
    test = Test.objects.get(id=id)
    test.questions = map(test.questions, lambda x: get_question(x.id))
    return test


def get_module(id: int):
    module = Module.objects.get(id=id)
    module.tests = map(module.tests, lambda x: get_test(x.id))



def get_all_interactive_readings():
    pass

def get_all_tinder_swipes():
    pass

def get_all_tests():
    pass


def get_interactive_reading():
    pass

def get_tinder_swipe():
    pass

def get_test():
    pass


