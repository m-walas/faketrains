<template>
    <v-container fill-height fluid>
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

.v-container.fill-height {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 2vw;
}

.routes-container {
  flex-grow: 1;
}

.route-info {
  text-align: center;
  margin-bottom: 2vw;
  margin-top: 5vw;
  color: #ff2770;
}

@media (min-aspect-ratio: 21/9) {
  .route-info {
    font-size: 1.8vw;
  }
}

.carousel-container {
  overflow: hidden;
  width: 100%; 
  margin: 0 auto;
}

.carousel-wrapper {
  width: 100%;
  margin-left: 0;
}

.carousel {
  display: flex;
  /* justify-content: flex-start; */
  transition: transform 0.5s ease-in-out;
}

.carousel-item {
  /* flex: 0 0 300px; */
  flex-shrink: 0;
  width: 90vw;
  max-width: 300px;
  opacity: 0.5;
  transition: transform 0.5s ease, opacity 0.3s ease;
  margin: 0 1vw;
}

.carousel-item.active {
  opacity: 1;
  transform: scale(1.1);
}

.carousel-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 10;
}

.carousel-button.left {
  left: 1vw;
}

.carousel-button.right {
  right: 1vw;
}

.route-card {
  max-width: 90vw;
  min-height: 400px;
  text-align: left;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  margin-top: 2vw;
}

.route-card:hover {
  transform: scale(1.03);
  box-shadow: 0 6px 12px 0 rgba(0,0,0,0.3);
}

.v-btn:hover {
  background-color: #ff2770;
  color: white;
}

@media only screen and (max-width: 600px) {
.carousel-item {
  width: 90vw;
  max-width: 300px;
}
}

.details-panel {
  padding: 2vw;
  background-color: #f2f2f2;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 2vw;
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