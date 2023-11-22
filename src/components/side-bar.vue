<template>
  <aside class="sidebar" :class="{ closed: !sidebarOpen }">
    <!-- Sidebar content -->
    <ProfileBlock :username="username" :role="role" />
    <button @click="logout" class="logout-button">Logout</button>
    <ul>
      <li style="font-size: 24px"><p style="font-size: 16px">다음 환자</p>홍길동 님<p style="font-size: 16px">(23112345)</p></li>
      <li style="font-size: 18px">최길동 님<p style="font-size: 16px">(23112346)</p></li>
      <li style="font-size: 18px">정길동 님<p style="font-size: 16px">(23112347)</p></li>
    </ul>
  </aside>
</template>

<script>
import ProfileBlock from "./profile-section.vue";

export default {
  components: {
      ProfileBlock,
  },
  data() {
    return {
      sidebarOpen: true, 
      username: "박유상",
      role: "물리치료사",
    };
  },
  methods: {
    toggleSidebar() {
      this.sidebarOpen = !this.sidebarOpen;
    },
    logout() {
      // logout methods
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
.sidebar {
  background: #333;
  color: #fff;
  width: 216px;
  height: 100%;
  transition: transform 0.3s ease-in-out;
  transform: translateX(0); /* Change this to move the sidebar in or out */
}

.sidebar-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logout-button {
  width: 80px; /* Set the desired width */
  height: 32px; /* Set the desired height */
  align-items: center;
  margin-top: 10px; /* Add margin to separate the button from other elements */
  margin-left: 68px;
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar ul li {
  padding: 16px;
}

/* Style for unvisited links */
.sidebar ul li a {
  color: #fff; /* Text color for unvisited links */
  font-size: 20px;
  text-decoration: none; /* Remove underlines from links */
}

/* Style for visited links */
.sidebar ul li a:visited {
  color: #fff; /* Change this to the color for visited links */
  font-size: 20px;
}

.sidebar.closed {
  transform: translateX(-250px);
}
</style>
