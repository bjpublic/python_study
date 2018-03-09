import wx
import base64
from Crypto import Random
from Crypto.Cipher import AES
import hashlib
 
# 암호화 관련 초기화 코드 입니다.
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s : s[0:-s[-1]]
 
 
# 윈도우즈 정의 클래스 입니다.
class Frame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 200))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
 
        # 버튼을 생성 합니다.
        self.btn = wx.Button(self.panel, -1, '암호화')
 
        # 텍스트 박스를 생성합니다.
        self.txt = wx.TextCtrl(self.panel, -1, size=(140,-1))
        self.txt.SetValue('input your value')
        
        # 텍스트 라벨을 생성합니다.
        self.some_text = wx.StaticText(self.panel, size=(140,150), pos=(10,60))
        self.some_text.SetLabel('result is...')
 
        # 버튼 클릭 시 이벤트를 연결 합니다.
        self.Bind(wx.EVT_BUTTON, self.GetEncryption, self.btn)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.btn)
        sizer.Add(self.txt)
 
        self.panel.SetSizer(sizer)
        self.Show()
 
    # 버튼 클릭 시 실행 되어, 암호화 하는 함수 입니다.
    def GetEncryption(self, e): 
        # 텍스트 박스(self.txt)로 부터 값을 얻어와 암호화 함수로 넘겨 줍니다.
        cipher = AESCipher('mysecretpassword')
        self.enc = cipher.encrypt(self.txt.GetValue())
        
        # 받은 값을 텍스트 라벨에 출력합니다.
        self.some_text.SetLabel(self.enc)
 
 
    def OnCloseWindow(self, e):
        self.Destroy()
 
 
# 암호화 관련 클래스 입니다.
class AESCipher:

    def __init__( self, key ):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt( self, raw ):
        raw = raw.encode()
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ).decode()

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] )).decode()

# 메인코드 입니다.
# 윈도우를 띄우고 제목을 넣습니다.
app = wx.App()
frame = Frame(None, 'WxEncryption')
app.MainLoop()
