<template>
  <v-container class="d-flex flex-column align-center justify-center">
    <Train></Train>
  </v-container>
</template>

  
<script lang="ts">
import SearchForm from '../components/SearchTripForm.vue';
import Train from '@/components/Train.vue';

export default {
  components: {
    SearchForm,
    Train,
  },
};
</script>