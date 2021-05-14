<template>
  <v-app>
    <v-navigation-drawer app clipped>
      <!-- -->
      <data-list></data-list>
    </v-navigation-drawer>
    <v-app-bar app color="primary" dark clipped-left>
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="xttps://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
      >
        <span class="mr-2">Latest Release</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
    
    <v-main>
      <!-- 用于路由展示 -->
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import DataList from "../components/DataList.vue";

export default {
  components: { DataList,},
  name: "App",

  data: () => ({
    //
  }),
};
</script>
