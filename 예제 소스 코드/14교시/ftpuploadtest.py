import ftplib
import os
from datetime import datetime
 
# datatime 모듈을 사용하여 오늘의 압축 파일 이름을 생성합니다.
filename = "backup_" + datetime.now().strftime("%Y%m%d") + ".zip"
 
# ftp에 연결합니다.
ftp = ftplib.FTP("127.0.0.1")
ftp.login("ftpuser", "test1234")
 
# ftp 에서 myback 폴더로 이동합니다.
ftp.cwd("/mybackup")
 
# zip 파일이 있는 폴더로 이동합니다.
os.chdir(r"c:\python\code\zipfile")
 
# 바이너리 형태로 파일을 업로드 합니다.
ftp.storbinary("STOR " + filename, open(filename, 'rb'))
 
print ('upload completed')
