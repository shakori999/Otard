<!-- Header.svelte -->

<script>
  import { page } from '$app/stores';
  import Cart from "./Cart.svelte"; // Import any other components or data you need
  import Logo from "$lib/public/logo.svg"

  // Define any variables or functions specific to the header
</script>

<header class="header">
  <div class="container">
    <!-- Logo or site title on the left -->
    <h1 class="logo">
      <a href="/" class='flex items-center space-x-2'>
        <img src={Logo} alt="logo" width={70} height={70} />
        <span class="hidden sm:inline-block font-extrabold text-3xl text-gray-700">
          epicstore
        </span>
      </a>
    </h1>

    <!-- Navigation menu (if applicable) on the right -->
    <nav class="nav">
      <ul class="flex space-x-4">
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <!-- Add more menu items as needed -->
      </ul>
    </nav>

    <!-- Cart component -->
    <Cart />

    <!-- User profile or login/logout button (if applicable) -->
    <!-- Example:
    <div class="user-profile">
      <a href="/profile">My Profile</a>
      <button>Logout</button>
    </div>
    -->
  </div>
</header>

<style>
  /* Add your custom CSS styles for the header here */
  .header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .logo {
    font-size: 24px;
    font-weight: bold;
    margin: 0;
  }

  .nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
  }

  .nav li {
    margin-right: 20px;
  }

  .nav a {
    color: #fff;
    text-decoration: none;
  }

  /* Add more styles as needed for navigation, cart, and user profile */
</style>

