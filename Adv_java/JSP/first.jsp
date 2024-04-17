<html>
    <body>
        <h1>My First Page</h1>
        <h3>Declarative tag</h3>
        <%!
        int a = 5;
        int b = 7;
        int mul(){
            return a*b;
        }
        String name = "My nam is Rahul";
        String reverse(){
            StringBuffer sb = new StringBuffer(name);
            return sb.reverse().toString();
        }
        %>
        <h3>Expression tag</h3>
        <%=reverse()%>
        <h3>Scriplet tag</h3>
        <%
        out.printn(a);
        out.println("<br>");
        out.printn(b);
        out.println("<br>");
        out.println("Multiplication result is:"+mul());

        %>
    </body>
</html>