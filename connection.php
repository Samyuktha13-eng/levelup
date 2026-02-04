<?php
    include("connection.php");
    $msg = '';

    if(isset($_POST['submit'])) {
        $name = mysqli_real_escape_string($conn, $_POST['username']);
        $email = mysqli_real_escape_string($conn, $_POST['email']);
        $password = $_POST['password'];
        $confirm_password = $_POST['Cpassword'];

        if($password !== $confirm_password) {
            $msg = "Passwords do not match!";
        } else {
            $select1 = "SELECT * FROM users WHERE email = ?";
            $stmt = mysqli_prepare($conn, $select1);
            mysqli_stmt_bind_param($stmt, "s", $email);
            mysqli_stmt_execute($stmt);
            $result = mysqli_stmt_get_result($stmt);

            if(mysqli_num_rows($result) > 0) {
                $msg = "User already exists";
            } else {
                $hashed_password = password_hash($password, PASSWORD_BCRYPT);
                $insert1 = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)";
                $stmt = mysqli_prepare($conn, $insert1);
                mysqli_stmt_bind_param($stmt, "sss", $name, $email, $hashed_password);

                if(mysqli_stmt_execute($stmt)) {
                    header('location:login.php');
                    exit();
                } else {
                    $msg = "Registration failed!";
                }
            }
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediPath LevelUp - Sign Up</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        body {
            background-color: #121212;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
        }
        .form-container {
            max-width: 400px;
            margin: 80px auto;
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        }
        .form-container h2 {
            text-align: center;
            margin-bottom: 25px;
            color: #00bcd4;
        }
        .form-control {
            background-color: #2c2c2c;
            border: 1px solid #444;
            color: #fff;
        }
        .form-control:focus {
            background-color: #2c2c2c;
            color: #fff;
            border-color: #00bcd4;
            box-shadow: none;
        }
        .btn {
            width: 100%;
            background-color: #00bcd4;
            border: none;
            color: #fff;
            padding: 10px;
            font-weight: bold;
            border-radius: 6px;
            margin-top: 10px;
        }
        .btn:hover {
            background-color: #00a2c2;
        }
        .msg {
            color: #ff5252;
            text-align: center;
            margin-bottom: 15px;
        }
        a {
            color: #00bcd4;
        }
        a:hover {
            text-decoration: underline;
            color: #00a2c2;
        }
        p {
            text-align: center;
            margin-top: 15px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <form action="" method="post">
            <h2>MediPath LevelUp</h2>
            <p class="msg"><?= $msg ?></p>
            <div class="form-group">
                <input type="text" name="username" placeholder="Full Name" class="form-control" required>
            </div>
            <div class="form-group">
                <input type="email" name="email" placeholder="Email Address" class="form-control" required>
            </div>
            <div class="form-group">
                <input type="password" name="password" placeholder="Password" class="form-control" required>
            </div>
            <div class="form-group">
                <input type="password" name="Cpassword" placeholder="Confirm Password" class="form-control" required>
            </div>
            <button class="btn" name="submit">Sign Up</button>
            <p>Already have an account? <a href="login.php">Login</a></p>
        </form>
    </div>
</body>
</html>
