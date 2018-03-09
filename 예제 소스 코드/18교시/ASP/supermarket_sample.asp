<%@ Language=VBScript %>
 
<%
   ' 연결 문자열을 정의 합니다.
   strMyTest = "Provider=SQLOLEDB; Data Source=localhost; Initial Catalog=mytest; User Id=pyuser; Password=test1234"
   Set objConn = Server.CreateObject("ADODB.Connection")
   objConn.Open strMyTest 
 
   ' 실행할 SQL 문을 정의 합니다.
   strSQL = "select itemno, category, foodname, company, price from supermarket s(nolock)"
 
    ' 쿼리를 실행 하여 결과 얻어옵니다.
   Set rtnRow = objConn.Execute(strSQL)
%>
 
 
<html>
   <head>
      <title>supermarket</title>
   </head>
 
   <body>       
      <p>supermarket 상품</p>
      <table border=1>
         <tr>
            <td>번호</td>
            <td>카테고리</td>
            <td>종류</td>
            <td>상품이름</td>
            <td>가격</td>       
         </tr>    
 
<%
   'DB 에서 조회한 행이 끝이 아니라면 루프를 돌리면서 각 컬럼을 <td> 태그안에 끼워 넣습니다.
   Do while Not rtnRow.EOF 
%>
 
         <tr>
            <td><%=rtnRow("itemno")%></td>
            <td><%=rtnRow("category")%></td>
            <td><%=rtnRow("foodname")%></td>
            <td><%=rtnRow("company")%></td>
            <td><%=rtnRow("price")%></td>
         </tr>
                        
<%
   'rsList의 내용을 다음 결과 행으로 이동하며 Do 문을 반복합니다.
   rtnRow.MoveNext
   Loop
%>
 
      </table>
</body>          
 
<%
   '열었던 연결을 닫습니다.
   objConn.Close
   Set objConn=Nothing
%>
