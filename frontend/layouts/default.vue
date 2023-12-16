<template>
  <div class="m-2">
    <PrimeMenubar :model="items">
      <template #item="{ item, props, hasSubmenu }">
        <router-link v-if="item.route" v-slot="{ href, navigate }" :to="item.route" custom>
          <a v-ripple :href="href" v-bind="props.action" @click="navigate">
            <span :class="item.icon" />
            <span class="ml-2">{{ item.label }}</span>
          </a>
        </router-link>
        <a v-else v-ripple :href="item.url" :target="item.target" v-bind="props.action">
          <span :class="item.icon" />
          <span class="ml-2">{{ item.label }}</span>
          <span v-if="hasSubmenu" class="pi pi-fw pi-angle-down ml-2" />
        </a>
      </template>
      <!-- <template #end>
        <PrimeDropdown v-model="currentGame" :options="games" optionLabel="name" optionValue="key"
          placeholder="Select a Game" class="w-80" />
      </template> -->
    </PrimeMenubar>

    <slot />
  </div>
</template>

<script setup>
import { ref } from "vue";

const items = ref([
  {
    label: "Home",
    icon: 'pi pi-home',
    route: "/"
  },
  {
    label: "Sessions",
    icon: 'pi pi-sessions',
    route: "/sessions"
  },
  {
    label: "Games",
    icon: 'pi pi-games',
    route: "/games"
  }
]);

</script>