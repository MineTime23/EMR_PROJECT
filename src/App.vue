<template>
  <div id="app">
    <side-bar></side-bar> <!-- Include the sidebar component here -->
    <main-content></main-content> <!-- Include the main-content component here -->
  </div>
</template>

<script>
import Sidebar from "./components/side-bar.vue";
import MainContent from "./components/main-content.vue";
// import PatientsInput from "./components/patients-input.vue";

export default {
  components: {
    'side-bar': Sidebar,
    'main-content': MainContent,
    // 'patients-input': PatientsInput,
  }
};
</script>

<style>
/* Add global styles here */
body {
  margin: 0;
  padding: 0;
  display: flex;
}

#app {
  display: flex;
}
</style>
