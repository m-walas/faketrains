<template>
  <v-footer class="footer">
    <v-container fluid>
      <v-row class="footer-content" align="center" justify="space-between">
        <!-- For mobile devices -->
        <template v-if="isMobile">
          <v-col cols="12" class="text-center author-info">
            © 2023 Mateusz Walas | Maja Wiśniewska | Dawid Burda
          </v-col>
          <v-col cols="12" class="version-github-row">
            <span class="version-info">v2.0.2</span>
            <v-btn icon href="https://github.com/m-walas/faketrains" target="_blank" class="github-btn">
              <v-icon>mdi-github</v-icon>
            </v-btn>
          </v-col>
        </template>

        <!-- For bigger screens -->
        <template v-else>
          <v-col cols="auto">
            <span class="version-info">v2.0.2</span>
          </v-col>
          <v-col cols="auto" class="text-center author-info">
            © 2023 Mateusz Walas | Maja Wiśniewska | Dawid Burda
          </v-col>
          <v-col cols="auto">
            <v-btn icon href="https://github.com/m-walas/faketrains" target="_blank" class="github-btn">
              <v-icon>mdi-github</v-icon>
            </v-btn>
          </v-col>
        </template>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script>
export default {
  data() {
    return {
      isMobile: window.innerWidth < 600
    };
  },
  mounted() {
    window.addEventListener('resize', this.checkMobile);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.checkMobile);
  },
  methods: {
    checkMobile() {
      this.isMobile = window.innerWidth < 600;
    }
  }
};
</script>

<style scoped>
.footer {
  color: #5a5353ba;
  box-shadow: 0 -0.1vw 0.2vw rgba(0, 0, 0, 0.1);
  background-color: rgba(0, 0, 0, 0.8) !important;
  max-height: 40vw !important;
}

/* style for mobile devices */
@media (max-width: 480px) {
  .footer {
    max-height: 35vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .footer {
    max-height: 10vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .footer {
    max-height: 20vw;
  }
}

.version-info {
  float: left;
  font-size: 0.5vw;
  color: #5a5353ba;
  padding-left: 1vw;
  padding-bottom: 0vw;
}

/* style for mobile devices */
@media (max-width: 480px) {
  .version-info {
    font-size: 2.5vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .version-info {
    font-size: 1.5vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .version-info {
    font-size: 0.4vw;
  }
}

.github-btn {
  float: right;
  background-color: transparent !important;
  color: #fff;
  padding-right: 1vw;
}

.author-info {
  order: -1; /* Make authors appear first on mobile */
  margin-bottom: 0vw;
  font-size: 0.7vw;
}

/* style for mobile devices */
@media (max-width: 480px) {
  .author-info {
    font-size: 3.3vw !important;
  }
}
/* style for tablets */
@media (max-width: 1028px) {
  .author-info {
    font-size: 1.8vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2260px) {
  .author-info {
    font-size: 0.5vw;
  }
}

.version-github-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

@media (min-width: 601px) {
  .version-info, .github-btn {
    float: none !important;
    padding: 0 !important;
  }
  .author-info, .version-github-row {
    order: 0 !important;
  }
}

</style>
