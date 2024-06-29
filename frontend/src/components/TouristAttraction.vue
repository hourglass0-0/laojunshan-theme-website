<template>
  <div id="honors" ref="sections">
    <h2>景点荣誉</h2>
    <div class="honors-container">
      <div v-for="touristAttraction in touristAttractions" :key="touristAttraction.id" class="honors-card">
        <div class="honors-icon">
          <i class="fa fa-trophy"></i>
        </div>
        <div class="honors-content">
          <h3>{{ touristAttraction.title }}</h3>
          <p v-html="touristAttraction.content"></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      touristAttractions: [],
    }
  },
  methods: {
    fetchTouristAttractions() {
      axios.get('/api/touristAttraction')
        .then(response => {
          this.touristAttractions = response.data.data;
        })
        .catch(error => {
          console.error("获取景点荣誉时出错！", error);
        });
    },
  },
  mounted() {
    this.fetchTouristAttractions();
  }
}
</script>

<style scoped>
#honors {
  padding: 20px;
  max-width: 1170px;
  margin: 0 auto;
  font-family: Arial, sans-serif;
}

h2 {
  font-size: 2em;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 20px;
  border-bottom: 2px solid #2980b9;
  padding-bottom: 10px;
}

.honors-container {
  display: flex;
  flex-wrap: wrap;
}

.honors-card {
  background-color: #ecf0f1;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  margin: 10px;
  width: calc(33.33% - 20px); /* 3 cards in a row */
  padding: 20px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.honors-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0,0,0,0.2);
}

.honors-icon {
  font-size: 24px;
  color: #f39c12;
  margin-bottom: 10px;
  text-align: center;
}

.honors-content h3 {
  font-size: 1.5em;
  color: #3498db;
  margin-bottom: 10px;
}

.honors-content p {
  font-size: 1.1em;
  color: #34495e;
}
</style>
