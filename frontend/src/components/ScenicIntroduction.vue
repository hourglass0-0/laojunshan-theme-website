<template>
    <div id="introduction">
        <div class="content-container">
            <div v-for="intro in introductions" :key="intro.id" class="intro-item fade-in">
                <div class="intro-content">
                    <h3 v-if="intro.title">{{ intro.title }}</h3>
                    <p v-html="intro.content"></p>
                </div>
            </div>
        </div>

        <div class="box-container">
            <div v-for="(item, index) in navItems" :key="index" class="box fade-in" @click="navigate(item.path)">
                <img :src="item.image" class="box-image" />
                <div class="box-text">{{ item.text }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            introductions: [],
            navItems: [
                { text: "发展历史", path: "/scenic/history", image: require("../../public/images/guide1.png") },
                { text: "地理环境", path: "/scenic/environment", image: require("../../public/images/guide2.png") },
                { text: "主要景点", path: "/scenic/scenic-spots", image: require("../../public/images/guide3.png") },
                { text: "自然资源", path: "/scenic/resources", image: require("../../public/images/guide4.png") },
                { text: "景点荣誉", path: "/scenic/honors", image: require("../../public/images/guide5.png") },
                { text: "历史文化", path: "/scenic/culture", image: require("../../public/images/guide6.png") },
            ],
        }
    },
    methods: {
        fetchIntroductions() {
            axios.get('/api/introduction')
                .then(response => {
                    this.introductions = response.data.data;
                })
                .catch(error => {
                    console.error("获取介绍时出错！", error);
                });
        },
        navigate(path) {
            this.$router.push(path);
        },
    },
    mounted() {
        this.fetchIntroductions();
    }
}
</script>

<style scoped>
#introduction {
  width: 100%;
  margin: 0 auto;
}

.content-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top:32px;
}

.intro-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border: 1px solid #ddd;
  border-radius: 10px;
  overflow: hidden;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}

.intro-item:hover {
  transform: translateY(-5px);
}

.intro-content {
  padding: 20px;
  flex: 1;
}

h3 {
  font-size: 24px;
  margin-bottom: 10px;
}

p {
  font-size: 18px;
  line-height: 1.5;
  color: #333;
}

.box-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-top: 40px;
}

.box {
  width: 30%;
  height: 240px;
  margin: 10px;
  border: 1px solid #ccc;
  border-radius: 10px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  transition: transform 0.3s ease-in-out, box-shadow 0.3s ease;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.box:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.15);
}

.box-image {
  width: 100%;
  height: 70%;
  object-fit: cover;
}

.box-text {
  height: 30%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  font-weight: bold;
  color: #333;
}

.fade-in {
  opacity: 0;
  animation: fadeIn 1s forwards;
  animation-delay: var(--fade-delay, 0s);
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}
</style>
