<template>
  <div>
    <v-card class="mx-auto" max-width="400">
      <v-card class="mx-auto my-1" max-width="400" elevation="10">
        <h2 class="my-4 mx-6">
          <v-icon>mdi-ticket-account</v-icon> Twoje Bilety
        </h2>
      </v-card>
      <v-card
        v-if="tickets.length === 0"
        class="mx-auto my-1"
        max-width="400"
        elevation="10"
      >
        <h5 class="my-4 mx-6">
          <v-icon class="ticket-info">mdi-information</v-icon> Nie masz żadnych
          biletów.
        </h5>
      </v-card>
      <v-card
        v-for="ticket in tickets"
        :key="ticket.id"
        class="mx-auto my-1"
        max-width="400"
        elevation="10"
      >
        <div class="ticket ma-5">
          <div class="travel-section">
            <h4 class="ticket-info">Trasa</h4>
            <p>
              <v-icon small>mdi-train</v-icon> <b>{{ ticket.train_name }}</b>
              {{ ticket.departure_city }}
              <v-icon small>mdi-arrow-right</v-icon> {{ ticket.arrival_city }}
            </p>
          </div>
          <div class="date-time-sections">
            <div class="date-section">
              <h4 class="ticket-info">Data</h4>
              <p><v-icon small>mdi-calendar</v-icon>{{ ticket.valid_date }}</p>
            </div>
            <div class="time-section">
              <h4 class="ticket-info">Godzina odjazdu</h4>
              <p>
                <v-icon small>mdi-clock-time-four-outline</v-icon>
                {{ ticket.departure_time }}
              </p>
            </div>
          </div>
          <div class="price-section">
            <h4 class="ticket-info">Cena</h4>
            <p><v-icon small>mdi-cash-multiple</v-icon> {{ ticket.price }}</p>
          </div>
        </div>
      </v-card>
    </v-card>
  </div>
</template>

<script lang="ts">
import axios from "axios";

interface Ticket {
  id: number;
  seat_number: string;
  valid_date: string;
  price: number;
  departure_city: string;
  arrival_city: string;
  train_name: string;
  departure_time: string;
}

export default {
  data() {
    return {
      tickets: [] as Ticket[],
    };
  },
  mounted() {
    // Fetch user's tickets when the component is mounted
    this.fetchUserTickets();
  },
  methods: {
    async fetchUserTickets() {
      try {
        const response = await axios.get("/api/tickets/");
        this.tickets = response.data;
      } catch (error) {
        console.error("Error fetching user tickets:", error);
      }
    },
  },
};
</script>

<style scoped>
.date-time-sections {
  display: flex;
  justify-content: space-between;
}

.date-section,
.price-section,
.travel-section,
.time-section {
  margin: 5px;
}

.ticket-info {
  color: #1976d2;
}
</style>
