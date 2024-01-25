<template>
  <div class="text-center">
    <v-card class="text-center my-4 mx-4" style="border-radius: 50px">
      <v-card-text class="text-h3 my-4 mx-4 text-center font-weight-bold">
        Wybierz miejsca
      </v-card-text>
      <div class="d-flex justify-center">
        <div class="train">
          <div class="seat-row">
            <div v-for="seat in seats.slice(0, 5)" :key="seat.seat_number"
                :class="{'seat-selected': seat.selected, 'seat-reserved': !seat.is_available}"
                @click="handleSeatClick(seat)">
              {{ seat.seat_number }}
            </div>
          </div>
          <div class="seat-row">
            <div v-for="seat in seats.slice(5, 10)" :key="seat.seat_number"
                :class="{'seat-selected': seat.selected, 'seat-reserved': !seat.is_available}"
                @click="handleSeatClick(seat)">
              {{ seat.seat_number }}
            </div>
          </div>
        </div>
      </div>
      <v-btn
        class="confirm-btn my-4 justify-center"
        @click="confirmSeat"
        color="primary"
        :disabled="!isAnySeatSelected || getSelectedSeatsCount() != maxSeatsToSelect">
        Potwierdź
      </v-btn>
      <p class="reservation-info">Po zatwierdzeniu miejsce zostanie tymczasowo zarezerwowane <br> i nie będzie można zmienić decyzji.</p>
      <div class="text-center">
        <v-snackbar v-model="snackbar" :timeout="2000" color="blue-grey">
          Maksymalna liczba miejsc do zarezerwowania to: {{ this.maxSeatsToSelect }}
        </v-snackbar>
      </div>
    </v-card>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import { useButtonStore } from "@/store/buttonStore";
import { useTicketStore } from "@/store/ticketStore";

export default {
  props: {
    trainId: String,
    departureDate: String,
    departureTime: String,
  },

  data() {
    return {
      seats: [],
      snackbar: false,
      maxSeatsToSelect: useTicketStore().getTicketsCount,
      // ws: new WebSocket("ws://localhost:8000/ws/train_seat/"),
      ws: new WebSocket("ws://django.mwalas.pl/ws/train_seat/"),
    };
  },

  methods: {

    async fetchSeats() {
      try {
          const url = `/api/get_train_seats_with_availability/${this.trainId}/${this.departureDate}/${this.departureTime}/`;
          const response = await axios.get(url);
          const ticketStore = useTicketStore();
          const previouslySelectedSeats = ticketStore.getSelectedSeats;

          this.seats = response.data.seats.map(seat => ({
              ...seat,
              selected: previouslySelectedSeats.some(selectedSeat => selectedSeat.seat_number === seat.seat_number)
          }));
      } catch (error) {
          console.error('Error fetching seats:', error);
      }
    },

    handleSeatClick(seat) {
      console.log("Clicked seat:", seat);

      if (seat.is_available) {
        const selectedSeatsCount = this.getSelectedSeatsCount();

        if (seat.selected) {
          seat.selected = false;
          console.log("Deselected:", seat.seat_number);
        } else if (selectedSeatsCount < this.maxSeatsToSelect) {
          seat.selected = true;
          console.log("Selected:", seat.seat_number);
        } else {
          this.snackbar = true;
        }
      }
    },

    async confirmSeat() {
      const selectedSeats = this.getSelectedSeats();
      const seatNumbers = selectedSeats.map(seat => seat.seat_number);

      const ticketStore = useTicketStore();
      ticketStore.setSelectedSeats(selectedSeats.map(seat => ({
          seat_number: seat.seat_number,
          passenger: { firstName: '', lastName: '' }
      })));

      try {
          await axios.post('/api/reserve_seats/', {
              trainId: this.trainId,
              departureDate: this.departureDate,
              departureTime: this.departureTime,
              seats: seatNumbers
          });
          console.log("Miejsca zostały zarezerwowane");
      } catch (error) {
          console.error('Error while reserving seats:', error);
      }

      useButtonStore().setShowTrainSeats(false);
    },

    getSelectedSeats() {
      return this.seats.filter(seat => seat.selected);
    },
    getSelectedSeatsCount() {
      return this.getSelectedSeats().length;
    },

    sendMessage(seatNumbers) {
      const message = JSON.stringify({
        selectedSeatNumbers: seatNumbers,
      });
      this.ws.send(message);
      console.log(seatNumbers);
    },
  },
  mounted() {
    this.fetchSeats();
    this.ws.onopen = function (event) {
      console.log("Connected");
    };
    this.$watch(
      () => useTicketStore().getTicketsCount,
      (newCount) => {
        this.maxSeatsToSelect = newCount;
      }
    );
  },
  computed: {
    isAnySeatSelected() {
      return this.getSelectedSeats().length > 0;
    },
  },
};
</script>

<style scoped>
.train {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  width: auto;
  background-color: #333;
  padding: 10px;
  border-radius: 20px;
}

.seat-row {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.seat-row > div {
  width: 50px;
  height: 50px;
  background-color: #ccc;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

.seat-selected {
  background-color: #4caf50 !important;
}

.seat-reserved {
  background-color: red !important;
}

.reservation-info {
    font-size: 12px;
    font-style: italic;
    color: grey;
    text-align: center;
    margin-top: 10px;
  }
</style>