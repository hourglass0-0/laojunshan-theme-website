<template>
  <nav v-if="showNavAndFooter" class="navbar navbar-expand-lg">
    <div class="container">
      <router-link to="/" class="navbar-brand">老君山</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/home" class="nav-link">首页</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/scenic" class="nav-link">景点介绍</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/guide" class="nav-link">游客指南</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/board" class="nav-link">留言板</router-link>
          </li>
          <li class="nav-item">
            <router-link to="/contact" class="nav-link">联系我们</router-link>
          </li>
        </ul>
        <button class="btn" @click="logout">退出登录</button>
      </div>
    </div>
  </nav>

  <router-view />

  <footer v-if="showNavAndFooter" class="bg text-light text-center py-3 footer">
    © 老君山： 道法自然之旅
  </footer>

</template>

<script>
export default {
  computed: {
    showNavAndFooter() {
      return !['/login', '/reg', '/'].includes(this.$route.path);
    }
  },
  methods: {
    logout() {
      // 实现退出登录的逻辑
      localStorage.removeItem('username'); 
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
  font-family: 'KaiTi', 'STKaiti', '楷体', 'KaiTi_GB2312', sans-serif;
}

.navbar,
.bg {
  font-size:px;
  background-color: rgba(67, 91, 117, 1);
  color: rgba(255, 255, 255, 1);
}

.navbar-brand,
.nav-link,
.btn {
  color: rgba(255, 255, 255, 1);
  font-family: 'KaiTi', 'STKaiti', '楷体', 'KaiTi_GB2312', sans-serif;
}

.navbar-nav {
    --bs-nav-link-hover-color:  rgba(225, 197, 166, 1);

}


.btn {
  width: 90px;
  height: 35px;
  border: 1px solid rgba(255, 255, 255, 1);
}

.navbar-brand:hover,
.nav-link:hover,
.btn:hover {
  color: rgba(225, 197, 166, 1);
}

.btn:hover {
  border: 1px solid rgba(225, 197, 166, 1);
}

.router-link-active {
  color: rgba(225, 197, 166, 1);
}
</style>