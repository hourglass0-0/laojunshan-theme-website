<template>
  <div class="scenic-page">
    <div class="nav-container">
      <div class="background-image"></div>
      <div class="nav-box">
        <div class="nav-line"></div>
        <div class="nav-items">
          <div
            v-for="item in navItems"
            :key="item.text"
            :class="['nav-item', { active: activeNav === item.path }]"
            @click="selectNav(item.path)"
          >
            <span>{{ item.text }}</span>
            <img v-if="activeNav === item.path" :src="item.icon" class="nav-icon" />
          </div>
        </div>
      </div>
    </div>
    
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeNav: this.$route.path, // 设置初始值为当前路由的完整路径
      navItems: [
        { text: '简介', path: '/scenic/introduction', icon: require('@/assets/icons/active.png') },
        { text: '发展历史', path: '/scenic/history', icon: require('@/assets/icons/active.png') },
        { text: '地理环境', path: '/scenic/environment', icon: require('@/assets/icons/active.png') },
        { text: '主要景点', path: '/scenic/scenic-spots', icon: require('@/assets/icons/active.png') },
        { text: '自然资源', path: '/scenic/resources', icon: require('@/assets/icons/active.png') },
        { text: '景点荣誉', path: '/scenic/honors', icon: require('@/assets/icons/active.png') },
        { text: '历史文化', path: '/scenic/culture', icon: require('@/assets/icons/active.png') },
      ],
    };
  },
  methods: {
    selectNav(navPath) {
      this.activeNav = navPath;
      this.$router.push(navPath);
    },
  },
  mounted() {
    // Set the initial activeNav based on the current route
    this.activeNav = this.$route.path;
  },
  watch: {
    $route(to) {
      this.activeNav = to.path;
    },
  },
};
</script>

<style scoped>
.scenic-page {
  width: 1170px;
  position: relative;
  margin: 0 auto;
}

.background-image {
  background-image: url('../../public/images/bg.png'); /* Update with your image path */
  background-size: cover;
  background-position: center;
  height: 300px; /* Adjust height as needed */
  position: relative;
}

.nav-container {
  position: relative;
}

.nav-box {
  position: absolute;
  bottom: 20px; /* Adjust as needed */
  left: 50%;
  transform: translateX(-50%);
  width: 80%;
  background: rgba(255, 255, 255, 0.8);
  padding: 10px;
  border-radius: 10px;
}

.nav-line {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  background: #ccc;
}

.nav-items {
  display: flex;
  justify-content: space-around;
}

.nav-item {
  position: relative;
  cursor: pointer;
  padding: 5px 10px;
  transition: color 0.3s;
}

span {
  font-size: 18px;
}

.nav-icon {
  position: absolute;
  top: -65px; 
  left: 50%;
  transform: translateX(-50%);
  width: 50px; 
  height: auto;
}
</style>
