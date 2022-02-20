<script setup>
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
  },
  media: String
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
  </div>
</template>

<style>

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
</style>