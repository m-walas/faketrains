<template>
  <v-container fluid class="main-container">
    <v-row>
      <v-col cols="12" class="image-col">

        <v-card class="form-card">
          <v-card-title class="headline font-weight-bold mb-2">Znajdź Połączenie</v-card-title>
          <v-divider></v-divider>

          <v-card-text>
            <Multiselect
              class = "autocomplete-field"
              v-model="selectedCityFrom"
              :options="cities"
              placeholder="Wybierz miasto początkowe"
              label="name"
              track-by="name"
              :searchable="true"
              @update:modelValue="handleCityFromChange"
            />
            <Multiselect
              class = "autocomplete-field"
              v-model="selectedCityTo"
              :options="cities"
              placeholder="Wybierz miasto docelowe"
              label="name"
              track-by="name"
              :searchable="true"
              @update:modelValue="handleCityToChange"
            />
          </v-card-text>

          <v-divider></v-divider>
          <v-card-text>
            <v-text-field type="date" label="Data" class="date-field" v-model="selectedDate"></v-text-field>
          </v-card-text>

          <v-divider></v-divider>
          <v-card-actions>
            <v-btn :disabled="!canSearch" @click="search">Szukaj</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

  <v-dialog v-model="noRoutesDialog" persistent max-width="300px">
    <v-card>
      <v-card-title class="headline">Informacja</v-card-title>
      <v-card-text>Brak dostępnych tras dla podanych kryteriów.</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="noRoutesDialog = false">OK</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="transactionModal.show" persistent max-width="350px">
    <v-card :class="{ 'transaction-dialog': true, 'success-dialog': transactionModal.isSuccess, 'error-dialog': !transactionModal.isSuccess }">
      <v-card-title class="headline">{{ transactionModal.title }}</v-card-title>
      <v-card-text>{{ transactionModal.message }}</v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn text @click="transactionModal.show = false">OK</v-btn>
        <v-btn v-if="transactionModal.isSuccess" class="green" text @click="goToProfile">Przejdź do profilu</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<style scoped>
.main-container {
  min-height: 100vh;
}

.image-col {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  position: relative;
}

.form-card {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  padding: 24px;
  transition: all 0.3s ease-in-out;
  opacity: 0;
  animation: fadeIn 0.5s ease forwards;
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

.autocomplete-field, .date-field {
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff; 
  border: 1px solid #090a0b;
  border-radius: 4px;
  padding: 10px 15px;
  margin-bottom: 10px;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
  min-width: 250px;
}

.autocomplete-field:hover, .date-field:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.autocomplete-field:focus, .date-field:focus {
  border-color: #ff2770;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.transaction-dialog {
  border-radius: 10px;
  box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease-in-out;
  background: rgba(255, 255, 255, 1);
  border-left: 5px solid;
}

.success-dialog {
  border-color: #4caf50;
}

.error-dialog {
  border-color: #f44336;
}

.v-card-actions .green {
  color: #4caf50;
  transition: transform 0.3s ease;
}

.v-card-actions .green:hover {
  transform: translateY(-2px);
}

.v-btn:hover {
  transform: translateY(-2px);
}

.v-card-title {
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}
</style>


<script lang="ts">
import { defineComponent, ref, onMounted, watchEffect } from 'vue';
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
        citiesData.forEach(city => {
          // console.log("załadowane miasto: ", city);
          this.cities = citiesData;
        });
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
      // console.log("selectedCityFrom.value: ", this.selectedCityFrom);
      // console.log("selectedCityTo.value: ", this.selectedCityTo);

      if (this.selectedCityFrom && this.selectedCityTo && this.selectedDate) {
        const apiUrl = `/api/search_trains/?from=${encodeURIComponent(this.selectedCityFrom)}&to=${encodeURIComponent(this.selectedCityTo)}&date=${encodeURIComponent(this.selectedDate)}`;
        axios.get(apiUrl)
          .then(response => {
            const routesStore = useRoutesStore();
            if (response.data.schedules.length === 0) {
              this.noRoutesDialog = true;
            } else {
              routesStore.setSchedules(response.data.schedules);
              routesStore.setSelectedDepartureDate(this.selectedDate);
              // console.log("Zapisane trasy w store:", routesStore.schedules);
              this.$router.push('/routes');
            }
          })
          .catch(error => {
            console.error('Błąd podczas wyszukiwania połączeń:', error);
          });
      } else {
        console.log("Proszę wybrać miasta 'Skąd' i 'Dokąd' oraz datę");
      }
    },
    updateCanSearch() {
      this.canSearch = this.selectedCityFrom !== null && this.selectedCityTo !== null && this.selectedDate !== '';
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
  },
  mounted() {
    this.loadCities();
    watchEffect(() => {
      this.updateCanSearch();
    });
    this.checkTransactionStatus();
  },
});
</script>