<template>
    <v-container>
        <div class="route-info" v-if="schedules.length > 0">
        <h2>{{ schedules[0].departure_city }} - {{ schedules[0].arrival_city }}</h2>
        </div>

        <div class="carousel-container" v-if="schedules.length > 0">
        <v-btn icon class="carousel-button left" @click="prevCarouselItem" v-if="activeIndex > 0">
            <v-icon>mdi-chevron-left</v-icon>
        </v-btn>

        <div class="carousel-wrapper">
            <div class="carousel" :style="carouselStyle">
            <div v-for="(route, index) in schedules" :key="index" class="carousel-item" :class="{ active: index === activeIndex }">
                <v-card class="route-card" @click="toggleDetails(index)">
                <v-card-text>
                    <RouteDisplay :route="route"></RouteDisplay>
                </v-card-text>
                </v-card>
            </div>
            </div>
        </div>

        <v-btn icon class="carousel-button right" @click="nextCarouselItem" v-if="activeIndex != (schedules.length - 1)">
            <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
        </div>

        <div v-if="detailsIndex >= 0" class="details-panel" :id="`details-${detailsIndex}`">
        <RouteDetails :route="schedules[detailsIndex]"></RouteDetails>
        </div>
    </v-container>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
}

.route-info {
  text-align: center;
  margin-bottom: 20px;
  margin-top: 50px;
}

.carousel-container {
  overflow: hidden;
  width: 640px; 
  margin: 0 auto;
}

.carousel-wrapper {
  width: 300px; 
  margin-left: 170px; 
}

.carousel {
  display: flex;
  justify-content: flex-start;
  transition: transform 0.5s ease-in-out;
}

.carousel-item {
  flex: 0 0 300px;
  opacity: 0.5;
  transition: transform 0.5s ease, opacity 0.3s ease;
  margin: 0 10px;
}

.carousel-item.active {
  opacity: 1;
  transform: scale(1.1);
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.carousel-button.left {
  left: 10px;
}

.carousel-button.right {
  right: 10px;
}

.route-card {
  max-width: 300px;
  min-height: 400px;
  text-align: left;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  margin-top: 20px;
}

.route-card:hover {
  transform: scale(1.03);
  box-shadow: 0 6px 12px 0 rgba(0,0,0,0.3);
}

.v-btn:hover {
  background-color: #0056b3;
  color: white;
}

@media only screen and (max-width: 600px) {
.carousel-wrapper {
  width: 100%;
}

.carousel-item {
  width: 100%;
}
}

.details-panel {
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
} 
</style>

<script>
import RouteDisplay from './RouteDisplay.vue';
import RouteDetails from './RouteDetails.vue';
import { useRoutesStore } from '../store/routes';

export default {
    components: {
        RouteDisplay,
        RouteDetails,
    },
    data() {
        return {
        routesStore: useRoutesStore(),
        activeIndex: 0,
        detailsIndex: -1,
        };
    },
    mounted() {
        // console.log(this.schedules);
    },
    computed: {
        schedules() {
        return this.routesStore.schedules;
        },
        carouselStyle() {
        const offset = this.activeIndex * 320;
        return { transform: `translateX(${-offset}px)` };
        },
    },
    methods: {
        toggleDetails(index) {
        this.detailsIndex = this.detailsIndex === index ? -1 : index;
        },
        nextCarouselItem() {
        if (this.activeIndex < (this.schedules.length - 1)) {
            this.activeIndex++;
        }
        },
        prevCarouselItem() {
        if (this.activeIndex > 0) {
            this.activeIndex--;
        }
        },
    },
};
</script>