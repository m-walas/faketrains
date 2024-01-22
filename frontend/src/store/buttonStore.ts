import { defineStore } from 'pinia';


export const useButtonStore = defineStore({
  id: 'button',
  state: () => ({
    showTrainSeats: false,
  }),
  getters: {
    getShowTrainSeats(state){
        return state.showTrainSeats
    }
  },
  actions: {
    setShowTrainSeats(value){
        this.$patch({ showTrainSeats: value });
    }
  },
});
