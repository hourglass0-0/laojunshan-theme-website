<template>

    <div class="body">
        <div class="container">
            <h3>微信公众号</h3>
            <div class="contact1">
                <div class="contact1.1">
                    <img src="../../public/images/contact1_1.png" alt="">
                    <h3>老君山景区</h3>
                </div>
                <div class="contact1.2">
                    <img src="../../public/images/contact1_2.png" alt="">
                    <h3>老君山风景名胜区</h3>
                </div>
                <h3>官方电话：13248107239</h3>
            </div>

            <h3>抖音</h3>
            <div class="contact2">
                <div class="contact2.1">
                    <img src="../../public/images/contact2.1.1.png" alt="">
                    <img src="../../public/images/contact2.1.2.png" alt="">
                </div>
                <div class="contact2.2">
                    <img src="../../public/images/contact2.2.1.png" alt="">
                    <img src="../../public/images/contact2.2.2.png" alt="">
                </div>
                <div class="contact2.3">
                    <img src="../../public/images/contact2.3.1.png" alt="">
                    <img src="../../public/images/contact2.3.2.png" alt="">
                </div>
            </div>
        </div>
    </div>


</template>

<script>
</script>

<style scoped>

.body{
    background-color: #f0f3f5; /* 使用渐变色背景 */
    background-image: linear-gradient(to bottom, #f0f3f5, #B1C4D4);
    padding: 50px 0; /* 增加上下间距 */
}

.body .container{
    background-color: #fff;
    border-radius: 10px; /* 添加圆角边框 */
    padding: 30px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
}

.contact1{
    display:flex;
    text-align:center;
    margin-bottom: 30px; /* 增加下边距 */
}

.contact1 div{
    padding:0 27px;
}

.contact2{
    display:flex;
    justify-content: space-between;
}

.contact2 div{
    display:flex;
    align-items: flex-start;
}

h3{
    font-weight: bold;
    padding:20px 0;
}

/* 添加图片淡入动画效果 */
img {
    opacity: 0;
    animation: fadeIn 1s ease-in-out forwards;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
</style>
