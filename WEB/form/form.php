<?php

// get the data from the form
$discord = $_POST['discord'];
$email = $_POST['email'];
$curso = $_POST['curso'];
$year = $_POST['year'];
$instagram = $_POST['instagram'];
$twitter = $_POST['twitter'];
$github = $_POST['github'];
$fname = $_POST['fname'];
$lname = $_POST['lname'];
$phone = $_POST['phone'];
$description = $_POST['description'];



// create the array
$data = array(
    'discord' => $discord,
    'email' => $email,
    'curso' => $curso,
    'year' => $year,
    'instagram' => $instagram,
    'twitter' => $twitter,
    'github' => $github,
    'fname' => $fname,
    'lname' => $lname,
    'phone' => $phone,
    'description' => $description
);

// encode the array to json

if ($discord == "") {
    header('Location: ../index.html');
    die();
    exit();
}

$json = json_encode($data);

// save the json to a file

file_put_contents('./db/data.json', $json);

// redirect to the index

header('Location: ../index.html');

//post to the web api

$ch = curl_init('127.0.0.1:4000/post?token=insert_token_here');

curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");

curl_setopt($ch, CURLOPT_POSTFIELDS, $json);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

curl_setopt($ch, CURLOPT_HTTPHEADER, array(

'Content-Type: application/json',

'Content-Length: ' . strlen($json))

);

$result = curl_exec($ch);

//alert the user that the form was sent

echo "<script>alert('¡Formulario enviado con éxito!');</script>";

curl_close($ch);

?>