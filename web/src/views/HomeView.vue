<script setup>
import PostInput from '../components/home/post/PostInput.vue'
import PostItem from '../components/home/post/PostItem.vue'
import AnnouncementItem from '../components/home/announcement/AnnouncementItem.vue'

</script>

<template>
  <div class="home">

    <div class="post-container">
      <div class="box-common">
        <PostInput></PostInput>
      </div>
      <div class="post-listn">
        <PostItem text="Welcome to CUForum" author="TaurusXin"></PostItem>
        <PostItem text="你好， 世界" author="Alice"></PostItem>
        <PostItem text="Hello world" author="Bob"></PostItem>
        <PostItem text="test post 4" author="Charlie"></PostItem>
        <PostItem text="test post 5" author="Ed Sheeran"></PostItem>
      </div>
    </div>

    <div class="announcement-container">
      <div class="announcement-list box-common">
        <AnnouncementItem text="test announcement 1"></AnnouncementItem>
        <AnnouncementItem text="test announcement 2"></AnnouncementItem>
        <AnnouncementItem text="test announcement 3"></AnnouncementItem>
        <AnnouncementItem text="test announcement 4"></AnnouncementItem>
      </div>
    </div>

  </div>
</template>

<style scoped>

.home {
  display: flex;
  flex-direction: row;
  background-color: var(--color-background-soft);
  margin-top: 0.7rem;
}

.box-common {
  border-radius: 4px;
  border: 1px solid var(--color-border);
  background-color: var(--color-background);
}

.post-container {
  width: 70%;
}

.post-list {
  margin-top: 0.8rem;
}

.announcement-container {
  margin-left: 25px;
  width: 30%;
}
</style>