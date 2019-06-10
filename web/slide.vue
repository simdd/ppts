<template>
  <div class="row-center cover">
    <section class="column-center fw600" v-if="idx < 0">
      <p class="fs50">{{user.title}}</p>
      <p class="fs24 pt50">{{user.author}}</p>
      <p class="fs24 pt30">{{user.date}}</p>
    </section>
    <section class="slide" v-else>{{slide[idx]}}</section>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      idx: -1,
      user: {},
      slide: []
    };
  },

  methods: {
    getUser() {
      axios.get("http://127.0.0.1:7337/user").then(({ data }) => {
        this.user = data;
      });
    },

    getSlide() {
      axios.get("http://127.0.0.1:7337/page").then(({ data }) => {
        this.slide = data;
      });
    }
  },

  mounted() {
    this.getUser();
    this.getSlide();

    document.addEventListener("keydown", e => {
      if (e.keyCode === 32 || e.keyCode === 39) {
        if (this.idx >= this.slide.length - 1) {
          this.idx = -1;
        } else {
          this.idx = this.idx + 1;
        }
      }

      if (e.keyCode === 37) {
        if (this.idx === -1) {
          this.idx = -1;
        } else {
          this.idx = this.idx - 1;
        }
      }
    });
  }
};
</script>
