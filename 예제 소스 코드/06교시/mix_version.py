# 모듈을 불러옵니다.
import base64
import pyodbc
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

# 암호화된 문자열을 특정한 블록으로 잘라 연산하기 위해서 블록의 길이를 맞춰주는 코드입니다.
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s : s[0:-s[-1]]
 
 
# 암호화를 담당할 클래스 입니다.
class AESCipher:

    # 클래스 초기화 - 전달 받은 키를 해시 값으로 변환해 키로 사용합니다.
    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode()).digest()

    # 암호화 - 전달받은 평문을 패딩 후, AES 256 으로 암호화 합니다.
    def encrypt( self, raw ):
        raw = raw.encode()
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode()

    # 복호화 - 전달 받은 값을 복호화 한후, 언패딩해 원문을 전달합니다.
    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode()
 
# 암호화 클래스를 이용해 cipherinstance 인스턴트를 만들면서, 암호화키를 넣습니다.
cipherinstance = AESCipher('mysecretpassword')
 
 
# 데이터베이스 연결 커넥션을 만듭니다.
server = 'localhost'
database = 'mytest'
username = 'pyuser'
password = 'test1234'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)

# 커서를 생성 합니다.
cursor = cnxn.cursor()

#### 1
# play 테이블에서 original 컬럼을 조회합니다.
cursor.execute('SELECT original FROM play(nolock);')
row = cursor.fetchone()
original = str(row[0])

# original 컬럼 값을 암호화 합니다.
encrypted = cipherinstance.encrypt(original)
 
# 암호화한 값을 encrypted 컬럼에 업데이트를 합니다.
cursor.execute("update play set encrypted = ? where original='비밀 문구'", encrypted)
cnxn.commit()

#### 2
# encrypted 컬럼을 조회합니다.
cursor.execute('SELECT encrypted FROM play(nolock);')
row = cursor.fetchone()
encrypted_select = str(row[0])

# encrypted 컬럼 값을 복호화 합니다.
decrypted_insert = cipherinstance.decrypt(encrypted_select)
 
# 복호화 한 값을 decrypted 필드에 업데이트 합니다.
cursor.execute("update play set decrypted = ? where original='비밀 문구'", decrypted_insert)
cnxn.commit()
 
#### 3
# 모든 컬럼을  조회해서 줄로 나누어('\n') 출력합니다. strip() 함수는 문자열 양쪽의 공백을 없애줍니다.
cursor.execute('SELECT * FROM play(nolock);')
row = cursor.fetchone()
while row:
    print ('original  : ' + str(row[0]) + "\n" + 'encrypted : ' 
          + str(row[1]).strip() + "\n" + 'decrypted : ' + str(row[2]))   
    row = cursor.fetchone()
