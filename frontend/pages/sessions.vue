<template>
  <div>
    <PrimeDataTable :value="sessions" class="mt-2">
      <PrimeColumn field="code" header="Code"></PrimeColumn>
      <PrimeColumn field="name" header="Name"></PrimeColumn>
      <PrimeColumn field="category" header="Category"></PrimeColumn>
      <PrimeColumn field="quantity" header="Quantity"></PrimeColumn>
    </PrimeDataTable>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

definePageMeta({
  key: (route: any) => route.fullPath
})

const sessions = ref([
  {
    code: "asdf",
    name: "products",
    category: 'asdf',
    quantity: 1
  }
])
</script>