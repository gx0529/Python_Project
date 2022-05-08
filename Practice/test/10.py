
import urllib.request
import urllib.error
import logging
import time
import sys
import threading

md5path = 'MD5.txt'
# 需要走工单申请
verify_key = "af028d73a2ad8f64f3408fafa6418c60"
download_Fold = r'D:\\OWL\\Sample_Download\\sample'
successful = 0
failed = 0

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_name = rq + '.log'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    stream=sys.stdout,
                    filename=log_name)


def download(filename):

    global successful, failed
    url = 'http://speccenter.wrapper.360es.cn:8082/specimen.php?type=file&key=%s&verify_key=%s' % (filename.strip('\n'), verify_key)

    try:
        f = urllib.request.urlopen(url)
        data = f.read()
        # 返回json，失败
        if data.startswith('{'):
            logging.info('%s \t error:%s' % (filename.strip('\n'), data))
            failed = failed+1
        else:
            fvirus = open(r'%s\%s' % (download_Fold, filename.strip('\n').strip('\n')), "wb")
            fvirus.write(data)
            fvirus.close()
            logging.info('%s \t success!' %filename.strip('\n'))
            successful = successful+1
    except Exception as e:
        logging.info('%s \t error:%s' %(filename.strip('\n'),e))
        failed = failed + 1


f = open(md5path)

currentmd5 = []
tds = []
data = f.readlines()
count1 = len(data)
count2 = 0

for md5 in data:

    currentmd5.append(md5)
    count2 = count2+1
    if(len(currentmd5)==10 or count2 == count1):
        for i in range(0, len(currentmd5)):
            tds.append(threading.Thread(target=download, args=(currentmd5[i],)))
        for j in range(0, len(tds)):
            tds[j].start()
        tds[len(tds)-1].join(300)
        currentmd5 = []
        tds = []
        print(u"本组下载完成!")


logging.info("sucessful count : %d \t failed count:%d" %(successful,failed))
