<?php
    include("connection.php");
    $msg = '';

    if(isset($_POST['submit'])) {
        $email = mysqli_real_escape_string($conn, $_POST['email']);
        $password = $_POST['password'];

        // Check if user exists
        $select = "SELECT * FROM users WHERE email = ?";
        $stmt = mysqli_prepare($conn, $select);
        mysqli_stmt_bind_param($stmt, "s", $email);
        mysqli_stmt_execute($stmt);
        $result = mysqli_stmt_get_result($stmt);

        if(mysqli_num_rows($result) > 0) {
            $user = mysqli_fetch_assoc($result);
            if(password_verify($password, $user['password'])) {
                // Login success
                session_start();
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['user_name'] = $user['name'];
                header('location:dashboard.php'); // Redirect to dashboard
                exit();
            } else {
                $msg = "Incorrect password!";
            }
        } else {
            $msg = "No user found with this email!";
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediPath LevelUp - Login</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <style>
        body {
            background-color: #121212;
            color: #fff;
            font-family: 'Segoe UI', sans-serif;
        }
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            background-color: #1e1e1e;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        }
        .login-container h2 {
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
    <div class="login-container">
        <form action="" method="post">
            <h2>MediPath LevelUp</h2>
            <p class="msg"><?= $msg ?></p>
            <div class="form-group">
                <input type="email" name="email" placeholder="Email Address" class="form-control" required>
            </div>
            <div class="form-group">
                <input type="password" name="password" placeholder="Password" class="form-control" required>
            </div>
            <button class="btn" name="submit">Login</button>
            <p>Don't have an account? <a href="register.php">Sign Up</a></p>
        </form>
    </div>
</body>
</html>

