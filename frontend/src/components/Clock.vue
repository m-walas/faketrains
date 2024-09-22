<template>
  <div class="clock-component" aria-label="Current time">
    <font-awesome-icon icon="clock" class="clock-component-icon" />
    <span class="clock-component-time">{{ time }}</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      time: '',
      timer: null,
    };
  },
  mounted() {
    this.updateTime();
    this.timer = setInterval(this.updateTime, 1000);
  },
  beforeUnmount() {
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
.clock-component {
  --clock-bg-color: transparent;
  --clock-text-color: rgba(255, 255, 255, 0.85);
  --clock-font-size: clamp(1rem, 1vw + 0.5rem, 2rem);
  --clock-padding: clamp(0.3rem, 0.5vw, 1rem);

  font-family: 'Roboto', 'Arial', sans-serif;
  color: var(--clock-text-color);
  background-color: var(--clock-bg-color);
  padding: var(--clock-padding);
  border-radius: 0.5vw;
  display: inline-flex;
  align-items: center;
  font-size: var(--clock-font-size);
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
  cursor: default;
  user-select: none;
  transition: background-color 0.3s ease, box-shadow 0.3s ease;
}

.clock-component-icon {
  margin-right: 0.5vw;
  color: #6f27ff;
  animation: clock-component-pulse 1s infinite;
}

@keyframes clock-component-pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
  100% {
    transform: scale(1);
  }
}

.clock-component-time {
  display: inline-block;
  animation: clock-component-fadeIn 0.5s ease-in-out;
}

@keyframes clock-component-fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@media (max-width: 480px) {
  .clock-component {
    display: none !important;
  }
}
</style>
