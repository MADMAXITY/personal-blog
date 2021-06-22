<template>
    <Navbar />
    <div class="home">
        <div
            class="single-post"
            v-for="(post, postindex) in data"
            v-bind:key="postindex"
        >
            <div class="post-title">{{ post.Title }}</div>
            <div class="post-content">{{ post.Content }}</div>
        </div>
    </div>
    <Footer />
</template>

<script>
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import axios from "axios";
export default {
    name: "Home",
    data() {
        return {
            data: {},
        };
    },
    components: {
        Navbar,
        Footer,
    },
    async mounted() {
        await axios.post("getdata/").then((response) => {
            this.data = response["data"]["data"];
        });
    },
};
</script>
<style scoped>
.home {
    min-height: 65vh;
    text-align: center;
}

.single-post {
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
    border-top: 3px solid rgb(249, 248, 244);
    padding: 2rem;
}
.post-title {
    font-family: "Montserrat";
    font-weight: 500;
    font-size: 2rem;
}
.post-content {
    width: 70%;
    font-family: "Montserrat";
    font-weight: 400;
    font-size: 1.3rem;
    line-height: 1.6rem;
}
</style>
