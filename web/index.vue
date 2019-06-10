<template>
  <v-slide></v-slide>
</template>

<script>
import Vue from "vue";
import Slide from "./slide.vue";

export default {
  name: "app",

  components: {
    "v-slide": Slide
  }
};
</script>

<style lang="less"></style>
