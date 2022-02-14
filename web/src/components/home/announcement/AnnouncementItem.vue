<template>
  <div class="announcement-item">
    {{ text }}
  </div>
</template>

<script setup>
defineProps(['text'])
</script>

<style>
  .announcement-item {
    padding: 1.5rem;
  }
</style>