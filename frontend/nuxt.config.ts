import { resolve } from 'path';

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: [
    "@/assets/scss/tailwind.css",
    "@/assets/scss/layered.tailwind.css",
    "@/assets/scss/main.scss",
    "primeicons/primeicons.css",
    'primevue/resources/themes/lara-dark-green/theme.css',
  ],
  devtools: {
    enabled: true,

    timeline: {
      enabled: true
    }
  },
  modules: [
    'nuxt-primevue',
    '@nuxtjs/tailwindcss',
    "@pinia/nuxt",
    "nuxt-icon"
  ],
  primevue: {
    components: {
        include: "*",
        prefix: "Prime"
    },
    options: {
      unstyled: true
    },
    importPT: { as: 'Tailwind', from: 'primevue/passthrough/tailwind' },
    cssLayerOrder: 'tailwind-base, primevue, tailwind-utilities'
  },
  pinia: {
    storesDirs: ['./stores/**']
  }
})