<template>
  <div class="login-page">
    <h1>登录</h1>
    <div class="login-container">
      <form @submit.prevent="login">
        <div class="form-group">
          <input type="text" id="username" v-model="username" placeholder="用户名" ref="usernameInput">
          <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" placeholder="密码">
          <img :src="showPassword ? eyeShow : eyeHidden" @click="togglePasswordVisibility" alt="Toggle Password Visibility">
        </div>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <button type="submit" id="submit">登录</button>
      </form>
      <a href="#" @click.prevent="register">去注册</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      showPassword: false,
      errorMessage: '',
      eyeShow:require('../../public/images/eyeShow.png'),
      eyeHidden:require('../../public/images/eyeHidden.png')
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.get('/api/login', {
          params: {
            userName: this.username,
            userPwd: this.password
          }
        });

        if (response.data.code === 200 && response.data.message === '登录成功') {
          console.log('登录成功:', response.data.data[0]);
          localStorage.setItem('username', response.data.data[0].username);
          this.$router.push('/home');
        } else {
          console.log('登录失败:', response.data.message);
          this.errorMessage = '用户名或密码错误';
          this.username = '';
          this.password = '';
          this.$refs.usernameInput.focus();
        }
      } catch (error) {
        console.error('请求失败:', error);
        this.errorMessage = '登录失败，请重试';
        this.username = '';
        this.password = '';
        this.$refs.usernameInput.focus();
      }
    },
    register() {
      this.$router.push('/reg');
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.login-page {
  height: 100vh;
  background: url('../../public/images/bg.png') no-repeat center center;
  background-size: cover;
  margin: 0;
  text-align: center;
  display: flex;
  align-content: center;
  align-items: center;
  flex-direction: column;
}

h1 {
  color: #565252;
  margin: 20px auto;
  font-size: 64px;
  margin-top: 70px;
}

.login-container {
  width: 555px;
  height: 416px;
  background-color: rgba(186, 205, 228, 0.7);
  border-radius: 31px;
  position: relative;
}

.form-group input {
  width: 440px;
  height: 69px;
  background-color: rgba(223, 220, 218, 0.5);
  border: transparent;
  border-radius: 20px;
  font-size: 24px;
  padding-left: 17px;
  margin-top: 56px;
}

.form-group img {
  position: absolute;
  top: 197px;
  right: 75px;
  cursor: pointer;
}

.error-message {
  color: red;
  margin-top: 10px;
  font-size: 18px;
}

#submit {
  background-color: rgba(177, 196, 212, 1);
  border-radius: 17px;
  width: 218px;
  height: 62px;
  border: transparent;
  color: white;
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
  font-size: 24px;
  position:absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom:56px;
}

a {
  position: absolute;
  color: white;
  right: 29px;
  bottom: 28px;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

#submit:hover {
  background-color: rgba(138, 164, 190, 1);
}
</style>
