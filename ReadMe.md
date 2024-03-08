<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formatted Data</title>
<style>
  .page {
    color: #0ff;
  }
  .access-level {
    color: #0ff;
  }
  .database {
    color: white;
  }
  .database_header{
    color: #0ff;
  }
</style>
</head>
<body>
  <h2>Pages:</h2>
  <ul>
    <li class="page">AccountInfo</li>
    <li class="page">Admin_Page</li>
    <li class="page">Contact_Us</li>
    <li class="page">Home</li>
    <li class="page">Product</li>
    <li class="page">SCADA</li>
    <li class="page">SignIn</li>
    <li class="page">SignUp</li>
  </ul>

  <h2>Access Level and Page Access:</h2>
  <ul>
    <li><span class="access-level">Admin:</span> "Admin", "Product", "SCADA", "My Account"</li>
    <li><span class="access-level">User:</span> "Home", "Contact", "Product", "My Account"</li>
    <li><span class="access-level">Guest:</span> "Home", "Contact", "Product", "Sign In", "Sign Up"</li>
  </ul>

  <h2>Databases:</h2>
  <ul>
    <li class="database_header">Product:
      <ul class="database">
        <li>PRODUCT_DB: products.db</li>
        <li>format: ['ID', 'Name']</li>
        <li>PRODUCT_PATH: "./database/products/"</li>
      </ul>
    </li>
    <li class="database_header">Users:
      <ul class="database">
        <li>USER_DB: users.db</li>
        <li>format: ['ID', 'first_name', 'last_name', 'gender', 'email', 'phone', 'pass', 'access']</li>
        <li>USER_PATH: "./database/users/"</li>
      </ul>
    </li>
    <li class="database_header">Orders:
      <ul class="database">
        <li>ORDER_DB: orders.db</li>
      </ul>
    </li>
  </ul>

  <h2>Important Variable in session_state</h2>
  
</body>
</html>
