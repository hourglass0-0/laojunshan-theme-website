<template>

  <div class="body">
    <div class="container" id="container">
      <div class="content">
        <div class="form">
          <div class="username">{{ username }}</div>
          <input type="text" v-model="title" placeholder="标题">
          <textarea v-model="message" placeholder="留言内容"></textarea>
          <button @click="postMessage">发表</button>
        </div>

        <div class="messages">
          <div class="message" v-for="msg in reversedMessages" :key="msg.id">
            <span class="title">{{ msg.title }}</span>
            <span class="time">{{ msg.date }}</span>
            <span class="author">{{ msg.author }}</span>
            <span class="message-body">{{ msg.content }}</span>
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
      username: localStorage.getItem('username') || '',
      title: '',
      message: '',
      messages: []
    };
  },
  created() {
    this.fetchMessages();
  },
  computed: {
      reversedMessages() {
        return this.messages.slice().reverse();
      }
  },
  methods: {
    async postMessage() {
      if (this.title && this.message) {
        try {
          const currentTime = new Date().toISOString(); // 获取当前时间
          const response = await axios.post('/api/postMessage', {
            userName: this.username,
            title: this.title,
            content: this.message,
            time: currentTime // 将当前时间作为time字段发送到后端
          });
          if (response.data.code === 200 && response.data.message === '发表成功') {
            console.log('留言成功:', response.data.data);
            this.clearForm();
            this.fetchMessages();
          } else {
            console.log('留言失败:', response.data.message);
            alert(response.data.message);
          }
        } catch (error) {
          console.error('留言失败:', error);
          if (error.response) {
            console.log('响应状态码:', error.response.status);
          }
          alert('留言失败，请重试');
        }
      } else {
        alert('请填写所有字段');
      }
    },

    fetchMessages() {
      axios.get('/api/getMessage')
        .then(response => {
          this.messages = [];
          response.data.forEach(msg => {
            this.messages.push({
              id: msg.message_id,
              author: msg.author,
              title: msg.title,
              content: msg.content,
              date: new Date(msg.timestamp).toLocaleString()
            });
          });
          console.log(this.messages);
        })
        .catch(error => {
          console.error("获取信息失败", error);
        });
    },

    clearForm() {
      this.title = '';
      this.message = '';
    }
  }
};
</script>

<style scoped>
.body {
  width: 100%;
  background-color: #B1C4D4;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form {
  width: 979px;
  height: 516px;
  border-radius: 16px;
  padding-top: 20px;
  background-color: rgba(37, 84, 136, 0.7);
  text-align: center;
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  margin-bottom: 14px;
}

.form input,
.form .username {
  width: 199px;
  height: 63px;
  border-radius: 32px;
  padding: 0 1em;
  border: 1px solid rgba(102, 111, 124, 1);
  background-color: rgba(37, 84, 136, 0.5);
  color: white;
  margin: 10px auto;
  font-size: 24px;
  outline: none;
  text-align: center;
  line-height: 63px;
}

.form input:focus,
.form textarea:focus,
.form button:hover {
  border: 1px solid white;
  /* 自定义focus时的边框样式 */
  outline: none;
  /* 确保focus时没有默认的outline */
  background-color: rgba(37, 84, 136, 1);
}


.form textarea {
  width: 498px;
  height: 293px;
  background-color: rgba(37, 84, 136, 0.35);
  border-radius: 16px;
  color: white;
  padding: 1em 1em;
  position: absolute;
  bottom: 24px;
  font-size: 20px;
  outline: none;
}

.form input::placeholder,
.form textarea::placeholder {
  color: rgba(255, 255, 255, .5);
}

.form button {
  width: 130px;
  height: 130px;
  background-color: rgba(37, 84, 136, 0.5);
  border-radius: 99px;
  border: 1px solid rgba(102, 111, 124, 1);
  color: white;
  position: relative;
  bottom: 0;
  right: 0;
  position: absolute;
  bottom: 24px;
  right: 44px;
  font-size: 28px;

}

#container {
  background-image: url('../../public/images/boardBg.png');
  background-size: cover;
  background-attachment: fixed;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.message {
  width: 860px;
  height: 158px;
  background-color: rgba(37, 84, 136, 0.5);
  border-radius: 16px;
  margin: 13px auto;
  padding: 1em 1em;
  color: white;
  position: relative;
  font-size: 24px;
}
.message:hover {
  transform: translateY(-2px);
}

.message .title {
  font-size: 32px;
  top: 1em;
  left: 1em;
}

.message .time {
  position: absolute;
  top: 1em;
  right: 1em;
}

.message .author {
  position: absolute;
  bottom: 0.5em;
  right: 1em;
  font-size:20px;
}

.message .message-body {
  position: absolute;
  bottom: 1em;
  left: 1em;
  font-size:22px;
  padding-right:1em;
}
</style>