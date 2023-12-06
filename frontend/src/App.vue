<template>
<v-app>
  <v-app-bar>
    <v-app-bar-title>
      <Header></Header>
    </v-app-bar-title> 

    <HeaderButtons></HeaderButtons>
    
  
  </v-app-bar>
  <v-main>
    <router-view />
  </v-main>
</v-app>
</template>

<script lang="ts">
import Header from "./components/Header.vue";
import HeaderButtons from "./components/HeaderButtons.vue";

export default {
  name: "App",
  components: {
    Header,
    HeaderButtons
  }
}

</script>
