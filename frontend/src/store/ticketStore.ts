import { defineStore } from 'pinia';

export interface TicketState {
  ticketsCount: number;
  reduced: boolean;
}
export const useTicketStore = defineStore({
  id: 'ticket',
  state: (): TicketState => ({
    ticketsCount: 0,
    reduced: false,
  }),
  getters: {
    getTicketsCount(state){
        return state.ticketsCount
    }
  },
  actions: {
    setTicketsCount(value: number){
        this.$patch({ ticketsCount: value });
    },
    setIsReduced(value: boolean){
        this.$patch({ reduced: value });
    }
  },
});
