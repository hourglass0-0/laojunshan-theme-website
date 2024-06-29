<template>
  <div class="bodyContainer">
    <div class="section" v-for="(guide, index) in guides" :key="guide.id" :class="{ 'first-section': index === 0 }">
      <div class="section-content" @mouseover="addHoverAnimation" @mouseleave="removeHoverAnimation">
        <div class="section-title">{{ guide.title }}</div>
        <div class="section-description" v-html="guide.content"></div>
        <img :src="guide.img_url" alt="Guide Image" class="section-image">
      </div>
    </div>
    <div class="footer">
      <p>此篇攻略已涵盖了老君山景区多方面信息</p>
      <p>总有一项是您需要的</p>
      <p>宝子们，拿走不谢</p>
      <p>❤️</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      guides: []
    };
  },
  created() {
    this.fetchGuides();
  },
  methods: {
    fetchGuides() {
      axios.get('/api/touristGuide')
        .then(response => {
          this.guides = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the guides!", error);
        });
    },
    addHoverAnimation(event) {
      event.currentTarget.classList.add('hover-animation');
    },
    removeHoverAnimation(event) {
      event.currentTarget.classList.remove('hover-animation');
    }
  }
};
</script>

<style scoped>

.bodyContainer {
  width: 100%;
  min-height: 100vh;
  background-color: #b1c4d4;
  font-family: 'Poppins', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.section {
  width: 100%;
  max-width: 1200px;
  margin-bottom: 40px;
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  animation: fadeInUp 0.5s ease forwards;
}

.first-section {
  margin-top: 20px;
}

.section-content {
  padding: 40px;
  text-align: center;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  color: #333;
  margin-bottom: 20px;
}

.section-description {
  font-size: 16px;
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
}

.section-image {
  max-width: 100%;
  border-radius: 10px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
}



.footer {
  width: 100%;
  background-color: #b1c4d4;
  padding: 30px 0;
  text-align: center;

}

.footer p {
  margin: 10px 0;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
