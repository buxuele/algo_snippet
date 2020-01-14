import re
import subprocess
import uuid
import time
import requests
from fake_useragent import UserAgent
from multiprocessing.dummy import Pool

u = UserAgent()
headers = {'User-Agent': u.random}


'''
m = https://videocdnbaidu.rhsj520.com/3/MRHQL/SNIS-576-C/1500kb/hls/index.m3u8
t = https://videocdnbaidu.rhsj520.com/3/MRHQL/SNIS-576-C/1500kb/hls/lJUBmbV1021000.ts

lJUBmbV1021000.ts
lJUBmbV10218541.ts

'''

filename = 'index.m3u8'
mp4_name = filename.split('.')[0]


def get_ts_url(filename):
    for i in open(filename, 'r'):
        if i.strip()[0] != '#':
            ts_url = 'https://videocdnbaidu.rhsj520.com/3/MRHQL/SNIS-576-C/1500kb/hls/' + i.strip()
            yield ts_url



def download(u):
    print(u)
    s = requests.Session()
    ts = s.get(u).content
    with open(u.split('/')[-1], 'wb') as g:
        g.write(ts)


def xdm():
    urls = get_ts_url(filename)
    pool = Pool(30)
    pool.map(download, urls)
    pool.close()
    pool.join()


def convert_to_mp4():
    cmd0 = 'ffmpeg -i index.m3u8 -c copy rename_me.mp4'
    cmd1 = 'copy /b *.ts {}.ts '.format(mp4_name)
    cmd2 = 'ffmpeg -i {0}.ts -vcodec copy -acodec copy {1}.mp4 '.format(mp4_name, mp4_name)
    cmd3 = 'del *.ts'
    cmd4 = 'del *.m3u8'

    subprocess.call(cmd0, shell=True)


if __name__ == '__main__':
    start = time.time()
    xdm()
    end = time.time()
    print("全部下载完成！下载一共消耗的时间是：" + str(end - start))

    # print("got all ts !")

    # convert_to_mp4()

    # subprocess.call(cmd1, shell=True)
    # subprocess.call(cmd2, shell=True)
    #
    # subprocess.call(cmd3, shell=True)
    # subprocess.call(cmd4, shell=True)
    # print('got mp4')
