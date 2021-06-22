<template>
    <div class="navbar">
        <div class="navbar-brand">SHANKAR JADHAV</div>
        <div class="navbar-about">About</div>
    </div>
</template>
<script>
export default {
    name: "Navbar",
};
</script>
<style scoped>
@media screen and (max-width: 480px) {
    .navbar {
        flex-direction: column;
    }
}
.navbar {
    background-color: rgb(249, 248, 244);
    display: flex;
    justify-content: space-between;
    padding: 2rem;
    align-items: center;
    margin-bottom: 5rem;
}
.navbar-brand {
    margin-left: 10%;
    font-family: "Montserrat";
    font-weight: 500;
    font-size: 1rem;
    transition: 0.1s linear;
    border-bottom: 2px solid;
    border-color: transparent;
}
.navbar-brand:hover {
    cursor: pointer;
    border-color: rgb(226, 221, 202);
}

.navbar-about {
    margin-right: 10%;
    font-family: "Montserrat";
    font-weight: 500;
    font-size: 1rem;
    transition: 0.1s linear;
    transition: 0.1s linear;
    border-bottom: 2px solid;
    border-color: transparent;
}
.navbar-about:hover {
    cursor: pointer;
    border-color: rgb(226, 221, 202);
}
</style>
