<template>
    <div id="culture" ref="sections">
      <h2>历史文化</h2>
      
      <div v-for="historicalCulture in historicalCultures" :key="historicalCulture.id">
        <div class="culture-section">
          <h4 v-if="historicalCulture.title">{{ historicalCulture.title }}</h4>
          <p v-html="historicalCulture.content"></p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        historicalCultures: [],
      }
    },
    methods: {
      fetchHistoricalCultures() {
        axios.get('/api/historicalCulture')
          .then(response => {
            this.historicalCultures = response.data.data;
            console.log(this.historicalCultures);
            console.log(response.data.data);
          })
          .catch(error => {
            console.error("获取历史文化时出错！", error);
          });
      },
    },
    mounted() {
      this.fetchHistoricalCultures();
    }
  }
  </script>
  
  <style scoped>
  #culture {
    padding: 20px;
    max-width: 1150px;
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
  
  .culture-section {
    margin-bottom: 20px;
  }
  
  h4 {
    font-size: 1.3em;
    color: #3498db;
    margin-bottom: 10px;
  }
  
  p {
    font-size: 1.1em;
    color: #34495e;
    line-height: 1.6;
    text-indent: 2em;
  }
  </style>
  