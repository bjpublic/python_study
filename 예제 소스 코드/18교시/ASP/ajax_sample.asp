<%@ Language=VBScript %>
 
<script>
function getMenu() {
   var xhttp;
   // 사용자가 입력한 값을 id 를 통해 가져옵니다.
   var menuNo = document.getElementById("menuNo").value;
   
   // 새로운 ajax 요청을 만듭니다.
   xhttp = new XMLHttpRequest();
   // 요청에 대해 응답이 정상으로 올때까지 기다려서, 
   xhttp.onreadystatechange = function() {
      if (xhttp.readyState == 4 && xhttp.status == 200) {
         // span 태그내에 응답으로 온 텍스트 값을 살짝 끼워 넣습니다.
         document.getElementById("menuName").innerHTML = xhttp.responseText;
      }
   }
   // 실제 요청하는 페이지는 ajax_sub.asp 페이지 이고, get 인자로 no 에 사용자가 입력한 값을 넣습니다.
   xhttp.open("GET", "ajax_sub.asp?no="+menuNo, true);
   xhttp.send();
}
</script>
 
<html>
   <head>
      <title>ajax 샘플</title>
   </head>
<body>
   <table>
      <tr>    
         <td> 메뉴 번호: </td>
         <!-- 사용자가 입력하는 값 -->
         <td width=120> <INPUT id="menuNo" size="10" type="text" value=""> </td>    
           <td width=200> 
               <!-- 버튼을 누르면 getMenu 함수를 실행 합니다 -->
               <input type="button" value="해당되는 메뉴 찾기" onclick="getMenu()">
               <!-- 나중에 응답 값을 끼워 넣을 span 태그. 첨에는 아무 내용도 없습니다 -->
               : <span id="menuName"></span>
           </td>
         </tr>
   </table>         
</body>
</html>
