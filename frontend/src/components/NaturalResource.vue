<template>
    <div id="resources" ref="sections">
      <h2>自然资源</h2>
      <div v-for="naturalResource in naturalResources" :key="naturalResource.id" class="resource-card">
        <p v-html="naturalResource.content"></p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        naturalResources: [],
      }
    },
    methods: {
      fetchNaturalResources() {
        axios.get('/api/naturalResource')
          .then(response => {
            console.log(response.data.data)
            this.naturalResources = response.data.data; // 修改此行，直接使用 response.data
          })
          .catch(error => {
            console.error("获取自然资源时出错！", error);
          });
      },
    },
    mounted() {
      this.fetchNaturalResources();
    }
  }
  </script>
  
  <style scoped>
  #resources {
    padding: 20px;
    max-width: 1140px;
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
  
  .resource-card {
    background-color: #ecf0f1;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    padding: 20px;
    margin-bottom: 20px;
    transition: transform 0.3s, box-shadow 0.3s;
  }
  
  .resource-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
  }
  
  .resource-card p {
    font-size: 1.2em;
    line-height: 1.6;
    color: #34495e;
  }
  </style>
  