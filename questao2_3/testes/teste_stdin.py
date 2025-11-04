from livro_input_stream import LivroInputStream
import sys
import json

def teste_stdin():
    sis = LivroInputStream(sys.stdin.buffer)
    objs = sis.read_all()
    print(json.dumps(objs, ensure_ascii=False, indent=2))