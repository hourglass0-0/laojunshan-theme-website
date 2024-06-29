<template>
  <div>

    <div class="scenic-container">
      <div id="scenic-spots" ref="sections">
        <div v-for="mainAttraction in mainAttractions" :key="mainAttraction.id" class="attraction">
          <div v-if="!mainAttraction.img_url" class="attraction-info">
            <p v-html="mainAttraction.description" class="attraction-description"></p>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div v-for="(item, index) in items" :key="index" :class="{ 'item': true, 'active': activeIndex === index }"
        :style="{ 'background-image': 'url(' + item.img_url + ')' }" @click="setActive(index)">
        <div class="content">
          <div class="text">
            <div class="tit">{{ item.name }}</div>
            <div class="sub" v-show="activeIndex === index" v-html="item.description"></div>
          </div>
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
      mainAttractions: [],
      items: [],
      activeIndex: 2,
    };
  },
  methods: {
    fetchMainAttractions() {
      axios.get('/api/mainAttraction')
        .then(response => {
          this.mainAttractions = response.data.data;
          this.items = response.data.data.filter(item => item.img_url);
          console.log(this.items);
        })
        .catch(error => {
          console.error("获取主要景点时出错！", error);
        });
    },
    setActive(index) {
      this.activeIndex = index; // 修改 activeIndex 的值
      console.log('setActive被调用', index, this.activeIndex);
    },
  },

  mounted() {
    this.fetchMainAttractions();
    this.activeIndex = parseInt(this.$route.query.index) || 0;
  }
}
</script>

<style scoped>
.scenic-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.attraction {
  margin: 20px;
}

.attraction-info {
  text-align: center;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f8f8f8;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.attraction-info:hover {
  transform: scale(1.05);
}


.attraction-description {
  font-size: 18px;
  line-height: 1.5;
}


.container {
  /* 弹性布局 默认水平排列 */
  display: flex;
  width: 90%;
  max-width: 1170px;
  height: 400px;
  margin-bottom: 20px;
}

.item {
  /* 相对定位 */
  position: relative;
  width: 60px;
  margin: 10px;
  cursor: pointer;
  border-radius: 30px;
  /* 保持原有尺寸比例，裁切长边 */
  background-size: cover;
  /* 定位背景图像为正中间 */
  background-position: center;
  /* 过渡效果：时长 贝塞尔曲线 */
  transition: 0.5s cubic-bezier(0.05, 0.61, 0.41, 0.95);
}

.item .content {
  display: flex;
  position: absolute;
  right: 0;
  transition: 0.5s cubic-bezier(0.05, 0.61, 0.41, 0.95);
}

.item .content .text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: 0 5px;
  color: #fff;
  width: 100%;
}

.item .content .text div {
  opacity: 0;
  transition: opacity 0.5s ease-out;
}

.item .content .text .tit {
  background-color: rgba(0, 0, 0, 0.5);
  font-weight: bold;
  font-size: 24px;
}

.item .content .text .sub {
  background-color: rgba(0, 0, 0, 0.5);
  border-radius: 20px;
  /* 设置过渡效果延迟时间 */
  transition-delay: 0.1s;
  font-size: 18px;
}

/* 选中态样式 */
.item.active {
  flex: 1;
  margin: 0;
  border-radius: 40px;
}

.item.active .content {
  bottom: 4px;
}

.item.active .content .text div {
  opacity: 1;
}
</style>