<template>
  <main class="content">
    <h1>EMR System</h1>
    <div id="app">
      <input type="text" v-model="searchPatients" placeholder="Textbox 1">
      <input type="text" v-model="searchTreatments" placeholder="Textbox 2">
    </div>
  </main>
</template>

<script>
export default {
  methods: {
    submitForm() {
      console.log('Textbox 1 value: ' + this.searchPatients);
      console.log('Textbox 2 value: ' + this.searchTreatments);
    }
  }
}
</script>

<style scoped>
/* Add your component-specific styles here */
.content {
  flex: 1;
  padding: 24px;
  background: #f0f0f0;
  min-height: 100vh;
}

</style>
