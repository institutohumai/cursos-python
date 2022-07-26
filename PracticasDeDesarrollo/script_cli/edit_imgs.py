import re
import os

ipynbs = [f for f in os.listdir(".") if f.endswith("ipynb")]

with open(ipynbs[0], "r") as inp:
    raw_nb = inp.read()


counter = 1


def replace_func(group):
    global counter
    to_repl = f"![image](imgs/{counter}.png)"
    counter += 1
    return to_repl


result = re.sub("!\[image.png\]\(attachment:.*?png\)", replace_func, raw_nb)
with open("new_nb.ipynb", "w") as out:
    out.write(result)

