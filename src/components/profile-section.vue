<template>
  <div class="profile-block">
    <img src="../assets/profile.png" alt="Profile Image" class="profile-image" />
    <div class="profile-info">
      <h2>{{ username }}</h2>
      <p>{{ role }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    username: String,
    role: String,
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
.profile-block {
  display: flex;
  align-items: center;
  font-size: 14px;
  line-height: 8px;
  padding: 20px;
}

.profile-image {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  margin-right: 16px;
}
</style>
