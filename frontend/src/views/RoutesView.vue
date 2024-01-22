<template>
  <v-container fill-height fluid>
    <v-layout align-center justify-center>
      <!-- Routes Component -->
      <Routes></Routes>

      <!-- Train Component (conditionally rendered) -->
      <v-overlay v-model="showTrain" class="d-flex justify-center align-center">
        <Train></Train>
      </v-overlay>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Routes from "../components/Routes.vue";
import Train from "@/components/Train.vue";
import { useButtonStore } from "@/store/buttonStore";

export default {
  data() {
    return {};
  },
  methods: {},
  computed: {
    showTrain: {
      get() {
        return useButtonStore().getShowTrainSeats;
      },
      set(value) {
        useButtonStore().setShowTrainSeats(value);
      },
    },
  },
  components: {
    Routes,
    Train,
  },
};
</script>
<style scoped>
.train-card {
  /* Adjust the max-width as needed */
  margin: auto;
  text-align: center;
}
</style>
