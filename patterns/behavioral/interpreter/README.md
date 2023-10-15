### Interpreter pattern
Implements a simple language to use inside an application. We define classes
to represent rules of language (its grammar) and an interpreter that deals with
this grammar.

### Notes:
* Terminal expression is associated with the terminal symbols as defined in the grammar.
* Non-terminal expressions implement logical operations (And, Or, etc).
* Complex grammars are hard to maintain since there have to be at least one class
for each rule.
* Specification pattern is the same as Interpreter.
* Sometimes Specification implementation is aimed at providing recombination of
complex business logic.