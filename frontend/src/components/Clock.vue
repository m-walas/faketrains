<template>
  <div class="clock">
    <font-awesome-icon icon="clock" />
    <span>{{ time }}</span>
  </div>
</template>


<style scoped>
.clock {
  font-family: 'Roboto', 'Arial', sans-serif;
  color: #fff;
  background-color: transparent;
  padding: 0.5vw 1vw;
  border-radius: 0.5vw;
  display: inline-block;
  font-size: 1.2vw;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}
/* style for mobile devices */
/* for mobile do not display clock */
@media (max-width: 480px) {
  .clock {
    display: none !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .clock {
    font-size: 3vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .clock {
    font-size: 1vw;
  }
}

.clock .fa-clock {
  margin-right: 0.5vw;
  color: #6f27ff;
}

.clock:hover {
  background-color: #16030a;
  box-shadow: 0 0.2vw 0.4vw rgba(0, 0, 0, 0.3);
}
</style>

<script>
export default {
  data() {
    return {
      time: null,
      timer: null,
    };
  },
  created() {
    this.updateTime();
    this.timer = setInterval(this.updateTime, 1000);
  },
  beforeDestroy() {
    clearInterval(this.timer);
  },
  methods: {
    updateTime() {
      const currentTime = new Date();
      this.time = currentTime.toLocaleTimeString();
    },
  },
};
</script>