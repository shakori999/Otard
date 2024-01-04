import Products from './routes/Products.svelte';
export default {
  '/': () => import('./routes/Home.svelte'),
  '/products': () => import('./src/routes/Products.svelte'),
  '/products/:id': () => import('./routes/ProductDetail.svelte'),
};
