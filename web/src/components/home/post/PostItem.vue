<script setup>
import { ref, onMounted } from 'vue';
const medias = ref([
  "https://images.unsplash.com/photo-1645192598815-df5a445ba803?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80",
  'https://images.unsplash.com/photo-1645222509499-fb2c51f977da?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80',
  'https://images.unsplash.com/photo-1645359271414-3697b7a5781f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1214&q=80',
  'https://images.unsplash.com/photo-1645355291078-b426f0b17e51?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1171&q=80',
  'https://images.unsplash.com/photo-1645111094688-b6a2184a56b3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80'
]);

defineProps({
  id: Number,
  avatar: {
    type: String,
    default: 'https://somewhere.com/default.png'
  },
  author: {
    type: String,
    default: 'Anonymous'
  },
  text: String,
  datetime: {
    type: String,
    default: 'Just now'
  }
})

onMounted(() => {
  console.log('mounted');
  // let medias.value = api.queryMedia('...')   //  fake api call

})

</script>

<template>
  <div class="post-item">

    <div class="user-info">
      <img src="@/assets/default.png" class="avatar">
      <div class="info-container">
        <div class="author">{{ author }}</div>
        <div class="datetime">{{ datetime }}</div>
      </div>
    </div>

    <div class="post-content">
      <div class="text">{{ text }}</div>
    </div>

    <div class="post-media">
      <img class="post-media-item" v-for="media in medias" :key="media.id" :src="media" />
    </div>

  </div>
</template>

<style lang="scss">
.post-item {
  padding: 1.3rem;

  border-radius: 4px;
  border: 1px solid var(--color-border);
  background-color: var(--color-background);
  margin: 0.8rem 0;
}

.avatar {
  width: 45px;
  width: 45px;
  border-radius: 50%;
  margin-right: 10px;
}

.user-info {
  display: flex;
}

.info-container {
  display: flex;
  flex-direction: column;
  height: 3rem;
  justify-content: center;
}

.author {
  font-weight: bold;
  line-height: 1rem;
}

.datetime {
  line-height: 1rem;
  color: rgb(151, 151, 151);
}

.post-content {
  padding-left: 55px;
}

.post-media {
  padding-top: 0.5rem;
  padding-left: 55px;
}

.post-media-item {
  display: inline-block;
  width: 200px;
  height: 200px;
  object-fit: cover;

  &:only-child {
    width: 240px;
    height: 240px;
    border-radius: 8px;
  }
  &:nth-child(3n + 1):nth-last-child(2),
  &:nth-child(3n + 2):last-child {
    width: 303px;
    height: 303px;
  }
  &:nth-child(3n + 2) {
    margin: 0 6px;
  }
  &:first-child {
    border-top-left-radius: 6px;
  }
  &:last-child {
    margin-right: 0;
    border-bottom-right-radius: 6px;
  }
  &:nth-child(3n + 1) {
    &:last-child,
    &:nth-last-child(2),
    &:nth-last-child(3) {
      border-bottom-left-radius: 6px;
    }
  }
  &:nth-child(2):last-child,
  &:nth-child(3) {
    border-top-right-radius: 6px;
  }
  &:nth-child(2):nth-last-child(3) {
    margin-right: 220px;
  }
  &:nth-child(2):nth-last-child(3) {
    border-top-right-radius: 6px;
  }
  &:nth-child(3):nth-last-child(2) {
    margin-top: 6px;
    margin-right: 6px;
    border-radius: 0 0 0 6px;
  }
  &:nth-child(4):last-child {
    border-radius: 0 0 6px 0;
  }
}
</style>