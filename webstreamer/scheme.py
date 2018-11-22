

OPTIONs={
}

DEPs={
}

def pre_build():
    
    import os
    from conans import tools
    git = tools.Git()
    branch =''
    if os.environ.get('CI') and os.environ.get('APPVEYOR'):
        branch = os.environ.get('APPVEYOR_REPO_BRANCH')
    elif os.environ.get('CI') and os.environ.get('TRAVIS'):
        branch = os.environ.get('TRAVIS_BRANCH')

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
    print('settings -->',type(settings))
    if isinstance(settings,dict):
        compiler = settings.get('compiler')
    else:
        compiler = settings.compiler
        
    if compiler == 'Visual Studio':
        if name in ['gmp','nettle','libtasn1','gnutls']:
            return 'static'
    return 'shared' # or tuple return 'shared','static'

