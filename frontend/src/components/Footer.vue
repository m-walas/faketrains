<template>
  <v-footer class="footer">
    <v-container fluid>
      <!-- for bigger screens -->
      <v-row align="center" justify="space-between" class="hidden-sm-and-down">
        <!-- version -->
        <v-col cols="auto">
          <span class="footer-version-info">v3.0.1</span>
        </v-col>

        <!-- author info -->
        <v-col cols="auto" class="text-center">
          © 2023 Mateusz Walas | Maja Wiśniewska | Dawid Burda
        </v-col>

        <!-- Buttons GitHub and Portfolio -->
        <v-col cols="auto" class="footer-buttons-col">
          <v-btn
            icon
            href="https://github.com/m-walas/faketrains"
            target="_blank"
            class="footer-icon-btn footer-github-btn"
            aria-label="GitHub Repository"
            @mousemove="handleMouseMove"
            @mouseleave="resetMousePosition"
          >
            <v-icon>mdi-github</v-icon>
          </v-btn>
          <v-btn
            icon
            href="https://mwalas.pl"
            target="_blank"
            class="footer-icon-btn footer-portfolio-btn"
            aria-label="Portfolio Website"
            @mousemove="handleMouseMove"
            @mouseleave="resetMousePosition"
          >
            <v-icon>mdi-web</v-icon>
          </v-btn>
        </v-col>
      </v-row>

      <!-- for smaller screens -->
      <v-row align="center" justify="center" class="hidden-md-and-up">
        <!-- author info -->
        <v-col cols="12" class="text-center">
          © 2023 Mateusz Walas | Maja Wiśniewska | Dawid Burda
        </v-col>

        <!-- version and buttons -->
        <v-col cols="12" class="text-center footer-version-buttons-row">
          <span class="footer-version-info">v3.0.1</span>
          <v-btn
            icon
            href="https://github.com/m-walas/faketrains"
            target="_blank"
            class="footer-icon-btn footer-github-btn"
            aria-label="GitHub Repository"
            @mousemove="handleMouseMove"
            @mouseleave="resetMousePosition"
          >
            <v-icon>mdi-github</v-icon>
          </v-btn>
          <v-btn
            icon
            href="https://mwalas.pl"
            target="_blank"
            class="footer-icon-btn footer-portfolio-btn"
            aria-label="Portfolio Website"
            @mousemove="handleMouseMove"
            @mouseleave="resetMousePosition"
          >
            <v-icon>mdi-web</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  methods: {
    handleMouseMove(event) {
      const btn = event.currentTarget;
      const rect = btn.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      btn.style.setProperty('--mouse-x', `${x}%`);
      btn.style.setProperty('--mouse-y', `${y}%`);
    },
    resetMousePosition(event) {
      const btn = event.currentTarget;
      btn.style.removeProperty('--mouse-x');
      btn.style.removeProperty('--mouse-y');
    },
  },
};
</script>

<style scoped>
.footer {
  --footer-bg-color: rgba(0, 0, 0, 0.8);
  --footer-text-color: rgba(255, 255, 255, 0.85);
  --footer-muted-text-color: rgba(66, 66, 66, 0.5);
  --footer-font-size: clamp(0.8rem, 1vw, 1rem);
  --footer-height: clamp(50px, 5vw, 80px);

  background-color: var(--footer-bg-color);
  color: var(--footer-muted-text-color);
  box-shadow: 0 -1px 5px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  animation: footer-fadeIn 1s ease;
  min-height: var(--footer-height);
}

.footer-author-info,
.footer-version-info {
  font-size: var(--footer-font-size);
  margin-bottom: 0;
  transition: color 0.3s ease;
}

.footer-icon-btn {
  color: #fff;
  background-color: transparent !important;
  position: relative;
  transition: transform 0.2s ease-out;
  margin-left: 4px;
  box-shadow: none !important;
  padding: 4px;
}

.footer-buttons-col .footer-icon-btn:first-of-type {
  margin-left: 0;
}

.footer-icon-btn .v-icon {
  color: #fff;
  font-size: 20px;
}

.footer-icon-btn:hover .v-icon {
  color: #bbb;
}

.footer-icon-btn::before {
  content: '';
  position: absolute;
  top: -5px;
  left: -5px;
  width: calc(100% + 10px);
  height: calc(100% + 10px);
  border: 1px solid rgba(255, 255, 255, 0);
  border-radius: 50%;
  box-sizing: border-box;
  transform: rotate(0deg);
  transition: border-color 0.3s ease, opacity 0.3s ease;
  opacity: 0;
  pointer-events: none;
}

.footer-icon-btn:hover::before {
  border-color: rgba(255, 255, 255, 0.5);
  opacity: 1;
  animation: footer-rotateBorder 10s linear infinite;
}

.footer-icon-btn:hover {
  background-color: transparent !important;
  box-shadow: none !important;
  background-image: none !important;
  transform: translate(
    calc((var(--mouse-x, 50%) - 50%) / 5),
    calc((var(--mouse-y, 50%) - 50%) / 5)
  );
  cursor: none;
}

@keyframes footer-rotateBorder {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

@keyframes footer-fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .footer-icon-btn::before,
  .footer-icon-btn:hover {
    animation: none;
    transform: none;
  }

  .footer-footer {
    animation: none;
  }
}

.footer-version-buttons-row {
  display: flex;
  align-items: center;
  justify-content: center;
}

.footer-version-info {
  margin-right: 8px;
}

@media (max-width: 600px) {
  .footer-author-info,
  .footer-version-info {
    font-size: clamp(0.8rem, 2.5vw, 1rem);
  }

  .footer-icon-btn .v-icon {
    font-size: 16px;
  }

  .footer-icon-btn {
    padding: 3px;
    margin-left: 3px;
  }
}
</style>
