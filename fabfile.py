from fabric.api import local

def test():
    local("flake8 nlpre")
    local("nosetests -v")
    #local("flake8 tests")
    local("aspell check README.md")
    #local("detox")

def lint():
    local("autopep8 nlpre/*.py -aaa --in-place")
    #local("autopep8 tests/*.py --in-place")

def push():
    test()
    local("git commit -a")
    local("git push")
