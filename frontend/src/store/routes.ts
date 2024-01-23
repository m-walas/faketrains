// stores/routes.ts
import { defineStore } from 'pinia';

interface RouteLeg {
  train_id: string;
  departure_city: string;
  departure_time: string;
  arrival_city: string;
  arrival_time: string;
  ticket_price: string;
  travel_time: string;
}

interface DirectRoute extends RouteLeg {
  is_transfer: false;
}

interface TransferRoute {
  is_transfer: true;
  first_leg: RouteLeg;
  second_leg: RouteLeg;
}

type Route = DirectRoute | TransferRoute;

interface RouteState {
  schedules: Route[];
  selectedDepartureDate: string | null;
}

export const useRoutesStore = defineStore('routes', {
  state: (): RouteState => ({
    schedules: [],
    selectedDepartureDate: null,
  }),
  actions: {
    setSchedules(data: Route[]) {
      this.schedules = data;
    },
    setSelectedDepartureDate(date: string) {
      this.selectedDepartureDate = date;
    },
  },
});
