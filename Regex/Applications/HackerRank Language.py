import re

regex_pattern = r"\d{4}\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$"

n = int(input())
for _ in range(n):
    row_input = input()
    if re.search(regex_pattern, row_input):
        print("VALID")
    else:
        print("INVALID")
