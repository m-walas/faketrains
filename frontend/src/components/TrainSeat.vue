<template>
  <div
    class="train-seat"
    :class="{ 'reserved': isReserved, 'confirmed': isConfirmed }"
    @click="reserveSeat"
  >
    <button v-if="!isConfirmed" @click="confirmSeat">Zatwierdź</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isReserved: false,
      isConfirmed: false,
    };
  },
  methods: {
    reserveSeat() {
      if (!this.isConfirmed) {
        this.isReserved = !this.isReserved;
      }
    },
    confirmSeat() {
      this.isConfirmed = true;
      this.sendReservation();
    },
    sendReservation() {
      const data = {
        seatNumber: this.seatNumber, // Dodaj numer miejsca lub identyfikator
        isReserved: this.isReserved,
        isConfirmed: this.isConfirmed,
      };

      // Przykładowe wysłanie danych przez WebSocket (wymaga konfiguracji WebSocket)
      this.$socket.sendObj(data);
    },
  },
};
</script>

<style>
.train-seat {
  width: 50px;
  height: 50px;
  background-color: green;
  border: 1px solid #000;
  cursor: pointer;
  display: inline-block;
  text-align: center;
  vertical-align: middle;
  line-height: 50px;
  font-weight: bold;
}

.reserved {
  background-color: gray;
  cursor: not-allowed;
}

.confirmed {
  background-color: red;
}
</style>
