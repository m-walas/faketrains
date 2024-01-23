import { defineStore } from 'pinia';

export const useButtonStore = defineStore({
  id: 'button',
  state: () => ({
    showTrainSeats: false,
    selectedTrainId: null,
    selectedDepartureTime: null,
  }),
  getters: {
    getShowTrainSeats(state) {
      return state.showTrainSeats;
    },
  },
  actions: {
    setShowTrainSeats(value) {
      this.showTrainSeats = value;
    },
    setSelectedRouteDetails(route) {
      this.selectedTrainId = route.trainId;
      this.selectedDepartureTime = route.departureTime;
    }
  },
});
