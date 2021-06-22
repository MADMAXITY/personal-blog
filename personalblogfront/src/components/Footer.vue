<template>
    <div class="footer">
        <div class="footer-greet">Thank you for reading!</div>
        <div class="note">
            Thank you if you have read the posts, it makes a difference. If you
            want to write something and have a page of your name, let me know, I
            will do my best to disappoint you. As I said, this is MY place. Have
            a good one
        </div>
    </div>
</template>

<script>
export default {
    name: "Footer",
};
</script>
<style scoped>
.footer {
    padding: 4rem 12rem;
    background-color: rgb(0, 0, 0);
}
.footer-greet {
    font-family: "Montserrat";
    margin-bottom: 0.4rem;
    font-weight: 500;
    font-size: 1.4rem;
    color: rgb(255, 255, 255);
}
.note {
    width: 60%;
    font-family: "Montserrat";
    font-weight: 400;
    font-size: 1rem;
    line-height: 1.4rem;
    color: rgb(146, 146, 146);
}
</style>
