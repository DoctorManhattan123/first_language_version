import numpy as np
from sys import getsizeof

from evaluator import Evaluator
from lexer import Lexer
from parser import Parser
from statements import StatementParser
from classes import Environment


def evaluate_string(string: str):
    tokens = get_tokens(string)
    parser = Parser(tokens)
    parsed_tree = parser.parse()
    evaluator = Evaluator(parsed_tree)
    environment = Environment()
    return evaluator.evaluate(environment)


def get_tokens(code: str):
    lexer = Lexer(code)
    lexer.run_lexer()
    return lexer.get_token_objects()


def execute(string: str):
    tokens = get_tokens(string)

    #print(tokens)
    statement_parser = StatementParser(tokens)
    statement_parser.parse()
    statement_parser.interpret()
    return statement_parser.get_store(), statement_parser.get_evaluated_store()


#print(evaluate_string("true && false"))
store, evaluated_store = execute("""
str a = "global";
{
  fun showA() {
    write( a);
  }

  showA();
  str a = "block";
  showA();
}
""")

print(store, evaluated_store)


