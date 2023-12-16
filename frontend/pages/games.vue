<template>
  <div>
    <div class="flex justify-between">
      <div>Hello</div>
      <PrimeButton class="mt-2 mb-1 p-2" icon="pi pi-plus" label="Add" />
    </div>
    <PrimeDataTable class="mt-2" :value="games" tableStyle="min-width: 50rem">
      <PrimeColumn field="name" header="Name"></PrimeColumn>
    </PrimeDataTable>
  </div>
</template>

<script setup lang="ts">
import { useGamesStore } from "@/stores/game_store";
import { storeToRefs } from 'pinia';

const store = useGamesStore();
const { games, currentGame } = storeToRefs(store);
const { fetchGames } = store;

fetchGames();

</script>