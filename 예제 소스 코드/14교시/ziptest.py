import subprocess 
from subprocess import check_output

#  서브 프로세스를 실행 시킵니다.
check_output('c:\"Program Files"\7-Zip\7z a -r -tzip c:\python\code\zipfile\backup_"%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%".zip c:\python\code\source\*.txt c:\python\code\source\*.jpg', shell=True) 

print ("zip done")