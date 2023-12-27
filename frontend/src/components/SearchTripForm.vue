<template>
  <v-container fluid class="main-container">
    <v-row>
      <!-- Zdjęcie na środku strony -->
      <v-col cols="12" class="image-col">
        <v-img src="../assets/tlo.jpg" class="full-height"></v-img>

        <!-- Formularz na zdjęciu -->
        <v-card class="form-card" >
          <!-- Sekcja "Trasa" -->
          <v-card-title class="headline font-weight-bold mb-2">Znajdź Połączenie</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-autocomplete
              :items="citiesFrom"
              label="Skąd"
              v-model="selectedCityFrom"
              @input="fetchCitiesFrom"
              :loading="isLoadingFrom"
            ></v-autocomplete>
            <v-autocomplete
              :items="citiesTo"
              label="Dokąd"
              v-model="selectedCityTo"
              @input="fetchCitiesTo"
              :loading="isLoadingTo"
            ></v-autocomplete>
          </v-card-text>

          <!-- Sekcja "Data" -->
          <v-divider></v-divider>
          <v-card-text>
            <v-text-field type="date" label="Data"></v-text-field>
          </v-card-text>

          <!-- Przycisk do rozpoczęcia wyszukiwania -->
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="primary" @click="search">Zatwierdź</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
.main-container {
  min-height: 100vh;
}

.full-height {
  height: 100%;
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
  top: 15%;
  left: 5%;
  height: 80%;
  width: 20%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: rgba(255, 255, 255, 0.7); 
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-card {
  width: 100%;
  padding: 24px;
}
</style>


<script>
import axios from 'axios';
import debounce from 'lodash/debounce';

export default {
  data() {
    return {
      citiesFrom: [],
      citiesTo: [],
      selectedCityFrom: '',
      selectedCityTo: '',
      isLoadingFrom: false,
      isLoadingTo: false,
    };
  },
  created() {
    this.debouncedFetchCitiesFrom = debounce(this.fetchCitiesFrom, 500);
    this.debouncedFetchCitiesTo = debounce(this.fetchCitiesTo, 500);
  },
  watch: {
    selectedCityFrom(newVal) {
      this.debouncedFetchCitiesFrom(newVal);
    },
    selectedCityTo(newVal) {
      this.debouncedFetchCitiesTo(newVal);
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
      console.log("Wyszukiwanie połączeń z", this.selectedCityFrom, "do", this.selectedCityTo);
      // Tutaj możesz dodać logikę wyszukiwania połączeń
    },
  },
};
</script>
