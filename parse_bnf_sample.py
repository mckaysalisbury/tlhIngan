from lark import Lark, Transformer, Tree
from typing import List

# Read the BNF grammar from file
with open('bnf') as f:
    lines: List[str] = f.readlines()

# Remove comments and join lines
bnf_grammar: str = ''.join(line for line in lines if not line.strip().startswith('#'))

# Lark expects rules in a slightly different format than BNF, so we do a minimal conversion:
# - Remove angle brackets
# - Replace ::= with :
lark_grammar: str = bnf_grammar.replace('<', '').replace('>', '').replace('::=', ':')

# Create the parser (Earley handles ambiguous grammars)
parser: Lark = Lark(lark_grammar, parser='earley', start='klingon_sentence')


# Parse the sentence
try:
    # Example sentence to parse (should match the grammar)
    sentence: str = "waw'maj HIvtaH jagh"
    tree: Tree = parser.parse(sentence)
    print('Parse tree:')
    print(tree.pretty())
    breakpoint()
except Exception as e:
    print('Parsing failed:', e)
