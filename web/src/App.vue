<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Nav from './components/Nav.vue'
</script>

<template>
  <el-container>
    <el-header class="header">
      <Nav></Nav>
    </el-header>
    <router-view></router-view>
  </el-container>
</template>

<style>
@import '@/assets/base.css';

body {
  background-color: var(--color-background-soft);
}

#app {
  max-width: 1080px;
  margin: 0 auto;

  font-weight: normal;
}

.header {
  background-color: var(--color-background);
}
</style>
