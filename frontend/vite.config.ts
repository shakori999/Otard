import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vitest/config';
import WindiCSS from 'vite-plugin-windicss'

export default defineConfig({
	plugins: [
    WindiCSS({ config: "windi.config.ts" }),
    sveltekit(),
  ],
	test: {
		include: ['src/**/*.{test,spec}.{js,ts}']
	}
});


