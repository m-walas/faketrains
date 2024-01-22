<template>
  <div class="route-details">
    <h3 class="details-heading">Szczegóły Trasy</h3>

    <div v-if="route.first_leg && route.second_leg">
      <div class="leg-details">
        <h4>
          Pierwszy odcinek: {{ route.first_leg.departure_city }} -
          {{ route.first_leg.arrival_city }}
        </h4>
        <p>
          <v-icon small>mdi-train</v-icon> Odjazd:
          {{ route.first_leg.departure_time }}
        </p>
        <p>
          <v-icon small>mdi-train</v-icon> Przyjazd:
          {{ route.first_leg.arrival_time }}
        </p>
        <p>
          <v-icon small>mdi-clock-outline</v-icon> Czas podróży:
          {{ route.first_leg.travel_time }}
        </p>
        <p>
          <v-icon small>mdi-cash-multiple</v-icon> Cena:
          {{ route.first_leg.ticket_price }}
        </p>
      </div>

      <div class="leg-details">
        <h4>
          Drugi odcinek: {{ route.second_leg.departure_city }} -
          {{ route.second_leg.arrival_city }}
        </h4>
        <p>
          <v-icon small>mdi-train</v-icon> Odjazd:
          {{ route.second_leg.departure_time }}
        </p>
        <p>
          <v-icon small>mdi-train</v-icon> Przyjazd:
          {{ route.second_leg.arrival_time }}
        </p>
        <p>
          <v-icon small>mdi-clock-outline</v-icon> Czas podróży:
          {{ route.second_leg.travel_time }}
        </p>
        <p>
          <v-icon small>mdi-cash-multiple</v-icon> Cena:
          {{ route.second_leg.ticket_price }}
        </p>
      </div>
    </div>

    <div v-else>
      <div class="direct-route-details">
        <h4>{{ route.departure_city }} - {{ route.arrival_city }}</h4>
        <p>
          <v-icon small>mdi-train</v-icon> Odjazd: {{ route.departure_time }}
        </p>
        <p>
          <v-icon small>mdi-train</v-icon> Przyjazd: {{ route.arrival_time }}
        </p>
        <p>
          <v-icon small>mdi-clock-outline</v-icon> Czas podróży:
          {{ route.travel_time }}
        </p>
        <p>
          <v-icon small>mdi-cash-multiple</v-icon> Cena:
          {{ route.ticket_price }}
        </p>
      </div>
    </div>

    <div class="ticket-options">
      <h3>Wybór biletów</h3>
      <div class="option">
        <label>Ilość biletów:</label>
        <select v-model="selectedTicketCount">
          <option value="0">0</option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>
      </div>
      <div class="option">
        <label>Ulga:</label>
        <select v-model="selectedDiscount">
          <option value="normal">Normalny</option>
          <!-- <option value="student">Student</option> -->
        </select>
      </div>
      <v-btn text small class="button-choose-seat" @click="selectSeats"
        >Wybierz miejsce</v-btn
      >
    </div>
  </div>
</template>

<script>
import { useButtonStore } from "@/store/buttonStore";
export default {
  props: {
    route: Object,
  },
  data() {
    return {
      selectedTicketCount: 0,
      selectedDiscount: "normal",
    };
  },
  methods: {
    selectSeats() {
      useButtonStore().setShowTrainSeats(true);
      console.log(useButtonStore().getShowTrainSeats);
    },
  },
};
</script>

<style scoped>
.route-details {
  padding: 15px;
  border-radius: 8px;
  background-color: #f2f2f2;
  margin-top: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.details-heading {
  font-weight: bold;
  color: #1976d2;
  margin-bottom: 10px;
}

.leg-details,
.direct-route-details {
  margin-bottom: 15px;
  padding: 10px;
  background-color: white;
  border-radius: 5px;
}

.leg-details h4,
.direct-route-details h4 {
  color: #333;
  font-weight: bold;
}

p {
  margin: 5px 0;
  line-height: 1.6;
  color: #555;
}

v-icon {
  margin-right: 5px;
}

.option {
  margin-bottom: 15px;
}

option {
  padding: 10px;
}

select {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: white;
  cursor: pointer;
  appearance: none;
  width: 100%;
}

select:focus {
  outline: none;
  border-color: #0056b3;
}

.ticket-options {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  background-color: white;
  padding: 15px;
  border-radius: 8px;
}

.ticket-options h3 {
  margin-top: 0;
}

.button-choose-seat {
  margin-top: 25px;
  background-color: #0056b3;
  color: white;
  text-transform: uppercase;
  font-weight: bold;
}

.button-choose-seat:hover {
  background-color: #003d82;
}
</style>
