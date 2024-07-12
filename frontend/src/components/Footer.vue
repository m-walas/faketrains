<template>
    <v-footer class="footer">
      <v-container>
        <v-row justify="center" align="center">
          <v-col cols="12" class="text-center">
            © 2023 Mateusz Walas | Maja Wiśniewska | Dawid Burda
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
</template>

<style scoped>
.footer {
  padding: 1vw 0;
  color: #fff;
  box-shadow: 0 -0.1vw 0.2vw rgba(0, 0, 0, 0.1);
  font-size: 0.7vw;
  max-height: 1.8vw;
  background-color: rgba(0, 0, 0, 0.8) !important;
}
/* style for mobile devices */
@media (max-width: 480px) {
  .footer {
    font-size: 2.2vw;
    max-height: 5.5vw;
  }
}
/* style for tablets */
@media (max-width: 768px) {
  .footer {
    font-size: 1.5vw;
    max-height: 2vw;
  }
}
/* style for 21:9 monitors */
@media (min-width: 2560px) {
  .footer {
    font-size: 0.5vw;
    max-height: 0.1vw;
  }
}
</style>
