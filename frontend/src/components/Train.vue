<template>
  <div class="text-center">
    <v-card class="text-center my-4 mx-4" style="border-radius: 50px">
      <v-card-text class="text-h3 my-4 mx-4 text-center font-weight-bold"
        >Wybierz miejsce</v-card-text
      >
      <div class="d-flex justify-center">
        <div class="train">
          <div v-for="row in seats" :key="row[0].id" class="seat-row">
            <div
              v-for="seat in row"
              :key="seat.id"
              @click="handleSeatClick(seat)"
              :class="{
                'seat-selected': seat.selected,
                'seat-reserved': seat.reserved,
              }"
            >
              {{ seat.id }}
            </div>
          </div>
        </div>
      </div>
      <v-btn
        class="confirm-btn my-4 justify-center"
        @click="confirmSeat"
        color="primary"
        :disabled="!isAnySeatSelected"
      >
        Potwierdź
      </v-btn>
      <div class="text-center">
        <v-snackbar v-model="snackbar" :timeout="2000" color="blue-grey">
          Maksymalna liczba miejsc do zarezerwowania to:
          {{ this.maxSeatsToSelect }}
        </v-snackbar>
      </div>
    </v-card>
  </div>
</template>

<script lang="ts">
import { useButtonStore } from "@/store/buttonStore";
export default {
  data() {
    const numRows = 2;
    const seatsPerRow = 5;

    const seats = Array.from({ length: numRows }, (_, rowIndex) =>
      Array.from({ length: seatsPerRow }, (_, seatIndex) => ({
        id: seatIndex * numRows + rowIndex + 1,
        selected: false,
        reserved: false,
        confirmed: false,
      }))
    );

    seats[0][1].reserved = true;
    seats[1][3].reserved = true; //Hardcoded for test

    return {
      snackbar: false,
      maxSeatsToSelect: 3,
      seats,
      ws: new WebSocket("ws://localhost:8000/ws/train_seat/"),
    };
  },
  methods: {
    handleSeatClick(seat) {
      console.log("Clicked seat:", seat);
      if (!seat.reserved) {
        console.log("Clicked seat:", seat);

        const selectedSeatsCount = this.getSelectedSeatsCount();

        if (seat.selected) {
          seat.selected = false;
          console.log("Deselected:", seat.id);
        } else if (selectedSeatsCount < this.maxSeatsToSelect) {
          seat.selected = true;
          console.log("Selected:", seat.id);
        } else {
          this.snackbar = true;
        }
      }
    },
    confirmSeat() {
      const selectedSeats = this.getSelectedSeats();
      const seatNumbers = selectedSeats.map((seat) => seat.id);

      this.sendMessage(seatNumbers);
      useButtonStore().setShowTrainSeats(false);
    },

    getSelectedSeats() {
      // Return an array of currently selected seats
      return this.seats
        .flatMap((row) => row.filter((seat) => seat.selected))
        .sort((a, b) => a.id - b.id);
    },
    getSelectedSeatsCount() {
      // Count the number of currently selected seats
      let count = 0;
      this.seats.forEach((row) => {
        row.forEach((seat) => {
          if (seat.selected) {
            count++;
          }
        });
      });
      return count;
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
    this.ws.onopen = function (event) {
      console.log("Connected");
    };
  },
  computed: {
    isAnySeatSelected() {
      return this.seats.some((row) => row.some((seat) => seat.selected));
    },
  },
};
</script>

<style scoped>
.train {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 400px;
  gap: 50px;
  background-color: #333;
  padding: 10px;
  border-radius: 20px;
}

.seat-row {
  display: flex;
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
</style>
