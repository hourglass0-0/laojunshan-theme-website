<template>


  <div class="bodyContainer">
    <div class="body">
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <!-- Indicators -->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active"
            aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1"
            aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2"
            aria-label="Slide 3"></button>
        </div>

        <!-- Carousel items -->
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="/images/scroll1.jpg" class="d-block w-100" alt="First slide">
          </div>
          <div class="carousel-item">
            <img src="/images/scroll2.jpg" class="d-block w-100" alt="Second slide">
          </div>
          <div class="carousel-item">
            <img src="/images/scroll3.png" class="d-block w-100" alt="Third slide">
          </div>
        </div>

        <!-- Carousel controls -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
          data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
          data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>

      </div>

      <div class="intro">
        <h3>老君山（The Laojun Mountain）</h3>
        <h3>“天下无双圣境，世界第一仙山”</h3>
        <h3>是道教中历史最长的山脉。</h3>
      </div>

      <div class="images">
        <div class="box box1" @click="handleClick(0)">老子文化苑</div>
        <div class="box box2" @click="handleClick(1)">金顶道馆群</div>
        <div class="box box3" @click="handleClick(2)">龙吟听泉</div>
        <div class="box box4" @click="handleClick(3)">云海</div>
        <div class="box box5" @click="handleClick(4)">枫林醉秋</div>
        <div class="box box6" @click="handleClick(5)">舍身崖</div>
      </div>

    </div>
  </div>


</template>

<script>
export default {
  methods: {
    logout() {
      // 实现退出登录的逻辑
      this.$router.push('/')
    },
    handleClick(index) {
      this.$router.push({ path: '/scenic/scenic-spots', query: { index } });
    }
  },

}
</script>

<style scoped>

.bodyContainer {
  width: 100%;
  background-color: rgba(150, 166, 185, 1);
}

.body {
  width: 1170px;
  margin: 0 auto;
}

.body .intro {
  background-color: rgba(165, 179, 195, 1);
  text-align: center;
  padding-top: 48px;
  padding-bottom: 48px;
}

.body .intro h3 {
  font-weight: bold;
}

.images {
  display: flex;
}

.images .box {
  width: 195.41px;
  height: 304.03px;
  text-align: center;
  line-height: 304.03px;
  color: white;
  font-weight: bold;
  font-size: 26px;
  position: relative;
}

.box::before {
  content: "";
  position: absolute;
  /* 绝对定位 */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(211, 211, 211, 0);
  /* 初始时透明 */
  transition: background-color 0.3s ease;
  /* 添加过渡效果 */
}

.box:hover::before {
  background-color: rgba(0, 0, 0, 0.5);
  /* 鼠标悬停时显示浅灰色图层 */
}


.box1 {
  background-image: url('../../public/images/box1.png');
}

.box2 {
  background-image: url('../../public/images/box2.png');
}

.box3 {
  background-image: url('../../public/images/box3.png');
}

.box4 {
  background-image: url('../../public/images/box4.png');
}

.box5 {
  background-image: url('../../public/images/box5.png');
}

.box6 {
  background-image: url('../../public/images/box6.png');
}
</style>