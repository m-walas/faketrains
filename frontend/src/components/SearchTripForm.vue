<template>
  <v-form>
    <v-autocomplete
      :items="citiesFrom"
      label="Skąd"
      v-model="selectedCityFrom"
      @input="fetchCitiesFrom"
    ></v-autocomplete>
    <v-autocomplete
      :items="citiesTo"
      label="Dokąd"
      v-model="selectedCityTo"
      @input="fetchCitiesTo"
    ></v-autocomplete>
    <v-text-field type="date" label="Data"></v-text-field>
    <v-btn @click="search">Zatwierdź</v-btn>
  </v-form>
</template>

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
