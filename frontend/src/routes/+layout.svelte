<script>
	import Header from './Header.svelte';
  import Footer from './Footer.svelte';
  import Cart from "./Cart.svelte"
  
</script>

<div class='font-serif min-h-screen flex flex-col'>
	<Header >
    <Cart />
  </Header>

	<main class='flex-grow bg-[#fafaf9]'>
   <slot />
	</main>

  <Footer />
</div>

