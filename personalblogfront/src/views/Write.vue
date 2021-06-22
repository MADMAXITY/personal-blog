<template>
    <div class="wrapper">
        <Navbar />
        <div class="mainpage">
            <textarea
                class="text"
                placeholder="Write your thing..."
                cols="70"
                rows="15"
                v-model="text"
            >
Some text is here okay</textarea
            >
            <div class="submission">
                <input
                    placeholder="Title"
                    type="text"
                    class="title"
                    v-model="title"
                />
                <button class="button" @click="submit">Submit</button>
            </div>
        </div>
        <Footer />
    </div>
</template>
<script>
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import axios from "axios";
export default {
    name: "Write",
    data() {
        return {
            title: "",
            text: "",
        };
    },
    components: {
        Navbar,
        Footer,
    },
    methods: {
        async submit() {
            this.form = new FormData();
            this.form.append("title", this.title);
            this.form.append("text", this.text);

            await axios.post("postdata/", this.form).then((response) => {
                if (response["data"]["status"] == "success") {
                    alert("Success!");
                }
            });
        },
    },
};
</script>
<style scoped>
.mainpage {
    height: 50vh;
    /* width: 50%; */
    margin-top: 5rem;
    display: flex;
    align-items: center;
    flex-direction: column;
}
.submission {
    display: flex;
    justify-content: space-around;
    align-items: center;
}
textarea {
    padding: 0.7rem 0.7rem;
    font-family: "Balsamiq Sans";
    font-size: 1.2rem;
    background-color: rgba(249, 248, 244, 0.7);
    border: 2px solid rgb(249, 248, 244, 1);
    outline: none;
}
.title {
    margin: 1rem;
    padding: 0.5rem 0.7rem;
    width: 60%;
    font-family: "Montserrat";
    font-size: 1.4rem;
    border-radius: 0.7rem;
    outline: none;
    border: 2px solid rgb(249, 248, 244, 1);
}
button {
    padding: 0.5rem 0.7rem;
    font-family: "Montserrat";
    font-size: 1.4rem;
    border-radius: 0.7rem;
    outline: none;
    border: 2px solid rgb(249, 248, 244, 1);
}
button:hover {
    border: 2px solid rgb(249, 248, 244, 0.5);
}
</style>
