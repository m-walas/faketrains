// stores/routes.ts
import { defineStore } from 'pinia';

interface DirectRoute {
  train_id: string;
  departure_city: string;
  departure_time: string;
  arrival_city: string;
  arrival_time: string;
  ticket_price: string;
  travel_time: string;
  is_transfer: boolean;
}

interface TransferRoute {
  first_leg: DirectRoute;
  second_leg: DirectRoute;
}

type Route = DirectRoute | TransferRoute;

interface RouteState {
  schedules: Route[];
}

export const useRoutesStore = defineStore('routes', {
  state: (): RouteState => ({
    schedules: [],
  }),
  actions: {
    setSchedules(data: Route[]) {
      this.schedules = data;
    },
  },
});
