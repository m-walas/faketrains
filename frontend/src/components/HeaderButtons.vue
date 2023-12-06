<template>
    
    <v-btn icon @click="changeLightDark">
        <v-icon>mdi-theme-light-dark</v-icon>
    </v-btn>
    <v-btn icon @click="login">
      <v-icon>mdi-login</v-icon>
    </v-btn>
    <v-btn icon @click="logout">
      <v-icon>mdi-logout</v-icon>
    </v-btn>
   
       
</template>

<script lang="ts">

export default {
  data() {
    return {}
  },

  methods: {

  },
};
</script>