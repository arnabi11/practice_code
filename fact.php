<?php
if(isset($_POST['submit']))
{
 $number = $_POST['num'];     /*number to get factorial */
 $fact   = 1;
 for($k=1;$k<=$number;++$k)
 {
 $fact =  $fact*$k;
 }
 echo "Factorial of $number is ".$fact;
}
 ?>
 <!DOCTYPE html>
 <html>
 <head>
 <title>Factorial of any number</title>
 </head>
 <body>
 <form name="factorial" action="" method="post">
 Number :<input type="text" name="num" value="" required=""><br>
 <input type="submit" value="Submit" name="submit">
 </form>
 </body>
 </html>