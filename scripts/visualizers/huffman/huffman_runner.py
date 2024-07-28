import math
import random
from visualizers.huffman.huffman import (
    build_huffman_tree,
    decode_huffman,
    get_huffman_codes,
    print_tree,
)


def main():
    text = "THREE CATS SAT THERE"
    root = build_huffman_tree(text)
    codes = get_huffman_codes(root)

    print("Character | Frequency | Code")
    print("-" * 30)
    strings = []
    for char, code in codes.items():
        strings.append(f"{char:<10} | {text.count(char):<9} | {code}")
    strings.sort()
    print("\n".join(strings))
    # for code in codes:
    # print(code)
    print(decode_huffman("100011001011100011010111", root=root))
