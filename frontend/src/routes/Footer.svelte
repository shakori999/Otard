<!-- Footer.svelte -->

<script>
  // You can add any logic or data here as needed
  let currentYear = new Date().getFullYear();

  // Placeholder social media links (replace with your own)
  let socialMediaLinks = [
    { name: "Facebook", url: "https://www.facebook.com" },
    { name: "Twitter", url: "https://www.twitter.com" },
    { name: "LinkedIn", url: "https://www.linkedin.com" },
  ];
</script>

<footer>
  <div class="container">
    <div class="footer-content">
      <p>&copy; {currentYear} Your Company Name. All rights reserved.</p>
      <div class="social-links">
        {#each socialMediaLinks as link}
          <a href={link.url} target="_blank" rel="noopener noreferrer">
            <img src={`images/${link.name.toLowerCase()}.png`} alt={link.name} />
          </a>
        {/each}
      </div>
    </div>
  </div>
</footer>

<style>
  /* Add your custom CSS styles for the footer here */
  footer {
    background-color: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .footer-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .social-links {
    display: flex;
    gap: 10px;
  }

  .social-links img {
    width: 24px;
    height: 24px;
  }
</style>

