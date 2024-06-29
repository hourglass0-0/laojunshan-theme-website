<template>
    <div>
        <div id="environment">
            <div v-for="environment in environments" :key="environment.id" class="environment-item fade-in">
                <h4 v-if="environment.title">{{ environment.title }}</h4>
                <p v-html="environment.content"></p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            environments: [],
        }
    },
    methods: {
        fetchEnvironments() {
            axios.get('/api/environment')
                .then(response => {
                    this.environments = response.data.data;
                })
                .catch(error => {
                    console.error("获取地理环境时出错！", error);
                });
        },
    },
    mounted() {
        this.fetchEnvironments();
    }
}
</script>

<style>
#environment {
    width: 100%;
    margin: 20px auto;
    padding: 20px;
    background-color: #fafafa;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.environment-item {
    background-color: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 0.6s ease-in-out forwards;
    transition: transform 0.3s ease, box-shadow 0.3s ease; /* 添加过渡效果 */
}

.environment-item:nth-child(odd) {
    background-color: #f0f8ff;
}

.environment-item:hover {
    transform: translateY(-10px); /* 悬停时向上移动 */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* 添加阴影效果 */
}

.environment-item h4 {
    font-size: 22px;
    margin-bottom: 10px;
    color: #2c3e50;
}

.environment-item p {
    font-size: 18px;
    line-height: 1.8;
    color: #34495e;
    margin: 0;
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
