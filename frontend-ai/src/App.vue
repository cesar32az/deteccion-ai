<template>
  <v-app>
    <v-app-bar app color="indigo" dark>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          :src="img"
          transition="scale-transition"
          width="40"
        />
      </div>
      <v-toolbar-title>Proyecto Inteligencia Artificial</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    img: "https://www.pinclipart.com/picdir/big/520-5208843_brain-learning-png-clipart-artificial-intelligence-logo-png.png"
  }),
  mounted() {
    this.$vuetify.theme.dark = true;
  },
};
</script>
