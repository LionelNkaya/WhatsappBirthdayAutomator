<html>

<body>
<h1>Well done, friend added sucessfully!</h1>


<?php 

$friend_name = $_POST["friend_name"];
$month = $_POST["month"];
$day = $_POST["day"];

// For consistency in DB if day is one digit append 0 in front of it
if ($day < 10) {
    $day = "0".$day;
}

// Creating the friend_DOB string to put in the DB
$friend_DOB =  $month."-".$day;

$myPDO = new PDO("sqlite:".__DIR__."/app.db");


$statement = $myPDO->prepare("INSERT INTO friends (friend_name, friend_DOB) VALUES (?, ?)");
$statement->bindParam(1, $friend_name);
$statement->bindParam(2, $friend_DOB);
$statement->execute();

?>

Added new friend : <?php echo $friend_name; ?>!<br>
DOB : <?php echo $month."-".$day; ?> <br>

<br>

<button class="GFG" onclick="window.location.href = 'index.html';">
    Add another friend
</button>

</body>
</html>