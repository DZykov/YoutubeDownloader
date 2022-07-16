import os

class Replacer:


    def __init__(self, directory):
        self.f_dir = directory

    def replace_wl(self, lst):
        files_str = os.listdir(self.f_dir)
        new_f = []
        for f in files_str:
            n = ''
            for el in lst:
                n = f.replace(el)
            o = self.f_dir+'/'+f
            os.rename(o, n)
            new_f.append(n)
        return new_f            
