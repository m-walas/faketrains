<template>
  <div id="app">
    <div class="train">
      <TrainSeat v-for="seat in seats" :key="seat.id" :seatNumber="seat.id" />
    </div>
  </div>
</template>

<script>
import TrainSeat from "./components/TrainSeat.vue";

export default {
  components: {
    TrainSeat,
  },
  data() {
    return {
      seats: [
        { id: 1 },
        { id: 2 },
        { id: 3 },
        // Dodaj więcej miejsc w pociągu
      ],
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.train {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

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
  margin: 5px;
}

.reserved {
  background-color: rgb(128, 128, 128);
  cursor: not-allowed;
}

.confirmed {
  background-color: red;
}
</style>
