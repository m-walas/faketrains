<template>
  <v-container fluid class="search-form-main-container">
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card class="search-form-card">
          <v-card-title class="search-form-title">Znajdź Połączenie</v-card-title>
          <v-divider class="search-form-divider"></v-divider>

          <v-card-text>
            <Multiselect
              class="search-form-field"
              v-model="selectedCityFrom"
              :options="cities"
              placeholder="Wybierz miasto początkowe"
              label="name"
              track-by="name"
              :searchable="true"
              @update:modelValue="handleCityFromChange"
            />
            <Multiselect
              class="search-form-field"
              v-model="selectedCityTo"
              :options="cities"
              placeholder="Wybierz miasto docelowe"
              label="name"
              track-by="name"
              :searchable="true"
              @update:modelValue="handleCityToChange"
            />
          </v-card-text>

          <v-divider class="search-form-divider"></v-divider>
          <v-card-text>
            <v-text-field
              type="date"
              label="Data"
              class="search-form-field"
              v-model="selectedDate"
            ></v-text-field>
          </v-card-text>

          <v-divider class="search-form-divider"></v-divider>
          <v-card-actions class="search-form-actions">
            <v-spacer></v-spacer>
            <v-btn
              :disabled="!canSearch"
              @click="search"
              class="search-form-button"
              @mousemove="handleMouseMove"
              @mouseleave="resetMousePosition"
            >
              Szukaj
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog v-model="noRoutesDialog" persistent max-width="300px">
      <v-card class="search-form-dialog-card">
        <v-card-title class="search-form-dialog-title">Informacja</v-card-title>
        <v-card-text>Brak dostępnych tras dla podanych kryteriów.</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="noRoutesDialog = false">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="transactionModal.show" persistent max-width="350px">
      <v-card
        :class="[
          'search-form-dialog-card',
          transactionModal.isSuccess ? 'search-form-success-dialog' : 'search-form-error-dialog',
        ]"
      >
        <v-card-title class="search-form-dialog-title">
          {{ transactionModal.title }}
        </v-card-title>
        <v-card-text>{{ transactionModal.message }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="transactionModal.show = false">OK</v-btn>
          <v-btn
            v-if="transactionModal.isSuccess"
            class="search-form-dialog-button"
            text
            @click="goToProfile"
          >
            Przejdź do profilu
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import Multiselect from '@vueform/multiselect';
import '@vueform/multiselect/themes/default.css';
import { useRoutesStore } from '../store/routes';

export default defineComponent({
  components: { Multiselect },
  data() {
    return {
      cities: [],
      selectedCityFrom: null,
      selectedCityTo: null,
      selectedDate: '',
      noRoutesDialog: false,
      transactionModal: {
        show: false,
        title: '',
        message: '',
        isSuccess: false,
      },
      canSearch: false,
    };
  },
  methods: {
    async loadCities() {
      try {
        const response = await axios.get('/api/cities/');
        const citiesData = response.data.cities;
        this.cities = citiesData;
      } catch (error) {
        console.error('Błąd podczas pobierania miast:', error);
      }
    },
    handleCityFromChange(value) {
      this.selectedCityFrom = value;
    },
    handleCityToChange(value) {
      this.selectedCityTo = value;
    },
    goToProfile() {
      this.transactionModal.show = false;
      this.$router.push('/profile');
    },
    search() {
      if (this.selectedCityFrom && this.selectedCityTo && this.selectedDate) {
        const apiUrl = `/api/search_trains/?from=${encodeURIComponent(
          this.selectedCityFrom
        )}&to=${encodeURIComponent(this.selectedCityTo)}&date=${encodeURIComponent(
          this.selectedDate
        )}`;
        axios
          .get(apiUrl)
          .then((response) => {
            const routesStore = useRoutesStore();
            if (response.data.schedules.length === 0) {
              this.noRoutesDialog = true;
            } else {
              routesStore.setSchedules(response.data.schedules);
              routesStore.setSelectedDepartureDate(this.selectedDate);
              this.$router.push('/routes');
            }
          })
          .catch((error) => {
            console.error('Błąd podczas wyszukiwania połączeń:', error);
          });
      } else {
        console.log("Proszę wybrać miasta 'Skąd' i 'Dokąd' oraz datę");
      }
    },
    updateCanSearch() {
      this.canSearch =
        this.selectedCityFrom !== null &&
        this.selectedCityTo !== null &&
        this.selectedDate !== '';
    },
    checkTransactionStatus() {
      const params = new URLSearchParams(window.location.search);
      const status = params.get('status');
      if (status === 'success') {
        this.transactionModal.show = true;
        this.transactionModal.title = 'Sukces!';
        this.transactionModal.message = 'Twój bilet został pomyślnie zakupiony.';
        this.transactionModal.isSuccess = true;
      } else if (status === 'canceled') {
        this.transactionModal.show = true;
        this.transactionModal.title = 'Anulowano!';
        this.transactionModal.message = 'Twoja rezerwacja została anulowana.';
        this.transactionModal.isSuccess = false;
      }
    },
    handleMouseMove(event: MouseEvent) {
      const btn = event.currentTarget as HTMLElement;
      const rect = btn.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 100;
      const y = ((event.clientY - rect.top) / rect.height) * 100;
      btn.style.setProperty('--mouse-x', `${x}%`);
      btn.style.setProperty('--mouse-y', `${y}%`);
    },
    resetMousePosition(event: MouseEvent) {
      const btn = event.currentTarget as HTMLElement;
      btn.style.removeProperty('--mouse-x');
      btn.style.removeProperty('--mouse-y');
    },
  },
  mounted() {
    this.loadCities();
    this.updateCanSearch();
    this.checkTransactionStatus();
  },
  watch: {
    selectedCityFrom: 'updateCanSearch',
    selectedCityTo: 'updateCanSearch',
    selectedDate: 'updateCanSearch',
  },
});
</script>

<style scoped>
.search-form-main-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: transparent;
  padding: 0;
  overflow: hidden;
}

.search-form-card {
  width: clamp(300px, 80vw, 500px);
  background-color: rgba(0, 0, 0, 0.8);
  backdrop-filter: blur(10px);
  color: #ffffff;
  border-radius: 0px;
  padding: 2rem;
  position: relative;
  overflow: hidden;
  animation: fadeInUp 0.6s ease forwards;
  border: 2px solid transparent;
  transition: border 1s linear;
}

.search-form-card {
  border-image: linear-gradient(45deg, #ff2770, #6f27ff) 1;
  animation: borderAnimation 10s linear infinite;
}

@keyframes borderAnimation {
  0% {
    border-image: linear-gradient(45deg, #ff2770, #6f27ff) 1;
  }
  50% {
    border-image: linear-gradient(45deg, #6f27ff, #ff2770) 1;
  }
  100% {
    border-image: linear-gradient(45deg, #ff2770, #6f27ff) 1;
  }
}

.search-form-title {
  font-family: 'Segoe UI', sans-serif;
  font-size: clamp(1.5rem, 2.5vw, 2rem);
  font-weight: bold;
  color: #ffffff;
  text-align: center;
  margin-bottom: 1rem;
  position: relative;
}

.search-form-title::after {
  content: '';
  width: 0;
  height: 2px;
  background-color: #ffffff;
  display: block;
  margin: 0.5rem auto 0;
  border-radius: 2px;
  transition: width 0.5s ease;
}

.search-form-title:hover::after {
  width: 60px;
}

.search-form-field {
  margin-bottom: 1.5rem;
  font-size: clamp(1rem, 1.5vw, 1.2rem);
  color: #000;
}

.multiselect__input,
.v-text-field input {
  background-color: #ffffff;
  color: #000000;
}

.v-label {
  color: #bbb;
}

.v-input--is-focused .v-label {
  color: #ff2770;
}

.search-form-divider {
  background-color: #3a3a3a;
}

.search-form-button {
  background-color: #ff2770;
  color: #ffffff;
  font-size: clamp(1rem, 1.5vw, 1.2rem);
  padding: 0.8rem 2rem;
  border-radius: 50px;
  position: relative;
  overflow: hidden;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.search-form-button:hover {
  transform: translate(
    calc((var(--mouse-x, 50%) - 50%) / 8),
    calc((var(--mouse-y, 50%) - 50%) / 8)
  );
}

.search-form-button::before,
.search-form-button::after {
  content: none;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.search-form-dialog-card {
  border-radius: 16px;
  background-color: #1e1e1e;
  color: #ffffff;
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.6);
}

.search-form-dialog-title {
  font-weight: bold;
  font-size: clamp(1.2rem, 2vw, 1.5rem);
  color: #ffffff;
  text-align: center;
}

.search-form-success-dialog {
  border-left: 5px solid #4caf50;
}

.search-form-error-dialog {
  border-left: 5px solid #f44336;
}

@media (max-width: 600px) {
  .search-form-card {
    padding: 1.5rem;
  }
}

.v-messages {
  display: none;
}

.v-input__control {
  background-color: transparent;
  border-bottom: 1px solid rgba(255, 255, 255, 0.5);
}

.v-input--is-focused .v-input__control::after {
  border-bottom-color: #ff2770;
}

.v-input__append-inner .v-icon {
  color: #ff2770;
}

.v-text-field input {
  caret-color: #ff2770;
}

.v-text-field input::selection {
  background-color: rgba(255, 39, 112, 0.3);
}

.multiselect__content {
  background-color: #ffffff;
  color: #000000;
}

.multiselect__element--highlight {
  background-color: rgba(0, 0, 0, 0.1);
}

.multiselect__content::-webkit-scrollbar {
  width: 6px;
}

.multiselect__content::-webkit-scrollbar-thumb {
  background-color: #ff2770;
  border-radius: 3px;
}

.v-btn {
  color: #ff2770 !important;
}

.v-btn:hover {
  background-color: rgba(255, 39, 112, 0.1);
}

.v-card-text {
  color: #ffffff;
}
</style>
