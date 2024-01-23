<template>
  <v-container fill-height fluid>
    <v-layout align-center justify-center>
      <Routes></Routes>

      <v-overlay v-model="showTrain" class="d-flex justify-center align-center">
        <Train :trainId="selectedTrainId" :departureDate="selectedDepartureDate" :departureTime="selectedDepartureTime"></Train>
      </v-overlay>
    </v-layout>
  </v-container>
</template>

<script lang="ts">
import Routes from "../components/Routes.vue";
import Train from "@/components/Train.vue";
import { useButtonStore } from "@/store/buttonStore";
import { useRoutesStore } from "../store/routes";

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
    selectedTrainId() {
      return useButtonStore().selectedTrainId;
    },
    selectedDepartureDate() {
      return useRoutesStore().selectedDepartureDate;
    },
    selectedDepartureTime() {
      return useButtonStore().selectedDepartureTime;
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
  margin: auto;
  text-align: center;
}
</style>
