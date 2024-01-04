<script>
	import Header from './Header.svelte';
  import Footer from './Footer.svelte';
  import Cart from "./Cart.svelte"
  
  import Products from "./Products.svelte"

  let featuredProducts = [
    {
      id: 1,
      name: 'Product 1',
      price: 20,
      imageUrl: 'path/to/image1.jpg',
    },
    {
      id: 2,
      name: 'Product 2',
      price: 25,
      imageUrl: 'path/to/image2.jpg',
    },
    // Add more featured products as needed
  ];
</script>

<div class='font-serif min-h-screen flex flex-col'>
	<Header >
    <Cart />
  </Header>

	<main class='flex-grow bg-[#fafaf9]'>
    <slot name="products" />
	</main>

  <Footer />
</div>

