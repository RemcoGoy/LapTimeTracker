<template>
  <NuxtLayout>
    <NuxtPage :page-key="route => route.fullPath" />
  </NuxtLayout>
</template>

<style lang="scss">
@use "~/assets/scss/main.scss"
</style>