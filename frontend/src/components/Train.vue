<template>
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
  <v-btn
    class="confirm-btn mt-5"
    @click="confirmSeat"
    color="primary"
    :disabled="!isAnySeatSelected"
  >
    Potwierdź
  </v-btn>
</template>

<script lang="ts">
import { transformWithEsbuild } from "vite";

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
      seats,
      ws: new WebSocket("ws://localhost:8000/ws/train_seat/"),
    };
  },
  methods: {
    handleSeatClick(seat) {
      console.log("Clicked seat:", seat);
      if (!seat.reserved) {
        this.seats.forEach((row) =>
          row.forEach((seat) => (seat.selected = false))
        );

        seat.selected = !seat.selected;
        console.log("Selected:", seat.selected);
      }
    },
    confirmSeat() {
      const selectedSeat = this.getSelectedSeat();
      this.sendMessage(selectedSeat.id, selectedSeat.isReserved);
    },

    getSelectedSeat() {
      for (const row of this.seats) {
        for (const seat of row) {
          if (seat.selected) {
            return seat;
          }
        }
      }
      return null;
    },

    sendMessage(seatNumber, isReserved) {
      const message = JSON.stringify({
        seatNumber: seatNumber,
        isReserved: isReserved,
      });
      this.ws.send(message);
      console.log(seatNumber);
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
