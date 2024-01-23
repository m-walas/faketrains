<template>
  <v-container fluid class="main-container">
    <v-row>
      <v-col cols="12" class="image-col">
        <v-img src="../assets/tlo.jpg" class="full-width"></v-img>

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
            <v-btn color="primary" :disabled="!canSearch" @click="search">Szukaj</v-btn>
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
        <v-btn color="primary" text @click="noRoutesDialog = false">OK</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<style scoped>
.main-container {
  min-height: 100vh;
}

.full-width {
  width: 100%;
}

.image-col {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  position: relative;
}

.form-card {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.9);
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
  border: 1px solid #ccc;
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
  border-color: #3d73da;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.v-autocomplete-field:focus-within .v-label, .v-text-field:focus-within .v-label {
  transform: translateX(10px);
}

.v-btn {
  color: white;
  padding: 10px 20px;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.v-btn:hover {
  background-color: #3d73da;
  transform: scale(1.05);
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
  },
  mounted() {
    this.loadCities();
    watchEffect(() => {
      this.updateCanSearch();
    });
  },
});
</script>