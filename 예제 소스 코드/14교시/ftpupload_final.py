import ftplib
import os
from datetime import datetime
import subprocess 
from subprocess import check_output
 
### 압축 코드
# 서브 프로세스를 실행시켜 7z 명령어로 압축을 합니다.
check_output('c:\\\"Program Files\"\\7-Zip\\7z a -r -tzip c:\\python\\code\\zipfile\\backup_\"%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%\".zip c:\\python\\code\source\\*.txt c:\\python\\code\\source\\*.jpg', shell=True) 
print ("zip done")  
 
### ftp 코드 
# datatime 모듈을 사용하여 오늘의 압축 파일 이름을 생성합니다.
filename = "backup_" + datetime.now().strftime("%Y%m%d") + ".zip"
 
# ftp 에 연결합니다.
ftp = ftplib.FTP("127.0.0.1")
ftp.login("ftpuser", "test1234")
 
# ftp 루트에서 mybackup 폴더로 이동합니다.
ftp.cwd("/mybackup")
 
# zip 파일이 있는 폴더로 이동 합니다.
os.chdir(r"c:\python\code\zipfile")
 
# 바이너리 형태로 파일을 업로드 합니다.
ftp.storbinary("STOR " + filename, open(filename, 'rb'))
print ("ftp upload done")

### 삭제 코드 
# 7일 이상 된 백업 폴더의 backup zip 파일을 삭제 합니다.
subprocess.call('forfiles /p "c:\\python\\code\\zipfile " /s /m backup*.zip /d -7 /c "cmd /c del @path"', shell=True)
print ("del done")
