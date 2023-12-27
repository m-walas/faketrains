<template>
  <div class="clock">
    <span>{{ time }}</span>
  </div>
</template>

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

<style scoped>
.clock {
  font-family: 'Arial', sans-serif;
  color: #333;
  background-color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  display: inline-block;
  font-size: 1.2rem;
}
</style>
