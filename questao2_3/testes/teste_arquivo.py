from helpers.objetos import _objetos_demo
from livro_output_stream import LivroOutputStream
from livro_input_stream import LivroInputStream
import json
import os

def teste_arquivo():
    print("\n=== Teste ii) Arquivo ===")
    with open("saida_sebo.bin", "wb") as f:
        stream = LivroOutputStream(_objetos_demo(), n_objetos=3, destino=f)
        stream.send_all()
    print("Gravado em 'saida_sebo.bin'.")

def teste_arquivo(path: str = "saida_sebo.bin", gerar_se_nao_existe: bool = True):
    if gerar_se_nao_existe and not os.path.exists(path):
        with open(path, "wb") as f:
            out = LivroOutputStream(_objetos_demo(), 3, f)
            out.send_all()
    with open(path, "rb") as f:
        ins = LivroInputStream(f)
        objs = ins.read_all()
    print(f"[Arquivo] Lidos {len(objs)} objetos de '{path}':")
    print(json.dumps(objs, ensure_ascii=False, indent=2))