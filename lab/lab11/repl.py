try:
    import readline  # history and arrow keys for CLI
except ImportError:
    pass  # but not everyone has it
import sys

from reader import read
from expr import global_env

# program start
if __name__ == '__main__':
    """Run a read-eval-print loop.
    `python3 repl.py` to start an interactive REPL.
    `python3 repl.py --read` to interactively read expressions and
      print their Python representations.
    """
    read_only = len(sys.argv) == 2 and sys.argv[1] == '--read' #判断是否为只读

    while True:
        try:
            # `input` prints the prompt, waits, and returns the user's input.
            user_input = input('> ') #请输入
            expr = read(user_input) #对输入物执行read指令
            if expr is not None:
                if read_only:
                    print(repr(expr)) #print这个的repr
                else:
                    print(expr.eval(global_env)) #从global环境里eval
        except (SyntaxError, NameError, TypeError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # Ctrl-C, Ctrl-D
            print()  # blank line
            break  # exit while loop (and end program)

