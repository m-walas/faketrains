<template>
  <div class="route-details">
    <h3 class="details-heading">Szczegóły Trasy</h3>

    <div v-if="route.first_leg && route.second_leg">
      <div class="leg-details">
        <h4>
          Pierwszy odcinek: {{ route.first_leg.departure_city }} -
          {{ route.first_leg.arrival_city }}
        </h4>
        <p class="train_id">
          {{ route.first_leg.train_id }}
        </p>
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

      <div class="ticket-options">
        <h3>Wybór biletów</h3>
        <p>{{ route.first_leg.train_id }}</p>
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
        <v-btn text small class="button-choose-seat" @click="selectSeats">
          Wybierz miejsce
        </v-btn>
      </div>

      <div class="leg-details">
        <h4>
          Drugi odcinek: {{ route.second_leg.departure_city }} -
          {{ route.second_leg.arrival_city }}
        </h4>
        <p class="train_id">
          {{ route.second_leg.train_id }}
        </p>
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

      <div class="ticket-options">
        <h3>Wybór biletów</h3>
        <p>{{ route.second_leg.train_id }}</p>
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
        <v-btn text small class="button-choose-seat" @click="selectSeats">
          Wybierz miejsce
        </v-btn>
      </div>
    </div>

    <div v-else>
      <div class="direct-route-details">
        <h4>{{ route.departure_city }} - {{ route.arrival_city }}</h4>
        <p class="train_id">
          {{ route.train_id }}
        </p>
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
        <v-btn text small class="button-choose-seat" @click="selectSeats">
          Wybierz miejsce
        </v-btn>
      </div>
    </div>

  </div>

  <div>
    <PassengerForm v-if="selectedSeats.length > 0" :selectedSeats="selectedSeats" />
  </div>
</template>

<script>
import { useButtonStore } from "@/store/buttonStore";
import { useTicketStore } from "@/store/ticketStore";
import { useRoute } from "vue-router";
import { useRoutesStore } from "@/store/routes";
import PassengerForm from "./PassengerForm.vue";
import { useTransactionStore } from "@/store/transactionStore";
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
      const buttonStore = useButtonStore();
      const transactionStore = useTransactionStore();

      buttonStore.setSelectedRouteDetails({
        trainId: this.route.train_id,
        departureDate: this.departureDate,
        departureTime: this.route.departure_time
      });
      buttonStore.setShowTrainSeats(true);

      transactionStore.setTransactionDetails(
        `${this.route.departure_city} - ${this.route.arrival_city}`,
        this.route.train_id,
        this.route.ticket_price,
        [] 
      );
    },
  },
  components: {
    PassengerForm,
  },
  computed: {
    departureDate() {
      return useRoutesStore().selectedDepartureDate;
    },
    ticketStore() {
      return useTicketStore();
    },
    selectedSeats() {
      const ticketStore = useTicketStore();
      return ticketStore.getSelectedSeats;
    },
  },
  watch: {
    selectedTicketCount(newValue) {
      useTicketStore().setTicketsCount(newValue);
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

.train_id {
  font-style: italic;
  color: #1976d2;
  margin-bottom: 15px;
  font-size: 12px;
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
