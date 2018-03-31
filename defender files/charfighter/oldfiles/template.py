## new template for my code
import os

def main():
    ## this is a great place to enter test code of my module that
    ## I don't want to run when I'm actually using the software.
    print("%s is being run as %s" % (__file__,__name__))

## this line forces the programmer no to name his files after
## the __main__ namespace. this can be troublesome when importing
assert os.path.basename(__file__) != '__main__.py'


## every file should have this
if __name__ == "__main__":
    ## this block will run if we are running this as a standalone
    ## god for calling test code like 'main()'
    main()
else:
    ## this block will only run if this module is being imported
    ## by another module (usually the __main__ module.
    print("%s is being imported by __main__" % __name__)



