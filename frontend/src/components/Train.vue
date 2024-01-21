<template>
    <div class="train">
      <div v-for="row in seats" :key="row[0].id" class="seat-row">
        <div v-for="seat in row" :key="seat.id" @click="handleSeatClick(seat)" :class="{ 'seat-selected': seat.selected, 'seat-reserved': seat.reserved }">{{ seat.id }}</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      const numRows = 2;
      const seatsPerRow = 5;
  
      const seats = Array.from({ length: numRows }, (_, rowIndex) =>
        Array.from({ length: seatsPerRow }, (_, seatIndex) => ({
          id: seatIndex * numRows + rowIndex + 1,
          selected: false,
          reserved: false,
        }))
      );
  
      seats[0][1].reserved = true;
      seats[1][3].reserved = true;
  
      return {
        seats,
      };
    },
    methods: {
      handleSeatClick(seat) {
        console.log('Clicked seat:', seat);
        if (!seat.reserved) {
          // Toggle the selected state
        this.seats.forEach(row => row.forEach(seat => (seat.selected = false)));

        seat.selected = !seat.selected;
        console.log('Selected:', seat.selected);
        }
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
    gap: 50px; /* Reduce the gap between seat rows for better visibility */
    background-color: #333; /* Train body color */
    padding: 10px; /* Adjust as needed */
    border-radius: 20px; /* Adjust as needed */
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
  