// stores/ticketStore.js
import { defineStore } from 'pinia';


export interface SeatWithPassenger {
  seat_number: string;
  passenger: {
    firstName: string;
    lastName: string;
  };
}

export interface TicketState {
  ticketsCount: number;
  reduced: boolean;
  selectedSeats: SeatWithPassenger[];
}


export const useTicketStore = defineStore({
  id: 'ticket',
  state: (): TicketState => ({
    ticketsCount: 0,
    reduced: false,
    selectedSeats: [],
  }),
  getters: {
    getTicketsCount(state) {
      return state.ticketsCount;
    },
    getSelectedSeats(state) {
      return state.selectedSeats;
    }
  },
  actions: {
    setTicketsCount(value: number) {
      this.ticketsCount = value;
    },
    setIsReduced(value: boolean) {
      this.reduced = value;
    },
    setSelectedSeats(seats: SeatWithPassenger[]) { 
      this.selectedSeats = seats;
    },
    clearSelectedSeats() {
      this.selectedSeats = [];
    },
    clearTicketsCount() {
      this.ticketsCount = 0;
    },
  },
});
