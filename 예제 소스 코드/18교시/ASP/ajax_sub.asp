<%@ Language=VBScript %>
 
<%
    ' request 값을 받습니다.
   menuNo = request("no")
    
   ' 넘어온 메뉴 번호에 해당하는 메뉴이름을 반환해 줍니다..
   Select Case menuNo
      Case 1
         Response.Write("pizza")
      Case 2
         Response.Write("pasta")
      Case Else
         Response.Write("drink")
   End Select
%>
