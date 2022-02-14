<template>
  <div class="container">
    <el-input
    v-model="textarea"
    :autosize="{ minRows: 2, maxRows: 6 }"
    type="textarea"
    placeholder="Something new..."
  >
  </el-input>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const textarea = ref('')
</script>