<template>
  <div class="reg-page">
    <h1>注册</h1>
    <div class="reg-container">

      <form @submit.prevent="register">
        <div class="form-group">
          <input type="text" id="username" v-model="username" placeholder="用户名" ref="usernameInput">
          <input :type="showPassword1 ? 'text' : 'password'"  id="password" v-model="password" placeholder="密码">
          <img :src="showPassword1 ? eyeShow : eyeHidden" @click="togglePasswordVisibility1" alt="" id="eyeImage1">
          <input :type="showPassword2 ? 'text' : 'password'"  v-model="confirmPassword" placeholder="确认密码">
          <img :src="showPassword2 ? eyeShow : eyeHidden" @click="togglePasswordVisibility2" alt="" id="eyeImage2">
        </div>
        <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
        <button type="submit" id="reg">注册</button>
      </form>
      <a href="#" @click.prevent="login">已经有了账号？去登录</a>
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
      confirmPassword: '',
      errorMessage: '',
      showPassword1: true,
      showPassword2: false,
      eyeShow:require('../../public/images/eyeShow.png'),
      eyeHidden:require('../../public/images/eyeHidden.png')
    };
  },
  methods: {
    async register() {
      if (this.password !== this.confirmPassword) {
        this.errorMessage = '密码与确认密码不一致';
        this.username = '';
        this.password = '';
        this.confirmPassword = '';
        this.$refs.usernameInput.focus();
        return;
      }
      try {
        const response = await axios.post('/api/addUser', {
          userName: this.username,
          userPwd: this.password
        });
        if (response.data.code === 200 && response.data.message === '注册成功') {
          console.log('注册成功:', response.data.data[0]);
            this.errorMessage = '注册成功，请等待跳转到登录页面...';
            setTimeout(() => {
              this.$router.push('/login');
            }, 3000); // 等待1秒后跳转
        } else {
          console.log('注册失败:', response.data.message);
          this.errorMessage = response.data.message;
          this.username = '';
          this.password = '';
          this.confirmPassword = '';
          this.$refs.usernameInput.focus();
        }
      } catch (error) {
        console.error('注册失败:', error);
        this.errorMessage = '注册失败，请重试';
        this.username = '';
        this.password = '';
        this.confirmPassword = '';
        this.$refs.usernameInput.focus();
      }
    },
    login() {
      this.$router.push('/login');
    },
    togglePasswordVisibility1() {
      this.showPassword1 = !this.showPassword1;
    },
    togglePasswordVisibility2() {
      this.showPassword2 = !this.showPassword2;
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.reg-page {
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
  margin-top: 55px;
}

.reg-container {
  width: 555px;
  height: 452px;
  background-color: rgba(186, 205, 228, .7);
  border-radius: 31px;
  position: relative;
  padding-top: 20px;
}


.form-group input {
  width: 440px;
  height: 69px;
  background-color: #DFDCDA;
  opacity: 0.7;
  border: transparent;
  border-radius: 20px;
  font-size: 24px;
  padding-left: 17px;
  margin-top: 26px;
}

.form-group img {
  position: absolute;
  right: 75px;
  cursor: pointer;
}

#eyeImage1 {
  top: 158px;
}

#eyeImage2 {
  top: 252px;
}

.error-message {
  padding-top: 4px;
  color: red;
  font-size: 18px;
}

#reg {
  background-color: #B1C4D4;
  border-radius: 17px;
  width: 218px;
  height: 62px;
  border: transparent;
  color: white;
  box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
  /* 左下角阴影 */
  font-size: 24px;
  margin-top: 41px;
  opacity: 1;
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  bottom: 48px;

}

a {
  position: absolute;
  color: white;
  right: 29px;
  bottom: 15px;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

#reg:hover {
  background-color: #8AA4BE;
}
</style>