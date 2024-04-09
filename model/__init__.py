from utils.prep import MyCut
import yt_dlp
import random
import shutil
import os

class Video:
    def __init__(self):
        self.rootfile = None
        self.file = None
        pass

    def rootExists(self):
        if os.path.exists(os.path.abspath(f"{Config.OUTPUT}/{self.root}.webm")):
            return True
        else:
            return self.rootfile != None
    
    def exists(self):
        return self.file != None
    
    def download(self):
        tmp_dir = f"tmp_{random.randrange(start=1000, stop=9999)}"
        exists = os.path.exists(tmp_dir)

        while exists:
            tmp_dir = f"tmp_{random.randrange(start=1000, stop=9999)}"
            exists = os.path.exists(tmp_dir)
        os.makedirs(tmp_dir)
        
        ydl_opts = {
            'paths': {'home': tmp_dir}
        }
        ydl = yt_dlp.YoutubeDL(ydl_opts)
        ydl.download(self.link)

        arquivo = os.listdir(tmp_dir)[0]
        sarquivo = arquivo.split(".")
        sarquivo[0] = self.root
        sarquivo = ".".join(sarquivo)

        src = os.path.abspath("/".join([tmp_dir, arquivo]))
        dest = os.path.abspath("/".join(['videos',sarquivo]))

        shutil.move(src, dest)
        shutil.rmtree(tmp_dir)
        
        self.rootfile = sarquivo
        return sarquivo
    
    def process(self):
        if (self.rootfile == None): self.rootfile = f"{self.root}.webm"
        file = os.path.abspath("/".join([Config.OUTPUT, self.root]))
        cut = MyCut(file, self.start, self.end)
        cut.save(self.descricao)


class Config:
    OUTPUT = 'videos'

    # @staticmethod
    # def getOutput(self):
    #     return Config.OUTPUT