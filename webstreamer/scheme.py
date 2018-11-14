

OPTIONs={
}

DEPs={
}

def pre_build():
    
    import os
    from conans import tools
    git = tools.Git()
    branch = git.get_branch()
    print('------------ current -----branch :',branch)
    if not branch.startswith('testing/'):
        return
    # you can overwrit Conan enviroments as yours

    os.environ['CONAN_STABLE_BRANCH_PATTERN'] = 'testing/*'
    os.environ['CONAN_UPLOAD'] = "https://api.bintray.com/conan/conanos/testing"    
    #  CONAN_USERNAME: "conanos"
    #  CONAN_LOGIN_USERNAME: "mingyiz"

def options(name,settings,shared):
    options = OPTIONs.get(name,{})
    return options

def dependencies(name,settings):
    deps = DEPs.get(name,{})
    return deps


def library_types(name, settings):
    #arch = self.settings.get('arch',None)
    #os   = self.settings.get('os',None)
    return 'shared' # or tuple return 'shared','static'

