<template>
  <div class="clock">
    <font-awesome-icon icon="clock" />
    <span>{{ time }}</span>
  </div>
</template>


<style scoped>
.clock {
  font-family: 'Roboto', 'Arial', sans-serif;
  color: #333;
  background-color: transparent;
  padding: 5px 10px;
  border-radius: 5px;
  display: inline-block;
  font-size: 1.3rem;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.clock .fa-clock {
  margin-right: 10px;
  color: #ff2770;
}

.clock:hover {
  background-color: #eaeaea;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
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