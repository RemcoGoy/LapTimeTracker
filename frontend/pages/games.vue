<template>
  <PrimeDataTable class="mt-2" :value="games" tableStyle="min-width: 50rem">
    <template #header>
      <div class="flex flex-wrap align-items-center justify-content-between gap-2">
        <span class="text-xl text-900 font-bold">Games</span>
        <PrimeButton icon="pi pi-refresh" rounded raised />
      </div>
    </template>

    <PrimeColumn field="name" header="Name"></PrimeColumn>
  </PrimeDataTable>
</template>

<script setup lang="ts">
import { useGamesStore } from "@/stores/game_store";
import { storeToRefs } from 'pinia';

const store = useGamesStore();
const { games, currentGame } = storeToRefs(store);
const { fetchGames } = store;

fetchGames();

</script>