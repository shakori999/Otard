<section>
  {#if featuredProducts.length > 0}
    <ul>
      {#each featuredProducts as product}
        <li>
          <img src={product.imageUrl} alt={product.name} />
          <h3>{product.name}</h3>
          <p>${product.price}</p>
          <!-- Add a link to the product page -->
          <a href="/products/{product.id}">View Details</a>
        </li>
      {/each}
    </ul>
  {:else}
    <p>No featured products available.</p>
  {/if}
</section>

<slot name="products" />
