import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        #to create new KB: kb1 = KnowledgeBase(facts=[],rules=[])

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)
        #can call just with repr(kb1)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string
        #can call just with str(kb1)

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        alreadyin = False
        for i in range(len(self.facts)):
            if self.facts[i] == fact:
                alreadyin = True
                break
        if isinstance(fact, Fact): #better than fact.name == 'fact'
            if alreadyin == False:
                self.facts.append(fact)
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if isinstance(fact, Fact) == False:
            return False
        bindings = ListOfBindings()
        for i in range(len(self.facts)):
            binding = match(self.facts[i].statement,fact.statement)
            if binding != False:
                bindings.add_bindings(binding)
        if len(bindings) == 0:
            return False
        return bindings
