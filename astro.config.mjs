import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://www.andrewaitken.com',
  markdown: {
    shikiConfig: {
      theme: 'one-dark-pro',
    },
  },
});
