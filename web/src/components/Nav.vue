<script setup>

</script>

<template>
  <div class="nav-bar">
    <img alt="CUForum logo" class="logo" src="@/assets/logo.svg"/>

    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/notification">Notification</RouterLink>
      <RouterLink to="/profile">Profile</RouterLink>
    </nav>

  </div>
</template>

<style>
@import '@/assets/base.css';

.nav-bar {
  height: 100%;
  width: 100%;
  padding: 1rem 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.logo {
  width: 100px;
  margin: auto 0;
  vertical-align: middle;
}

nav {
  font-size: 18px;
}

nav a.router-link-exact-active {
  color: var(--color-text);
  font-weight: bold;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
}

a {
  text-decoration: none;
  color: hsla(160, 100%, 37%, 1);
  transition: 0.15s;
}
</style>