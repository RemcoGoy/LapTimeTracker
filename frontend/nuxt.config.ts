// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['primevue/resources/themes/lara-dark-green/theme.css', "@/assets/scss/main.scss", "primeicons/primeicons.css"],
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
    }
  },
  pinia: {
    storesDirs: ['./stores/**']
  }
})