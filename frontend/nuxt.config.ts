// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: ['primevue/resources/themes/lara-dark-green/theme.css'],
  devtools: { enabled: true },
  modules: [
    'nuxt-primevue',
    '@nuxtjs/tailwindcss'
  ],
  primevue: {
    components: {
        include: "*",
        prefix: "Prime"
    }
  }
})
