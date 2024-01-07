<template>
  <v-container fluid class="main-container">
    <v-row>
      <v-col cols="12" class="image-col">
        <v-img src="../assets/tlo.jpg" class="full-width"></v-img>

        <v-card class="form-card">
          <v-card-title class="headline font-weight-bold mb-2">Znajdź Połączenie</v-card-title>
          <v-divider></v-divider>

          <v-card-text>
            <v-autocomplete
              class="autocomplete-field"
              :items="citiesFrom"
              label="Skąd"
              v-model="selectedCityFrom"
              @input="fetchCitiesFrom"
              :loading="isLoadingFrom"
            ></v-autocomplete>
            <v-autocomplete
              class="autocomplete-field"
              :items="citiesTo"
              label="Dokąd"
              v-model="selectedCityTo"
              @input="fetchCitiesTo"
              :loading="isLoadingTo"
            ></v-autocomplete>
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
  background-color: rgba(255, 255, 255, 0.7);
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
  width: 100%;
  max-width: 300px;
  min-width: 250px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

.autocomplete-field:hover, .date-field:hover {
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.v-autocomplete .v-label, .v-text-field .v-label {
  transition: all 0.3s ease;
}

.v-autocomplete:focus-within .v-label, .v-text-field:focus-within .v-label {
  transform: translateX(10px);
}

.v-btn {
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.v-btn:hover {
  background-color: #4f8bf9;
  transform: scale(1.05);
}
</style>


<script lang="ts">
import { defineComponent } from 'vue';
import axios from 'axios';
import debounce from 'lodash/debounce';
import { useRoutesStore } from '../store/routes';

export default {
  data() {
    return {
      citiesFrom: [],
      citiesTo: [],
      selectedCityFrom: '',
      selectedCityTo: '',
      selectedDate: '',
      isLoadingFrom: false,
      isLoadingTo: false,
      canSearch: false,
      noRoutesDialog: false,
    };
  },
  created() {
    this.debouncedFetchCitiesFrom = debounce(this.fetchCitiesFrom, 500);
    this.debouncedFetchCitiesTo = debounce(this.fetchCitiesTo, 500);
  },
  watch: {
    selectedCityFrom(newVal) {
      this.debouncedFetchCitiesFrom(newVal);
      this.updateCanSearch();
    },
    selectedCityTo(newVal) {
      this.debouncedFetchCitiesTo(newVal);
      this.updateCanSearch();
    },
    selectedDate() {
      this.updateCanSearch();
    },
  },
  methods: {
    fetchCitiesFrom() {
      if (this.selectedCityFrom === null) {
        this.citiesFrom = [];
        return;
      }
      this.isLoadingFrom = true;
      axios.get(`/api/cities/?search=${this.selectedCityFrom}`)
        .then(response => {
          this.citiesFrom = response.data.map(city => city.name);
          this.isLoadingFrom = false;
        })
        .catch(error => {
          console.error('Błąd:', error);
          this.isLoadingFrom = false;
        });
    },
    fetchCitiesTo() {
      if (this.selectedCityTo === null) {
        this.citiesTo = [];
        return;
      }
      this.isLoadingTo = true;
      axios.get(`/api/cities/?search=${this.selectedCityTo}`)
        .then(response => {
          this.citiesTo = response.data.map(city => city.name);
          this.isLoadingTo = false;
        })
        .catch(error => {
          console.error('Błąd:', error);
          this.isLoadingTo = false;
        });
    },
    search() {
      if (this.selectedCityFrom && this.selectedCityTo && this.selectedDate) {
        const apiUrl = `/api/search_trains/?from=${encodeURIComponent(this.selectedCityFrom)}&to=${encodeURIComponent(this.selectedCityTo)}&date=${encodeURIComponent(this.selectedDate)}`;

        axios.get(apiUrl)
          .then(response => {
            const routesStore = useRoutesStore();
            if (response.data.schedules.length === 0) {
              this.noRoutesDialog = true;
            } else {
              routesStore.setSchedules(response.data.schedules);
              console.log("Zapisane trasy w store:", routesStore.schedules);
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
      this.canSearch = this.selectedCityFrom && this.selectedCityTo && this.selectedDate;
    },
  },
};
</script>
