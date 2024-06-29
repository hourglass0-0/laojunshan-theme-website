<template>
    <div id="history">
        <div class="content-container">
            <div v-for="history in histories" :key="history.id" class="history-item fade-in">
                <h3 v-if="history.title">{{ history.title }}</h3>
                <p v-html="history.content"></p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            histories: [],
        }
    },
    methods: {
        fetchHistories() {
            axios.get('/api/history')
                .then(response => {
                    this.histories = response.data.data; 
                })
                .catch(error => {
                    console.error("获取历史时出错！", error);
                });
        },
    },
    mounted() {
        this.fetchHistories();
    }
}
</script>

<style scoped>
#history {
    width: 100%;
    margin: 20px auto;
    padding: 30px;
    background-color: #f9f9fb;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    overflow: hidden;
}

.content-container {
    display: flex;
    flex-direction: column;
    gap: 25px;
}

.history-item {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 1s ease-in-out forwards;
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* 添加过渡效果 */
}

.history-item:hover {
    transform: translateY(-10px); /* 悬停时向上移动 */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* 添加阴影效果 */
}

.history-item h3 {
    font-size: 26px;
    margin-bottom: 15px;
    color: #2c3e50;
}

.history-item p {
    font-size: 18px;
    line-height: 1.8;
    color: #34495e;
}

@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(30px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

.fade-in {
    animation-delay: calc(var(--order) * 0.2s);
}
</style>
