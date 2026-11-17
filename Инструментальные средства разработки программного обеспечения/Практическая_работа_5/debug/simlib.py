import sys, io, builtins, importlib.util, traceback, pdb, os
sys.stdout.reconfigure(encoding="utf-8")
_p = builtins.print
def _print(*a, **k):
    t = " ".join(str(x) for x in a)
    if t in ("\nМеню:", "Меню:") or t[:3] in ("1. ", "2. ", "3. ", "4. ", "5. ", "6. "):
        return
    _p(*a, **k)
builtins.print = _print

def run(path, answers, bp=None, cmds=()):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    it = iter(answers)
    def fake_input(prompt=""):
        a = next(it)
        print(prompt + a)
        return a
    builtins.input = fake_input
    spec = importlib.util.spec_from_file_location("tm", path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    try:
        if bp:
            class Echo(io.StringIO):
                def readline(self, *a):
                    l = super().readline(*a)
                    sys.stdout.write(l if l else "\n")
                    return l
            d = pdb.Pdb(stdin=Echo("\n".join(cmds) + "\n"), stdout=sys.stdout)
            d.use_rawinput = False
            d.set_break(path, bp)
            d.runcall(m.main)
        else:
            m.main()
    except StopIteration:
        pass
    except Exception:
        traceback.print_exc(file=sys.stdout)
