<template>
  <div>
    <v-card class="mx-auto">
      <v-card-title>
        <span class="headline">Twoje Bilety</span>
      </v-card-title>
      <v-card v-for="ticket in tickets" :key="ticket.id" max-width="400">
        <v-card-text>
          <div>
            <v-subheader>Seat: {{ ticket.seat }}</v-subheader>
            <v-subheader>Valid Date: {{ ticket.valid_date }}</v-subheader>
            <v-subheader>Price: {{ ticket.price }}</v-subheader>
          </div>
        </v-card-text>
      </v-card>
    </v-card>
  </div>
</template>

<script lang="ts">
import axios from "axios";

interface Ticket {
  id: number;
  seat: string;
  valid_date: string;
  price: number;
  departure_city: string;
  arrival_city: string;
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
        console.log(response.data);
        this.tickets = response.data;
      } catch (error) {
        console.error("Error fetching user tickets:", error);
      }
    },
  },
};
</script>
